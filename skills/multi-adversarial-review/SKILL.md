---
name: multi-adversarial-review
version: 0.2.0
description: "Sequential multi-model adversarial review. A lead commits a stable code, plan, or specification state; independent reviewer models inspect it one at a time; after each pass the lead verifies, fixes, revises, or defers the findings and commits the outcome before the next model reviews. Use when the user says 'mar', 'run mar', 'multi-adversarial-review', asks for a Claude/Codex/GLM review chain, cross-model review commits, adversarial plan review, spec or design-note review through project design principles, copy review of a document with its readers as the lenses, or a repeated review-disposition-commit gate. Do not use for ordinary one-pass code review, same-model subagent review, simultaneous panel discussion, or review synthesis with no lead response between passes."
user-invocable: true
---

# /multi-adversarial-review — Sequential Multi-Model Review

> **Quick Reference:** See [HELP.md](HELP.md) for commands, targets, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.
> For detailed mechanics or edge cases, the full SKILL.md has the complete specification.
> `mar` is the short name; it is the same skill.

Run a committed-state review chain that uses model diversity to catch blind
spots. The defining rule is sequential pressure: reviewer N inspects a stable
commit, the lead addresses that review and commits, then reviewer N+1
inspects the new stable commit.

**Lead** means the implementer for code, the editor for a plan or spec, and the
maintainer when a design ruling is required. A spec editor may clarify and expose
OPEN work but must not silently make a maintainer-owned design decision.

**Project directives win.** Everything here is a portable default. Where the host
repository states its own cadence — `AGENTS.md`, an iteration/process spec such as
`ITER.md`, or an explicit maintainer instruction — that governs, and this skill's
defaults (chain shape, stage ordering, commit count, waiver rules) yield to it.
Follow the project; fall back to this skill only for what the project leaves
unspecified.

**This file is the doctrine; two references carry the mechanics.** Read
[`references/routes.md`](references/routes.md) **before launching or judging any
route** — adapters, sandbox topology, copy-paste recipes, heartbeats, stalls,
kill/retry discipline live there, and launching from memory is how healthy
routes get recorded as failures. Read
[`references/disposition-panel.md`](references/disposition-panel.md) only when a
contested finding trips the panel gate (§ Pushback). For `spec` targets, read
[`references/spec-review.md`](references/spec-review.md) before constructing
prompts or dispositioning findings. For `copy` targets, read
[`references/copy-review.md`](references/copy-review.md) the same way.

For background and prior art, read the survey this skill was built from,
`multi-adversarial-review-prior-art.md` in [vog_kit](https://github.com/amattn/vog_kit),
when changing this skill or when choosing route policy for a new host.

## Host Awareness

This copy runs on a **Claude Code host**, so Claude is normally the implementer.
The core prior-art rule is *the partner reviews, never the host*: a same-host
reviewer shares the author model's blind spots, so it does not count as
independent adversarial coverage.

Therefore, when Claude is the implementer:

- The independent reviewer families are **Codex** and a **third non-family model
  such as GLM 5.3** — routed out of this host via `codex exec` or Pi (cn or
  OpenCode as fallback).
- A Claude reviewer (subagent or `claude -p`/`/code-review`) is a **same-host
  sanity adapter**, not an independent gate. Use it for a fast local pass, but do
  not present it as one of the cross-model gates, and mark the chain degraded if
  it is the *only* review that ran.
- A Claude stage counts as independent **only** when the lead/author was a
  different model or a human — e.g. you are reviewing work authored by Codex, GLM,
  or a person. In that case treat Claude as a legitimate cross-model reviewer.

## Quick Contract

- Prefer true cross-model or cross-host reviewers: Claude, Codex, and a third
  non-family model such as GLM 5.3 when available.
- Do not present same-host subagents as independent adversarial review.
- Reviews are cumulative by default. Each stage reviews a stable commit and MAY
  read the committed prior findings — Claude's `/code-review`, an earlier stage's
  disposition — and build on them; that layering is intended (GLM builds on the
  local review, Codex builds on GLM), not a leak. Only *uncommitted* work is
  withheld — commit between stages. Full blindness applies to **one** place: the
  disposition panel (§ Pushback), the rare contested finding. (Empirically backed:
  in prior-art § Case Study, the cumulative chain caught and correctly escalated a
  live regression that the otherwise-identical blind chain under-rated on the same
  code.)
- Do not blindly apply reviewer feedback. Verify every finding against source.
- Do not force fake findings. "No findings" is valid when it names residual risk.
- Do not use reviewer-side writes in the primary checkout.
- Run each stage at the capability tier the gate warrants: pin the reviewer's
  model/effort explicitly at launch (`references/routes.md` § Adapters — CLI
  defaults can silently run a lower tier). A stage that completed at the wrong
  tier is corroboration, not the gate.
- In `spec` mode, complete the authority coverage gate in
  `references/spec-review.md` before crediting a reviewer stage. Partial-canon
  review is `route-failed`, not a completed review with a caveat.
- In `copy` mode, name the readers before launching. A copy review with no
  named reader is `route-failed: reader-undefined`
  (`references/copy-review.md`).

## Targets

Choose one target mode from the request and local context.

| Target | Use when | Review asks |
| --- | --- | --- |
| `code` | An implementation is committed or ready to commit. | Does the code satisfy intent without regressions? |
| `plan` | A proposed plan/cut/order needs stress-testing before implementation. | Are dependencies, sizing, order, and assumptions sound? |
| `code-vs-plan` | Code claims to implement a prior plan. | Did the implementation actually follow the plan and avoid hidden scope changes? |
| `spec` | A design spec, RFC, protocol, or normative design note (a Vog VDN, for example) needs review. | Is the proposed meaning principled, coherent, viable, honestly scoped, and ready for maintainer ratification? |
| `copy` | A document for human readers (README, guide, release notes, the prose of a plan or spec) needs review as writing. | Can each named reader find what they need, trust it, and stop early, without a rule being lost? |

For `spec`, `references/spec-review.md` defines the compact
overall/strong/needs-work/viability/open/mechanical/readiness output and, when
the project has durable design principles, makes alignment with them the primary
lens. Select `spec` automatically for a project's design-note type (a Vog VDN,
for example); never force it into `plan`.

For `copy`, `references/copy-review.md` makes the document's named readers the
lenses and defines the overall/strong/needs-work/fidelity/judgment/readiness
output. `copy` reviews whether readers can use the text; `spec` reviews what the
text proposes. A design note that needs both gets `spec` first, then `copy` on
the settled text. Reviewers never change meaning: a fix that would alter a rule
or a decision is a `meaning` finding for the owner.

For `code` and `code-vs-plan`, every model-stage review outcome normally becomes
its own disposition commit. For a single-model `plan` review, fold findings into
the plan before the plan commit unless the repository cadence requires separate
review commits. For a multi-model `plan` chain, keep the central invariant:
commit the plan disposition after each model stage before the next model reviews.
For a multi-model `spec` chain, commit the stable artifact and durable review
ledger after each stage. The lead may revise confirmed document defects or mark
design work OPEN; only the maintainer ratifies semantic choices. A `copy` chain
follows the same rule: commit the edited artifact and its disposition record
after each stage.

## Chain

Default chain when the user gives no model order, **with Claude as the
implementer on this host** (see § Host Awareness — Claude does not review its own
work as an independent gate):

1. Stable baseline commit by Claude (the current agent) or a prior author.
2. GLM 5.3 or another non-family model stage through Pi (cn or OpenCode as fallback).
3. Lead disposition commit.
4. Codex stage.
5. Lead disposition commit.

If the lead/author was **not** Claude (you are reviewing work authored by Codex,
GLM, or a human), add a Claude stage as a legitimate cross-model reviewer,
following the same commit-between-stages discipline: Claude stage → disposition
commit → GLM stage → disposition commit → Codex stage → disposition commit.

**Ordering — strongest independent finder last.** Because the chain is cumulative
(each stage builds on the committed prior findings), the *last* stage inherits the
richest record, so place the family that finds the deepest correctness bugs for
your codebase there. On the Vog compiler, the origin project, that is **Codex**
(hence GLM → Codex above): in
the prior-art § Case Study controlled comparison, Codex-last read GLM's committed
mechanism-correction and escalated a pre-existing bug to its true severity, while
the blind variant left it under-rated. This ordering is derived from a single
iteration; treat it as the default, not a law, and reverse it if your codebase's
evidence points the other way — or if a project directive (§ intro) specifies its
own order, which wins.

Use the order requested by the user when specified. If a route is unavailable,
try the next configured route and record the miss. If all cross-model routes are
unavailable, stop or proceed only in explicitly degraded mode. Also mark the
chain degraded when any requested model family does not run, even if other
families completed.

## Stage Parallelism

The chain is sequential across model families, but a single model stage may run
several reviewers in parallel with different lenses over the same committed
state, deduplicated and verified before one disposition commit. Default to one
reviewer per stage for cost control; use three to five lenses when the user asks
for high scrutiny, the diff is risky, or the repository cadence expects a
heavyweight review.

Recommended lenses: correctness/edge-cases/failure paths; tests and whether
green checks would catch a break; architecture/boundaries/coupling; simplicity
and accidental scope growth; security/privacy/data-loss/concurrency/reliability.
For `spec`, replace these with the reference's principle-fit, coherence,
status-honesty, evidence, viability, and canon-cascade lenses; preserve positive
strengths as well as adversarial findings. For `copy`, the lenses are the named
readers, one reviewer each, plus the record and fidelity lenses from the
reference.

Within a stage, reviewers should not see each other's output until every lens
has finished. Cross-lens agreement is a priority signal, not proof. Deduplicate
and verify findings, then run exactly one implementer disposition step for the
whole stage.

## Capability Modes

Use exactly one of these reviewer capability modes per stage.

### No Writing Anywhere

The reviewer must not create, edit, delete, stage, or commit files in any
worktree. It may read, search, inspect diffs, and run non-writing diagnostics
when safe. It may include proposed tests or patches in its output as text, but
those patches are not applied or observed.

Default for `plan`, `spec`, and `copy`, where empirical execution usually does
not add evidence. If the route exposes a general shell, this mode is hard-enforced only
when the harness or sandbox actually denies writes; a prompt that says
read-only is not an OS write barrier (`references/routes.md` § Sandbox
Topology — including the post-run write-audit scope).

### Scratch Writing Only

The reviewer may create temporary tests or probes only in an isolated scratch
copy or disposable git worktree. It must not edit the primary checkout, and
scratch permission never includes fixing production code.

Require the reviewer to report: scratch/worktree identity; the probe diff; the
command run; the observed result; whether the probe failed before any
production-code fix; minimal reproduction steps. The implementer ports accepted
probes into the primary checkout, watches them red, fixes to green, and commits.

Default for substantive `code` and `code-vs-plan` review when a disposable
worktree is available. Pin the worktree to the exact reviewed commit, give it
an independent build directory, and allow targeted builds/tests/probes there.
A reviewer should run the cheapest probe that can falsify a material claim, not
rerun a full green suite unless the suite itself is under review. **Scratch
permission is optional capability, not a probe quota** — the reviewer may
finish without writing. Snapshot the worktree before and after, retain probe
diffs and results through disposition, then discard the worktree.

### Worktree Placement

Put each writable review worktree in an **isolated per-run review root**. In a
multi-repository workspace, snapshot every required authority into that root at
launch, as a sibling of the worktree (normal sibling names — `../vog_specs` in
the origin project — keep familiar paths working):

```text
<review-root>/
├── <target>_mar_<iteration>_<family>/   # writable disposable worktree
└── <authority>/                         # read-only snapshot, no .git history
```

A harness-owned session scratchpad is the default review root; a project may
bind its own. Do not place a Scratch Writing Only worktree beside real
authority repositories unless an outer sandbox makes them physically read-only
to the reviewer. Snapshot the authority's working files (excluding `.git`,
build output, caches) and record source path, source commit, dirty-state
summary, and a manifest/digest so the disposition identifies exactly which
canon was read. `a-w` on the snapshot is an accidental-write guard, **not** a
security boundary — the outer sandbox is the physical enforcement.

Topology is convenience, not authority: the prompt must still enumerate every
snapshot authority by absolute path. Create and remove the worktree through the
target repository's `git worktree` commands, never by deleting its directory;
before removal, retain any probe evidence disposition needs.

## Route Adapters and Route Recipes

**All route mechanics live in [`references/routes.md`](references/routes.md) —
read it before launching or judging any route, every time; mandatory after any
compaction with a chain pending or in flight.** It owns: launch discipline
(harness-native backgrounding, the `< /dev/null` stdin redirect, ceilings), the
sandbox stack and the Codex `-s danger-full-access` adapter for confirmed outer
sandboxes, model/effort tier pinning, per-route commands for Claude / Codex /
GLM (Pi, cn, OpenCode), the review-prompt template, and the harness budget.

The invariants that must survive any summary of it:

- Background every route through the harness-native mechanism with stdin from
  `/dev/null`; never a bare shell `&`, never a short foreground cap.
- Point the route at the repo with a base range — no packet; the chain is
  cumulative, so tell the reviewer to build on committed prior findings AND
  hunt for what they missed.
- Pin external reviewers to a disposable worktree at the reviewed SHA; pin the
  model tier explicitly; audit writes afterward (primary checkout included).
- **AWAIT each stage's terminal state before launching the next family.**

## Disposition Step

After each model stage, the lead must produce a disposition before the
next model stage runs. If a stage used parallel lenses, deduplicate those lens
findings into one stage disposition — but dedup must be **non-lossy**: two
findings at the same site that differ in *kind* (a security reading and a
correctness reading) are not duplicates. Record each original lens finding, or
mark it an explicit pointer-duplicate of another, so every raised finding is
traceable to a disposition and none is silently merged away.

Use these states:

- `accepted-fixed`: confirmed and fixed.
- `accepted-deferred`: confirmed but deferred with a reason and future home.
- `rejected`: not confirmed or technically wrong, with evidence.
- `unclear-blocked`: cannot decide without missing information.
- `no-findings`: reviewer found no actionable issue.
- `route-failed`: reviewer stalled, errored, or produced unusable output.
- `contested`: a disposition panel could not resolve a guarded finding — the
  distinct terminal for an unresolved standoff (§ Pushback).

In `spec` mode, tag accepted findings as `design`, `evidence`, `status/canon`,
or `mechanical`. `accepted-fixed` means the document was corrected;
`accepted-deferred` means real design work stays OPEN with its tradeoff,
dependency, authority/owner, and future home. Mechanical cleanup never closes a
design item.

In `copy` mode, tag accepted findings as `cut`, `reorder`, `stale`,
`provenance`, `gloss`, `meaning`, or `mechanical`. A `meaning` finding is
`accepted-deferred` to the owner, never fixed by the editor. A `rejected` cut
is a normal outcome; record the reason where the next pass will read it.

`contested` is its own terminal state, **not** a marker on a resolved
disposition: a panel ran a guarded finding to the cap and picked no side, so it
is carried unresolved — with both sides' evidence — for maintainer audit. It
asserts neither `accepted-deferred` nor `rejected`. Distinct from
`unclear-blocked`, which is a *draft* disposition that can admit a finding to a
panel but is never the panel's output. `contested` **blocks release, never the
next review stage.**

For production-code fixes, write or port the failing check first when practical,
watch it fail, implement the fix, and verify it passes.

The disposition commit must always have an auditable payload. Prefer a small
project-local review record when the repository already has one (progress log,
review ledger, iteration journal). Record at minimum the reviewed commit or
range, route, capability mode, result state, and either findings or
`no-findings` / `route-failed`. A `no-findings` result must still name the
weakest remaining assumption or residual risk — "none" alone manufactures false
confidence. If the project has no durable tracking file and there are no code or
test changes, an explicit empty commit is acceptable:

```sh
git commit --allow-empty \
    -m "review: Record <model> disposition" \
    -m "Reviewed: <commit-or-range>" \
    -m "Route: <route>; capability: <no-writing-anywhere | scratch-writing-only>" \
    -m "Result: <disposition-state>" \
    -m "Findings: <none | summary of findings and disposition evidence>"
```

Do not start the next model stage until this disposition is committed — that is
the sequential-pressure rule: each stage reviews a *stable* commit. The committed
disposition is auditable state **and** intended input to the next stage (the
cumulative chain needs no packet and no record-exclusion — point the next stage
at the repo and let it read the prior findings). **Blindness is reserved for the
disposition panel**, the only place a reviewer is scoped away from prior output.

## Pushback / Re-Review

Use pushback to audit dispositions and to escalate a contested finding — not as
the next review stage. Once a stage's findings exist and the implementer has
drafted dispositions, cross-examination of those dispositions is allowed and
useful. Two levels: a one-shot disposition audit (the default) and a bounded
disposition panel (escalation for contested findings only).

### One-Shot Disposition Audit (default)

A pushback prompt includes the prior review, the implementer's dispositions, and
evidence:

```text
You previously reviewed this change and reported the findings below.

Prior review:
<verbatim reviewer output>

Implementer disposition:
- Finding A: accepted. Fixed in commit <sha>. Evidence: <test/line/diff summary>.
- Finding B: rejected. Reason: <technical reason>. Evidence: <file/line/spec>.
- Finding C: deferred. Reason/home: <risk item / follow-up>.

Review task:
Audit the dispositions only. Do not search for new issues unless they are caused
by the fixes. For each prior finding, say one of:
- resolved
- still open
- rejection accepted
- rejection not accepted
- deferral acceptable
- deferral not acceptable

If you disagree, cite concrete evidence.
```

### Disposition Panel (escalation only)

When a one-shot audit deadlocks on a **guarded** finding — either party rates it
high-severity/security-sensitive and the draft disposition is `rejected`,
`accepted-deferred`, or `unclear-blocked`, and no cheap probe or citation
settles it — escalate to the bounded panel:
**read [`references/disposition-panel.md`](references/disposition-panel.md)**
for the convene gate, roles, round protocol, and the `contested` terminal. The
two invariants that must survive any summary: a debate verdict is not
verification (confirmed findings still get the failing-check-first fix
discipline), and the raw panel thread stays out of the committed tree, withheld
from any re-convened panel on the same finding.

## Stalls and Failures

**Liveness judgment, stall thresholds, kill discipline, retry rules, and the
full terminal-state definitions live in [`references/routes.md`](references/routes.md)
§ Liveness, Stalls, and Cleanup — judge no route without them.** What must
survive any summary:

- Pi runs in background text mode, never JSON mode. Its stdout may stay empty;
  process existence proves only aliveness. For scratch-writing review, inspect
  new/changed probes and `_build` activity for progress, then enforce the
  wall-clock ceiling. Use cn's rotating logs where available; a harness-reaped
  live route is `harness-killed`, never `route-failed`.
- **Terminal states — record the one that happened, never a conflation:**
  `completed` · `harness-killed` · `manually-cancelled` · `rate-limited` (a
  real 429 in hand, never inferred) · `route-failed` · `not-run` (never
  launched — a never-launched stage written up as `route-failed` is a FALSE
  record; it gets a terminal-only ledger row, no synthetic kickoff).
- Every stage writes a **launch record and a terminal record** to the project's
  append-only ledger (two appends, never an amendment), riding the disposition
  commit. **An unmatched launch record at pickup is an UNRESOLVED stage —
  reconcile before proceeding**; never launch another family past it.
- A stalled or failed route is a **degraded gate, not a waiver** — retry once
  with a **minimal delta** (remove only the cause; a reworded ask can steer the
  verdict), then move on only with an explicit degraded-route note.

## Final Report

Report the chain as an audit trail:

```text
Review chain
- <sha>: stable baseline
- <sha>: after Claude disposition - <accepted/rejected/deferred/no findings>
- <sha>: after GLM disposition - <accepted/rejected/deferred/no findings>
- <sha>: after Codex disposition - <accepted/rejected/deferred/no findings>

Route status
- Claude: <route, capability mode, status>
- GLM: <route, capability mode, status>
- Codex: <route, capability mode, status>

Confirmed findings
- <finding, reviewer, disposition, commit>

Rejected or unconfirmed findings
- <claim, reviewer, reason rejected or unresolved>

Residual risk
- <routes unavailable, tests not run, scratch probes not ported, or scope not covered>
- <contested findings that hit the panel round cap unconverged>
```

For `spec`, also report the compact assessment required by
`references/spec-review.md`: overall judgment and high-level principle fit,
strong, needs work, viability, open design, mechanical follow-through, and
readiness by topic. Do not substitute the commit audit trail for the design
assessment. For `copy`, report the assessment required by
`references/copy-review.md`: overall by reader, strong, needs work, fidelity
when reviewing an edit, judgment versus mechanical, and readiness per reader.

Do not average reviewer opinions. Model agreement is a reason to verify first,
not proof. One confirmed defect from the last reviewer requires the same response
discipline as one from the first.

## How It Fits

```
/multi-adversarial-review   → the review layer: stable commit, independent
                               reviewer, disposition, commit, next reviewer

/notes                       → the durable ledger a disposition commit rides on
                               (NOTES.md or a project review log)

/stable-label                → IDs for findings and decisions so a disposition
                               is greppable from the commit that answered it

/fast-chat                   → the maintainer's ruling on a contested finding,
                               as lettered options rather than prose

/red-pen                     → the `copy` target's vocabulary: its symptom list,
                               reader roster, and writing conventions are what
                               a copy reviewer reads and cites
```

/multi-adversarial-review is the gate the other skills feed. /notes gives it somewhere durable to record each disposition, /stable-label makes every finding and ruling addressable, and /fast-chat keeps the maintainer's rulings fast. Without it, a review is one model's opinion of its own work; with it, every stage inspects a committed state and leaves an auditable trail.
