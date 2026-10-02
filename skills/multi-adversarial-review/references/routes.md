# Routes — adapters, recipes, liveness, and failure handling

Read this file **before launching or judging any route** — never launch from
memory. It consolidates the route mechanics the core skill (`../SKILL.md`)
binds by pointer: launch discipline, the sandbox stack, per-model adapters,
copy-paste recipes, heartbeats, stalls, and the terminal-state taxonomy.
Project directives still win over everything here.

## Launch Discipline

Four rules apply to **every** external route, regardless of adapter. Each has
produced a false `route-failed` when skipped.

1. **Background through the harness-native mechanism, never a shell `&`.**
   Many agent harnesses run each tool command in a scope that reaps child
   processes when the command returns — a route launched with a trailing `&`
   dies the instant the launching tool call ends (observed: a `( … cn … ) &`
   child exits within seconds with 0 bytes, while the identical foreground
   command streams fine). On Claude Code, pass the full command (no `&`) to the
   Bash tool with `run_in_background: true`. A raised foreground timeout is the
   fallback only when it comfortably exceeds the review's wall-clock; never run
   a route under a default short foreground cap (~2 minutes on many hosts) — a
   healthy review killed by the cap is indistinguishable from a stall unless
   you check (a one-word smoke prompt returning instantly proves the route was
   fine and the cap killed the real run).
2. **Redirect stdin from `/dev/null`.** `codex exec`, `pi`, and `cn` read
   stdin for additional input; backgrounded with an open terminal stdin they
   block forever (`codex.out` literally reads `Reading additional input from
   stdin…`) and a healthy route looks identical to a stall. The `< /dev/null`
   in every recipe below is load-bearing, not decoration.
3. **Size the ceiling to the review, and await the terminal state.** Ten
   minutes suits a tiny diff; a repository-context or scratch-probe review
   legitimately runs 30–60 minutes. Never launch the next family past a live
   stage — advancing past a running review violates sequential pressure and
   turns a healthy stage into an absent one. Note the native background task
   itself has a finite lifetime (an APPARENT ~30-minute reap was inferred from
   one incident — treat as a working estimate): a reaped-while-streaming route
   is `harness-killed`, not `route-failed` — check the heartbeat before
   classifying. For a review expected to run long, split it into bounded
   lenses or detach from the reaper (`setsid`/`nohup`, output to files, PID
   captured) and poll.
4. **Two ledger appends per stage, never an amendment.** In-flight stage state
   lives in the project's designated append-only ledger: at LAUNCH append one
   record (stage, baseline SHA, route, PID/task id, stdout path, heartbeat
   location, started-at, ceiling — attributed to the REVIEWER family, never
   the orchestrating session model); at TERMINAL state append the outcome
   (state from the taxonomy below, elapsed, last heartbeat, output bytes,
   terminating actor). Both ride the stage's disposition commit; the pair
   makes stage duration a mechanical read. On restart or context loss: re-read
   the skill, then the ledger tail — **a launch record with no matching
   terminal record is an UNRESOLVED stage; reconcile before proceeding** and
   never launch another family past it. A never-launched stage is `not-run`
   and gets a TERMINAL-ONLY record — a synthetic kickoff would fabricate a
   launch and an elapsed effort.

Prose discipline decays over a long session, with or without compaction — the
incident behind these rules ran for hours with the mechanics written and in
reach, and they simply stopped being applied. That is why the core skill makes
re-reading this file at stage time mandatory; wrapping route mechanics in
committed runner scripts is the stronger mitigation when a host accumulates
them.

## Sandbox Topology

Choose capability flags from the **effective sandbox stack**, not from the
route name. Before launch, record the outer sandbox, the access inherited by
child processes, its writable allow-list, and whether the route applies
another OS sandbox of its own.

**Nested Seatbelt defect (macOS).** When the session already runs under an
outer OS sandbox that confines children — [nono](https://nono.sh/docs/cli/clients/codex),
or an agent harness's own profile (e.g. a Claude Code host that confines every
spawned process to the workspace + session scratchpad) — Codex's attempt to
apply its own per-command Seatbelt profile can fail with `sandbox_apply:
Operation not permitted`, sometimes only intermittently (a run can start
static and die mid-run). A harness-level "disable sandbox" flag for the
launching tool does **not** escape the outer profile; children still inherit
it.

When the outer sandbox is **confirmed**, launch Codex with
`-s danger-full-access`: this disables only Codex's *inner* sandbox and does
not loosen the outer allow-list, which remains the enforcement truth. Keep the
normal approval policy; never substitute
`--dangerously-bypass-approvals-and-sandbox`. This is a scoped adapter for a
confirmed outer profile, never a portable default on an unsandboxed host.

Empirical (voglang macOS host): the nested launch produced static-only or
mid-run-dying shells (2026-07-14, ITER_262/263); with `-s danger-full-access`
the shell is fully live — `rg`/`git` and a complete `dune runtest` ran clean
in a pinned worktree (2026-07-15, ITER_267). Read older "codex is
static-inspection-only" notes as describing the nested launch, not the route.

**Capability caveat under a wide outer profile.** If the outer profile grants
write access to the whole workspace, the reviewer has full write capability
inside it: `No Writing Anywhere` is prompt-plus-audit and `Scratch Writing
Only` is worktree convention-plus-audit, **not** a physical reviewer-specific
write barrier. Keep the isolated worktree and authority snapshots, record the
caveat, never claim hard read-only enforcement — and run the **post-run write
audit over the PRIMARY checkout and every authority repository, not just the
review worktree** (an unattributed file appearing in the primary checkout
during a review window must be reconcilable from the audit). Hard enforcement
requires an outer profile already limited to the review worktree, or running
the reviewer outside the outer layer with its own `read-only` /
`workspace-write` sandbox.

## Review Harness Budget

Keep an A/B honest: when comparing routes, hold the prompt, model, reviewed
commit, worktree, authority scope, capability mode, and tool policy fixed;
change only the harness. Do not infer a model-family weakness from one slow
harness.

Prefer a tool loop that returns to observation frequently over one assistant
turn that reasons for tens of thousands of tokens before its first tool call.
For configurable routes, cap one assistant turn at **16,384 output tokens**
(**8,192** preferred to start) — a per-turn bound, not a total budget.

Expose the smallest useful tool set:

- `plan` / `spec`: read, list, search; add a shell only when inspection
  requires it;
- `code` / `code-vs-plan` in a disposable worktree: read, list, search, shell,
  and temporary edit/write tools for targeted probes;
- disable web fetch, skills, subagents, background-job management, checklists,
  and interactive-question tools unless the review specifically needs one.

When a route emits structured model/tool events, preserve the raw stream
through disposition — it is the heartbeat proxy and the best trace of what the
reviewer actually read and ran.

## Adapters

### Claude

On a Claude host, Claude is normally the implementer, so these routes are a
**same-host sanity adapter, not an independent gate** (core skill § Host
Awareness). Explicit prompt mode: `claude -p "$REVIEW_PROMPT"`. The local
`/code-review` is a strong opaque adapter (multi-agent verify/dedup/rank);
capture its output and continue with the disposition step; never `--fix` for a
reviewer pass.

### Codex

Explicit prompt mode: `codex exec -C "$REPO" "$REVIEW_PROMPT"`. Use the normal
Codex sandbox on an unsandboxed host; use the `-s danger-full-access` adapter
only under a confirmed outer profile (§ Sandbox Topology).

**Pin the model tier at launch.** Bare `codex exec` runs the CLI's configured
DEFAULT model and reasoning effort — often a lower tier than a gate stage
warrants (observed 2026-07-15: a gate launch silently ran the workhorse-tier
default). Pass `-m <model>` and `-c model_reasoning_effort="<effort>"` per the
host project's model bindings, then verify the transcript header's `model:` /
`reasoning effort:` lines after launch and record the tier in the kickoff
record. A stage that completed at the wrong tier is **corroboration, not the
gate** — relaunch with the identical prompt (held fixed; only the tier
changes) at the bound tier.

Inside Claude Code with `codex-plugin-cc`, `/codex:adversarial-review` is a
strong adapter for challenging design choices; it is not plain Codex CLI.

### GLM 5.3 and Other Third Models

Prefer **Pi in text mode**: its bounded-turn loop has produced faster, more
inspectable GLM reviews than cn's long single-turn loop on the same codebase.
Do **not** use `--mode json`. Pi's per-delta JSON events may repeat the growing
accumulated partial message, making log volume roughly quadratic; two reviews
produced >100 MB streams in minutes and stopped progressing. Text mode keeps
the route quiet until the final answer, so monitor scratch-worktree activity
and the wall-clock ceiling instead. Disable extensions and skill discovery so
the tool surface is explicit (recipe below).

**cn (Continue CLI)** is the first fallback, with a review-specific model
config capped at 16,384 output tokens (8,192 for a small diff) and unused
tools excluded; keep `--verbose` for its rotating chunk heartbeat. If no
capped config exists, cn may run explicitly uncapped — record that fact rather
than treating its wall time as model evidence. **OpenCode** is the final
fallback. Verify identifiers with `pi --list-models glm-5.3` or `opencode
models` when needed.

## Route Recipes

Don't re-derive route mechanics per run, and don't build a packet. Point each
route at the repo with a base range and run it backgrounded. `$BASE` is the
reviewed baseline (the prior stage's disposition commit, or the implementation
baseline for the first stage); the reviewer diffs `$BASE..HEAD` itself.

Set `$REVIEW_ROOT` to the smallest safe common ancestor of the repository and
every required authority directory (for a single-repo review it is `$REPO`).
Spec mode must enumerate the absolute required-authority paths in the prompt
and enforce the coverage gate in `spec-review.md`; starting a route in the
artifact repository is not proof it can traverse to sibling canon.

The chain is **cumulative**: tell each reviewer to read the diff **and** the
committed prior findings and build on them — *and hunt for what they missed*,
so anchoring on the prior framing doesn't shrink coverage. Only the
disposition panel runs blind.

```sh
BASE=<baseline-sha>; SP=<scratch-dir>; REPO=$(git rev-parse --show-toplevel)
REVIEWED=$(git -C "$REPO" rev-parse HEAD)
REVIEW_ROOT=<isolated-per-run-root-usually-$SP>
REVIEW_WORKTREE="$REVIEW_ROOT/$(basename "$REPO")_mar_<iteration>_<family>"
REVIEW_REPO="$REVIEW_WORKTREE" # use "$REPO" when the stage has no worktree
read -r -d '' REVIEW <<EOF
Adversarial review — you are an auditor, not a contributor.
Repository: $REVIEW_REPO
Source repository: $REPO
Scope: git -C $REVIEW_REPO range $BASE..$REVIEWED.
For a plan cut: git -C $REVIEW_REPO diff $REVIEWED.
Target mode: <code | plan | code-vs-plan | spec>.
Required authority snapshots (absolute paths): <path list | none>.
Capability mode: <No Writing Anywhere | Scratch Writing Only>.
For No Writing Anywhere, do not create, edit, delete, stage, or commit files.
For Scratch Writing Only, this is a disposable worktree: you MAY create temporary
tests or probes and run targeted builds/tests when they materially strengthen the
review; do not fix production code, stage, or commit. Report every probe diff,
command, and observed result. You may finish without writing when no probe helps.
Read the diff AND the committed prior review findings (git log, PROGRESS/STATUS);
build on them — deepen or challenge each, don't re-derive — and separately hunt
for what those passes missed.
Intent: <what changed and why>.
Focus: does it satisfy the intent; what assumption fails first in production;
what edge / error / state / integration path is unproven; are tests meaningful or
only green; needless complexity or the wrong abstraction; security, privacy,
concurrency, or data-loss risk.
Finding bar: actionable issues with concrete evidence and file/line refs; no
style nits unless they hide a correctness or maintenance risk; don't force a
finding — "No findings" is valid only if it names the weakest remaining
assumption.
Output: findings first, by severity; for each — severity, evidence, why it
matters, suggested verification or fix.
EOF
```

For a worktree-backed stage, create the reviewed state before launch and remove
it only after disposition evidence is retained:

```sh
git -C "$REPO" worktree add --detach "$REVIEW_WORKTREE" "$REVIEWED"
# ...run and disposition the reviewer...
git -C "$REVIEW_WORKTREE" status --short --untracked-files=all
# ...retain every probe diff/result and confirm the scratch state is disposable...
git -C "$REPO" worktree remove --force "$REVIEW_WORKTREE"
```

For `spec`, adapt the prompt overlay from `spec-review.md` — the generic
production/test focus is not the spec rubric.

The trailing `&` in each recipe below is command-shape shorthand — launch
through the harness-native background (§ Launch Discipline), keeping the
`< /dev/null` regardless.

**Claude** — same sibling-authority scope as external routes. No Writing
Anywhere (`--add-dir` is load-bearing when canon is outside `$REPO`):

```sh
( cd "$REPO" && claude --permission-mode plan --add-dir "$REVIEW_ROOT" -p "$REVIEW" ) < /dev/null > "$SP/claude.out" 2>&1 &
```

Scratch Writing Only — start in the disposable worktree with only the probe
tools:

```sh
( cd "$REVIEW_WORKTREE" && claude --permission-mode acceptEdits \
    --tools Read,Grep,Glob,Bash,Edit,Write \
    --allowedTools Read,Grep,Glob,Bash,Edit,Write \
    -p "$REVIEW" ) < /dev/null > "$SP/claude.out" 2>&1 &
```

**Codex** — pin the tier (§ Adapters); `read-only` enforces No Writing on an
unsandboxed host:

```sh
codex exec -m "$CODEX_REVIEW_MODEL" -c model_reasoning_effort="$CODEX_REVIEW_EFFORT" \
  -s read-only -C "$REPO" --add-dir "$REVIEW_ROOT" "$REVIEW" < /dev/null > "$SP/codex.out" 2>&1 &
```

Scratch Writing Only — point `workspace-write` at the disposable worktree; the
prompt still forbids production fixes and commits:

```sh
codex exec -m "$CODEX_REVIEW_MODEL" -c model_reasoning_effort="$CODEX_REVIEW_EFFORT" \
  -s workspace-write -C "$REVIEW_WORKTREE" "$REVIEW" < /dev/null > "$SP/codex.out" 2>&1 &
```

Under a confirmed outer sandbox, replace either `-s` value with
`-s danger-full-access` (§ Sandbox Topology) and record the outer profile's
writable scope plus the capability caveat.

**GLM 5.3 via Pi (preferred)** — use text mode, backgrounded through the
harness-native mechanism. The tool list below is No Writing Anywhere with
repository inspection; `bash` can write, so remove it when no hard read-only
sandbox backs it. For Scratch Writing Only, run from the disposable worktree
and append `edit,write`:

```sh
( cd "$REVIEW_WORKTREE" && pi --model zai/glm-5.3 \
    --thinking high --no-session --no-extensions --no-skills \
    --tools read,bash,grep,find,ls -p "$REVIEW" ) \
    < /dev/null > "$SP/pi.out" 2> "$SP/pi.err" &
PI_PID=$!
```

Text stdout may remain empty until completion. Keep the process in the
background and poll its captured task/PID, but treat process existence as
aliveness only, never proof of progress. For Scratch Writing Only, inspect the
worktree on each poll: look for new/changed probes or tests with `git status`
and for advancing `_build` artifacts (for example `_build/trace.csexp`). Record
the last observed worktree/build activity and enforce the wall-clock ceiling.

**GLM 5.3 via cn (fallback)** — bind the capped review config; `--readonly`
for No Writing Anywhere; Scratch Writing Only solely in a disposable worktree
(`--auto`, same exclusions, pre/post snapshot). Capture the PID at launch — cn
presents to the OS as a `node` process (comm `MainThread`), so no name match
finds it:

```sh
( cd "$REVIEW_WORKTREE" && cn -p --readonly --verbose \
    --config "$CN_REVIEW_CONFIG" \
    --exclude Fetch --exclude Checklist --exclude CheckBackgroundJob \
    --exclude AskQuestion --exclude Skills "$REVIEW" ) \
    < /dev/null > "$SP/cn.out" 2>&1 &
CN_PID=$!
```

With `--verbose`, cn writes one `Received chunk` line per streamed token-chunk
to its rotating `$CONTINUE_GLOBAL_DIR/logs/cn*.log` files — re-resolve the
newest file on every poll; watching only `cn.log` reports a false stall after
rotation.

## Liveness, Stalls, and Cleanup

**Heartbeats.** Final-answer stdout may stay quiet, so empty stdout alone is
not a stall. Pi text mode has no event heartbeat: process/task existence proves
only aliveness. For Scratch Writing Only, use advancing worktree evidence — new
or changed probes/tests and `_build` activity — as the progress signal, while
recognizing that a reasoning interval may write nothing. Judge it ultimately by
the wall-clock ceiling. cn uses the newest rotating `cn*.log`; Codex and Claude
may also stay flat through a think window and are judged by ceiling plus process
liveness. A long silent interval is not itself a stall on a route that normally
emits only final output.

**Reap finished and abandoned jobs.** Piled-up review processes contend and
slow every route; on cancel, kill zombies too, and don't stack routes — the
chain is sequential across families anyway (parallel lenses on one committed
state are the deliberate exception).

**Kill by exact process, never `pkill -f "codex exec"`.** A command-line
pattern also matches the launcher script carrying the same string in its args,
so the cleanup kills itself mid-run. Use `pgrep -x codex` / `pgrep -x pi`; cn
is the exception (a `node` process) — kill the PID captured at launch. Keep
the reap step in a separate command from the launch so a kill can never race
the spawn.

**Terminal route states — record the one that happened, never a conflation:**

- `completed` · `harness-killed` (the harness reaped a live route — check the
  heartbeat) · `manually-cancelled` · `rate-limited` (a real 429/quota
  response in hand, never inferred) · `route-failed` (the route errored,
  stalled dry, or produced unusable output) · `not-run` (never launched —
  record exactly that; a never-launched stage written up as `route-failed` is
  a FALSE record: what happened is the family was absent).

Per stage record: task/PID, reviewed range, elapsed wall-clock, last-heartbeat
time, output bytes, terminating actor (completion / harness / agent / route).
Run reviews that execute diagnostics against a disposable worktree with its
own build directory — a "read-only" review that runs build commands still
takes the project's build lock, and a suite run in the primary checkout can
starve or kill it. Pin the worktree to the kickoff record's baseline SHA: the
primary tree legitimately carries uncommitted ledger rows while a review runs.

**Ceiling exceeded:** cancel, record `route-failed`, retry once with a
narrower scope, a longer explicitly-chosen ceiling, or a safer route; if the
retry fails, stop or move to the next model only with an explicit
degraded-route note. A reviewer that produces setup chatter, asks for missing
tools, edits the primary checkout, or gives a generic summary instead of
findings is a malformed route — retry once with a tighter prompt.

**`sandbox_apply: Operation not permitted` before useful commands** is the
nested-sandbox launch defect (§ Sandbox Topology) — a launch-environment
defect, not a model failure or family absence. Kill it without waiting out the
ceiling; retry once with `-s danger-full-access` if the outer sandbox is
confirmed; otherwise change topology or record `route-failed`. Never retry an
identical launch.

**A retry after truncation or malformed output must be a MINIMAL delta —
remove only the cause, never restructure the ask.** The common truncation is a
reviewer ending mid-investigation reaching for a tool; block that one detour
(state the suite is green, forbid build/test commands) and nothing else. Do
not reword the ask into "produce findings NOW", a rigid schema, or an
enumerated focus list — a retry that changes the question can steer the
verdict, so its output is no longer a faithful review of the same change. If a
minimal-delta retry still spirals, record `route-failed` and lean on the other
families: a verdict is trustworthy when an un-steered reviewer independently
reaches it, not because a reworded retry restated it.
