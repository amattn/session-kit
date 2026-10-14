# session-kit

A suite of Claude Code and OpenCode skill plugins for making AI-assisted development sessions reliable and productive across time.

Extracted from patterns discovered during hundreds of sessions of AI-assisted development. Each skill addresses a specific friction point that compounds over time — lost context, slow decision-making, garbled input, unedited output, fragile cross-references. Works with both Claude Code and OpenCode.

## Skills

| Skill | What it does |
|-------|-------------|
| [`/start`](#start) | Unified bootstrap for the suite. One approval covers the plan, plus a quick multi-select for `.claude/settings.json` when that file is missing or marketplace-only. Tiers: `minimal` (/warmup), `standard` (default, adds /notes, /stable-label, /fast-chat, /red-pen), `full` (adds /dictation and /feedback-foo). Re-runnable — picks up only what's missing. |
| [`/stable-label`](#stable-label) | Greppable stable references. Gives every referenceable thing an append-only ID (`REQ_3`, `DEC_14`) that never renumbers and always resolves to exactly one definition. |
| [`/fast-chat`](#fast-chat) | Structured interaction patterns. Numbered questions, lettered options, batch answer codes (`1A, 2B, 3 let's discuss pros/cons`), and a review prompt that always ends with R (show recommendations) and O (approve). Always-on communication style that makes decisions faster. |
| [`/multi-adversarial-review`](#multi-adversarial-review) | Sequential multi-model review. A lead commits a stable state, independent reviewer models inspect it one at a time, and the lead dispositions every finding and commits before the next model reviews. Read-only reviewers, evidence-backed findings, an auditable trail. (Also invocable as `/mar`.) |
| [`/notes`](#notes) | Institutional memory. Captures decisions, rationale, and conventions in NOTES.md so future sessions don't re-litigate settled questions. |
| [`/red-pen`](#red-pen) | Writing directives. Makes AI-generated text less painful to read with explicit constraints: counted limits, a named reader, a mandatory cut pass. Separate rules for specs, code comments, code, and chat. |
| [`/warmup`](#warmup) | Session bootstrap and compaction recovery. Ensures skills, disciplines, and key files load reliably and survive context compaction. |
| [`/dictation`](#dictation) | Project-specific correction table. Originally designed for voice-to-text errors, but also useful for recurring typos and emergent shorthand — any systematic input pattern where the user means something other than what they literally typed. |
| [`/feedback-foo`](#feedback-foo) | Process improvement — pattern detection, observation tracking, and discipline creation. FOO = Feedback, Observation, Oversight. Proactively notices recurring patterns, tracks process observations with a resolution lifecycle, and helps formalize workflows as named disciplines. (Also invocable as `/foo`, `/feedback`, or `/observation`.) |

## Install

Installing activates nothing by itself. A skill sets itself up in a project the first time you invoke it there. `/multi-adversarial-review` also needs a second coding-agent command-line tool to act as the outside reviewer (see its entry under How to Use).

### Option 1: Claude Code Marketplace

```bash
/plugin marketplace add amattn/session-kit
```

```bash
/plugin install session-kit@session-kit-marketplace
```

### Option 2: Global Installation

Copy the skills into your Claude Code / OpenCode skills directory so they're available across all projects. The `*-workspace` directories hold eval artifacts and are skipped:

```bash
rsync -a --exclude='*-workspace' skills/ ~/.claude/skills/
```

### Option 3: Project-Level Installation

Copy the skills into your project for per-project use:

```bash
mkdir -p .claude/skills
```

```bash
rsync -a --exclude='*-workspace' /path/to/session-kit/skills/ .claude/skills/
```

### Option 4: OpenCode (project or global)

OpenCode discovers skills from six locations — any of these work:

| Location | Path |
|----------|------|
| Project config | `.opencode/skills/` |
| Global config | `~/.config/opencode/skills/` |
| Project Claude-compatible | `.claude/skills/` |
| Global Claude-compatible | `~/.claude/skills/` |
| Project agent-compatible | `.agents/skills/` |
| Global agent-compatible | `~/.agents/skills/` |

The `.claude/skills/` paths overlap with Claude Code — if you installed via Options 2 or 3, OpenCode already sees the skills.

For OpenCode-specific directories, install like this:

Global (all projects):

```bash
mkdir -p ~/.config/opencode/skills
```

```bash
rsync -a --exclude='*-workspace' /path/to/session-kit/skills/ ~/.config/opencode/skills/
```

Project-level:

```bash
mkdir -p .opencode/skills
```

```bash
rsync -a --exclude='*-workspace' /path/to/session-kit/skills/ .opencode/skills/
```

### Option 5: Agent-compatible directories (Codex)

The `.agents/skills/` directories are unique to OpenCode.

Global (all projects):

```bash
mkdir -p ~/.agents/skills
```

```bash
rsync -a --exclude='*-workspace' /path/to/session-kit/skills/ ~/.agents/skills/
```

Project-level:

```bash
mkdir -p .agents/skills
```

```bash
rsync -a --exclude='*-workspace' /path/to/session-kit/skills/ .agents/skills/
```

## The Skills

### `/start` — Unified Suite Bootstrap

The recommended on-ramp for new projects. Bootstraps the whole suite (or any tier you pick) in one pass instead of running each skill individually. Smart defaults plus a single bootstrap approval replace the 10+ questions across the per-skill setups. The one sub-prompt: `/warmup` surfaces a quick multi-select for `.claude/settings.json` when that file is missing or contains only the marketplace-installed `enabledPlugins` entry — settings changes are never automatic.

Why it matters: per-skill bootstraps are great for incremental adoption, but a fresh project benefits from coordinated setup. `/notes` pre-seeds the prefix table that `/stable-label` expects; `/warmup` adds NOTES.md to Required Reading; `/fast-chat`'s conventions land alongside the Notes Discipline. `/start` does that coordination automatically.

Tiers:
- `minimal` — just `/warmup`
- `standard` *(default)* — `/warmup` + `/notes` + `/stable-label` + `/fast-chat` + `/red-pen`
- `full` — all seven skills that have a setup step

`/multi-adversarial-review` has no setup step, so it is in no tier.

Re-runnable — picks up only what's missing; existing files are never overwritten.

Best for: new projects starting from scratch, existing projects missing one or more session-kit pieces, anyone who'd rather "just get me set up" than walk through per-skill bootstraps.

### `/stable-label` — Greppable Stable References

Gives every referenceable thing an append-only ID using the `XXX_N` convention (`REQ_3`, `DEC_14`). IDs never renumber, never get reused, and always resolve to exactly one definition. A project-wide search such as `grep -rn REQ_3 .` returns the definition and every reference.

Why it matters: without stable IDs, cross-references are fragile text that breaks when things get renamed. With them, any ID is a permanent, greppable anchor — in docs, in code comments, in docstrings, anywhere text lives. Both humans and agents can trace a requirement from spec to implementation in seconds.

What it adds over baseline Claude: convention enforcement is the biggest win — without the skill, Claude invents ad-hoc formats (kebab-case, dashes, zero-padding) that vary per session. The skill ensures consistent `XXX_N` format every time. Lifecycle operations are the second major differentiator: splits get provenance notes, merges keep tombstone redirects so every ID stays greppable, promotions get bidirectional cross-references, and crosscutting concerns get domain-specific faceted IDs instead of just prose. The baseline handles simple operations fine but loses ID traceability during lifecycle changes.

Best for: spec-driven projects, requirements tracking, any project with cross-referenced documents where you need to trace a decision from origin to implementation.

### `/fast-chat` — Structured Interaction Patterns

Replaces prose-heavy back-and-forth with structured codes. Numbered questions with lettered options, batch answer codes (`1A, 2B, 3ok`), and a standard review prompt with an R/O stable tail (R — show me recommendations, O — ok, approve). Silence is not approval — the review stays open until you say O. This is an always-on communication style, not just a tool you invoke.

Why it matters: every decision point in AI-assisted work is a potential bottleneck. Open-ended questions ("what do you think?") force the user to do generative work. Structured options let them do evaluative work — picking from a list instead of inventing from scratch. The speed gain compounds across hundreds of decisions per session and hundreds of sessions per project.

What it adds over baseline Claude: behavioral activation. Claude already *knows* these interaction patterns, but doesn't consistently *use* them — even when conventions are written in CLAUDE.md. The skill provides the activation energy to apply structured options to every decision point, use the review prompt for approvals, and avoid open-ended questions. The patterns themselves aren't novel; the consistent application is.

Best for: decision-heavy sessions, review workflows, voice-input users, anyone tired of typing paragraphs when a single code would do.

### `/multi-adversarial-review` — Sequential Multi-Model Review

A model reviewing its own work shares its own blind spots. `/multi-adversarial-review` breaks the author/reviewer monoculture: a lead commits a stable state, then reviewer models from different families inspect it one at a time. Reviewers are read-only and must back every finding with evidence. After each pass the lead verifies each finding against source, fixes it, defers it with a home, or rejects it with a reason, and commits that disposition before the next model reviews the new state. "No findings" is a valid outcome, but it must name the residual risk. Targets: code, plan, code-vs-plan, spec, and copy. Short name: `/mar`.

Why it matters: review as a one-shot opinion gets averaged or ignored. Review as a sequential gate with a committed disposition between stages produces an audit trail, lets each reviewer build on the last one's confirmed findings, and forces the author to answer every finding instead of the ones it likes.

What it adds over baseline Claude: the discipline, not the critique. Baseline Claude will review code when asked and often finds real issues. The skill adds the parts that make review trustworthy: cross-model reviewers routed out of the host, read-only capability modes with write audits, disposition states with evidence, the commit-between-stages rule, stall and route-failure handling, and a bounded panel for contested findings. The spec target adds an output contract (overall, strong, needs work, viability, open vs mechanical, readiness) that keeps design review from collapsing into prose.

Best for: implementation gates before merge, stress-testing a plan before building it, design-note and spec review against a project's principles, any project where the same model writes and reviews.

### `/notes` — Institutional Memory

A common failure mode in multi-session AI work: decisions get re-litigated because nobody remembers why they were made. `/notes` maintains a living `NOTES.md` that captures decisions, rationale, rejected alternatives, and conventions. Every session starts with an accurate picture of what's been decided and why.

Why it matters: without institutional memory, session 12 reopens questions that session 3 settled. The rationale is gone, so the same arguments play out again. `/notes` makes this much less likely — the reasoning is written down, in the user's own words, before the conversation moves on.

What it adds over baseline Claude: the CLAUDE.md discipline block is the killer feature — it makes note-taking behavior persist across sessions, not just the current one. The skill also enforces consistent structure (the same suggested sections in every project) and preserves user quotes verbatim where baseline Claude tends to paraphrase.

Best for: multi-session projects, design-heavy work with many decisions, teams where context is lost between sessions or handoffs.

### `/red-pen` — Writing Directives

AI-generated text is painful to read — not because it's wrong, but because it's unedited. A human writer pays for every sentence, and that cost filters out what isn't worth the reader's attention. Generated text pays nothing, so nothing filters it: uniform length, uniform pacing, headers that encode no priority, completeness instead of compression, no stance, session narration. `/red-pen` is the editor. It substitutes explicit constraints for the missing cost — counted limits, a named reader, mandatory prioritization, a required cut pass — with separate rules for the four places the damage differs: specs and plans, code comments, code and diffs, chat. The goal is clarity; shorter text is a side effect.

Why it matters: a bloated spec wastes a decision-maker's attention. A narrating comment misleads a debugger years later. An over-defensive diff burdens a reviewer. A padded chat reply slows a conversation. Each is cheap to produce and expensive to read, and the cost lands on the human every time.

What it adds over baseline Claude: the rules are not novel — Claude knows "answer first" and "don't restate the code." The skill makes them the default instead of something the user has to ask for each time, and it adds the pieces baseline skips: deciding the output type before writing, a 300-word spec tripwire, the `chose A over B because C; revisit if D` decision shape, and a cut pass against a checklist of the recognizable symptoms. `/red-pen <target>` also turns the rules into an editing pass you can point at any file.

Best for: anyone who reads more AI output than they write, spec-heavy projects where a human ratifies decisions, codebases that have started accumulating narrating comments and defensive noise.

### `/warmup` — Session Bootstrap & Compaction Recovery

AI agents don't reliably read project files at session start, and context compaction mid-session can silently drop critical instructions. `/warmup` is the reliability layer — it uses every available tactic (auto-memory, Required Reading sections, discipline blocks, loading canaries) to ensure that what matters gets loaded and stays loaded.

Why it matters: every other skill in session-kit depends on the agent actually reading and following project directives. `/warmup` is what makes that reliable instead of aspirational.

What it adds over baseline Claude: the baseline can set up individual pieces (compaction recovery, required reading) but doesn't build the complete layered system — Required Reading + canaries + post-compaction rule + breadcrumbs + auto-memory guidance + cross-platform AGENTS.md — as integrated infrastructure. The skill also provides a systematic diagnostic checklist and escalation ladder for when rules aren't being followed reliably.

Best for: long sessions that hit context limits, projects with CLAUDE.md directives that get ignored, any project where you've said "it keeps forgetting to do X."

### `/dictation` — Correction Table

Maintains a project-specific table for voice-to-text errors, recurring typos, and emergent shorthand. Originally designed for dictation (voice engines predictably mangle project jargon), but the table is useful for any systematic input pattern where the user means something other than what they literally typed.

Why it matters: each uncorrected error costs a correction cycle — the user says it, the agent misunderstands, the user corrects, the agent apologizes. A correction table eliminates this for known patterns, and a learning loop captures new ones as they appear.

What it adds over baseline Claude: the setup puts the correction table in CLAUDE.md (loaded every session) rather than an ad-hoc file. When input is garbled beyond the table, the skill presents structured disambiguation options instead of guessing. And the "What Does NOT Go" boundaries prevent table bloat — one-off typos and standard abbreviations (k8s, img) stay out.

Best for: voice-input users, projects with unusual jargon or internal tool names, anyone who finds themselves repeatedly correcting the same misinterpretation.

### `/feedback-foo` — Process Improvement

FOO = Feedback, Observation, Oversight — a bucket concept for items observed in the wild that need triage or action. Combines pattern detection, observation tracking, and discipline creation into one place. Proactively notices recurring patterns ("I've seen this twice, should we write it down?"), tracks process observations with a resolution lifecycle (open → resolved), and helps formalize important workflows as named disciplines. Also invocable as `/foo`, `/feedback`, or `/observation`. (Renamed from `/sharpen` — the old name was too conceptual; the natural inclination is to say "add an observation" or "add a feedback item.")

Why it matters: process improvements come from two directions — the agent notices patterns, and the user reports friction. Both need somewhere to go. Without `/foo`, observations get lost in conversation and patterns go unnoticed. With it, informal habits become named disciplines, friction becomes tracked observations, and the process improves over time.

What it adds over baseline Claude: when told about a recurring failure, baseline Claude apologizes and fixes the immediate problem. The skill treats it as a process improvement opportunity — creates a tracked observation, strengthens the relevant discipline, and flags escalation to tooling if prose keeps failing. The methodology (routing, discipline creation, prose→tooling escalation) is confirmed by evals. The proactive detection — the always-on capability where the agent notices patterns without being told — is the highest-value feature and requires real-world usage to fully validate.

Best for: long-running projects with evolving workflows, teams noticing the same friction repeatedly, anyone who wants the agent to get better at working with them over time.

## How to Use

Most skills have a one-time **setup** (the first invocation creates project files) and an **ongoing** usage pattern. `/multi-adversarial-review` has no setup step.

For new projects, run `/start` first to bootstrap everything at once. The per-skill setups below are still available — `/start` just runs them for you with smart defaults.

### `/start`

**Setup:** Run `/start` (default standard tier), or `/start minimal` / `/start full` to pick a tier. It detects what's already in place, proposes a plan, and bootstraps the per-skill artifacts in one pass. You approve the plan once (plus a quick multi-select for `.claude/settings.json` if that file is missing or marketplace-only) instead of the 10+ separate questions you'd get from the per-skill bootstraps. Existing files are never overwritten — re-running picks up only what's missing.

**Ongoing:** Rarely. The skill is bootstrap-oriented — once the suite is in place, the per-skill commands take over. Invoke it again when you want to:
- Add a tier you skipped (run with a different tier flag)
- Set up session-kit on another project quickly

**Example:**
```
You: /start
Agent: About to bootstrap session-kit (standard tier) for `my-project`:

       Files to create:
       - AGENTS.md     (Required Reading, Post-Compaction Rule, Session Start
                        canary, NOTES.md Discipline, Stable Label Convention,
                        /fast-chat Interaction Conventions, /red-pen Writing
                        Conventions)
       - CLAUDE.md     (pointer to AGENTS.md)
       - NOTES.md      (from /notes template, with default prefix table
                        pre-seeded: DEC, ICR, INS, OPN, MON, TAX, FOO)
       - .gitignore    (.DS_Store) — only if missing
       - .claude/settings.json — sub-prompt for additions when missing,
                        empty, or marketplace-only; otherwise skipped

       Auto-memory entries:
       - project-my-project.md
       - warmup-session-canary.md

       A. Approve — write everything as planned
       B. Switch tier (minimal | full)
       C. Customize interactively — walk through each sub-skill's bootstrap

       R. Show me recommendations
       O. Ok, approve

You: O
Agent: .claude/settings.json is missing. Propose adding:

       A. permissions.allow — read-file Bash + read-only git + grep
       B. includeCoAuthoredBy: false
       C. env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: "1"
       D. enabledPlugins: session-kit@session-kit-marketplace

       Pick any combination (e.g., "A,B,C", "all", "none").
       R. Show me recommendations
       O. Ok, all

You: O
Agent: Bootstrapped. Loaded: AGENTS.md, NOTES.md. Git: working tree clean. Ready.
       /multi-adversarial-review needs no setup; it is ready once a second
       reviewer tool (Codex, Pi, cn, or OpenCode) is installed.
```

### `/stable-label`

**Setup:** Run `/stable-label` in your project. It branches on what's already there:
- **Branch A** — if `/notes` was already bootstrapped (the common case under `/start`), it detects the pre-seeded prefix table in NOTES.md and just adds the convention rules to CLAUDE.md, then offers to customize the seeded prefixes.
- **Branch B** — if no prefix table exists, it scans existing artifacts, proposes a prefix table (e.g., `DEC` for decisions, `REQ` for requirements), adds convention rules to CLAUDE.md, and writes the table to NOTES.md under Taxonomy / Conventions.

**Ongoing:** IDs are assigned automatically when you create or commit to something — a new requirement, a design decision, a feature. The agent won't assign IDs to exploratory output (brainstorms, summaries, option lists). Invoke `/stable-label` when you want to:
- Add a new prefix to the table
- Run a consistency pass (Quick for a single ID, Standard for a batch, Sweep for a whole prefix)
- Manage ID lifecycle — splitting, merging, deprecating, or promoting items

**Example:**
```
You: add a new requirement: API responses must be under 200ms
Agent: Added to the requirements spec:
       REQ_7 — API responses must complete in under 200ms

You: let's go with Redis caching to meet that
Agent: (adds to NOTES.md)

       ### Caching strategy: Redis (2026-03-14)
       DEC_12 — Use Redis for response caching to meet REQ_7.
       - Rejected: CDN-only — doesn't help for authenticated endpoints

You: ok now implement the caching middleware
Agent: (writes code with traceability)

       # Cache middleware for API responses
       # Implements DEC_12 (Redis caching) to satisfy REQ_7 (under 200ms)
       class ResponseCache:
           ...

You: (later) grep REQ_7
       spec.md:         REQ_7 — API responses must complete in under 200ms
       NOTES.md:        DEC_12 — Redis caching to meet REQ_7
       middleware.py:   # Implements DEC_12 to satisfy REQ_7
```

### `/fast-chat`

**Setup:** Run `/fast-chat` in your project. It adds an Interaction Conventions section to CLAUDE.md with the NL/NLR/1b1 shorthands, batch answer format, and the standard review prompt.

**Ongoing:** Always-on — no invocation needed. The agent presents choices as numbered questions with lettered options and uses the review prompt (R/O tail) for approvals. Your side:
- Answer with batch codes: `1A, 2B, 3ok`
- Say `NL` to reformat a question as numbered-letters options
- Say `NLR` for options with the agent's recommendation marked
- Say `1b1` to discuss items one at a time instead of batching
- Say `R` during a review to get NL-formatted recommendations
- Say `O` to approve — implicitly accepts any simple displayed rec
- Just type instructions (add/change/remove) — no prefix needed
- Unanswered items stay open — silence is never treated as approval

**Example — review flow:**
```
Agent: [presents section for review]

   R. Show me recommendations
   O. Ok, approve

You: fix the typo in paragraph 2
Agent: [fixes typo, re-presents section]

   R. Show me recommendations
   O. Ok, approve

You: R
Agent: 1. Edge case handling
          A. Add a note about edge cases
          B. Skip for now
       2. Examples section
          A. Expand with more examples
          B. Keep as-is

You: 1A, 2B, O
```

**Example — batch decisions:**
```
Agent: A few decisions needed:
       1. Database engine?
          A. SQLite
          B. PostgreSQL ← recommended
          C. Other
       2. Auth strategy?
          A. JWT
          B. Session cookies
          C. Other
       3. Rate limiting?
          A. Per-user token bucket
          B. Global sliding window
          C. Skip for now
       4. Logging format?
          A. Structured JSON
          B. Plain text
          C. Other

You: 1A, 2B, 3 do you have any recommendations, 4 defer till later
Agent: For 3, I'd recommend A (per-user token bucket) — it prevents
       noisy-neighbor problems without penalizing well-behaved users.
       Noted 4 as still open. Applied 1A and 2B.
```

### `/multi-adversarial-review`

**Setup:** Nothing to bootstrap. You need at least one reviewer route that is not the host model: `codex exec` for Codex, Pi, Continue's `cn`, or OpenCode (three coding-agent command-line tools; any one will do) for GLM or another non-family model. The launch recipes are in [`references/routes.md`](skills/multi-adversarial-review/references/routes.md). If your project defines its own review cadence in AGENTS.md or an iteration spec, that wins.

**Ongoing:** Invoke it when work is committed and ready for a gate:
- `/mar` runs the default chain with the available non-host models, strongest finder last
- `/mar with Claude, Codex, and GLM 5.3` uses the order you name
- `/mar to review HEAD against <base>` points reviewers at a range
- `/mar review <note> as a spec` runs the spec target with its output contract
- `/mar review <doc> as copy for <readers>` reviews a document as writing, with its named readers as the lenses

Each stage: the reviewer reads a stable commit, the lead (your agent, with you ruling on anything contested) dispositions every finding (`accepted-fixed`, `accepted-deferred`, `rejected` with evidence, `unclear-blocked`, `no-findings` with residual risk, `route-failed`, `contested`) and commits, and the next reviewer reads the new commit.

**Example:**
```
You: /mar to review HEAD against main
Agent: Baseline 3f2a1c9 is stable. Launching GLM through Pi in a disposable
       worktree, no writes to the primary checkout.
       GLM: 3 findings. Verified against source:
       - F1 retry loop swallows TransportError — accepted-fixed, test added
       - F2 "unused import" — rejected, used in the type annotation
       - F3 backoff cap unbounded — accepted-deferred, tracked as RSK_4
       Committed 8b77e02. Launching Codex against 8b77e02 ...

       Review chain
       - 3f2a1c9: stable baseline
       - 8b77e02: after GLM disposition - 1 fixed, 1 rejected, 1 deferred
       - c41d9aa: after Codex disposition - no findings; residual risk: RSK_4
```

### `/notes`

**Setup:** Run `/notes` on a project without NOTES.md. It copies the canonical NOTES.md template — suggested sections (Project Context, Invariants, Important Concepts, Taxonomy, Key Design Decisions, Open Questions, Things to Monitor), Quick Reference front-matter, and a default stable-label prefix table pre-seeded under § Taxonomy / Conventions — then references it from CLAUDE.md and adds a Notes Discipline block that enforces note-taking in every future session.

**Ongoing:** Mostly automatic — the discipline block tells the agent to update NOTES.md after every decision before moving on. You don't need to invoke `/notes` for routine note-taking. Invoke it when you want to:
- Reorganize sections that have grown unwieldy
- Set up routing for multiple NOTES.md files (e.g., `guide/NOTES.md` for a subfolder with its own decision history)
- Set up a new project

**Example:**
```
You: let's go with PostgreSQL for the event store
Agent: (updates NOTES.md immediately)

       ### Database choice: PostgreSQL for event store (2026-03-14)
       User: "let's go with PostgreSQL for the event store"
       Chosen for durability guarantees and JSONB support.
       - Rejected: SQLite — insufficient for concurrent writes
       - Rejected: DynamoDB — team has no AWS experience

You: oh and we should never delete events, only soft-delete
Agent: (adds to Invariants & Critical Requirements)

       **Events are append-only — never hard-delete.**
       Soft-delete via a `deleted_at` timestamp. This is load-bearing
       for audit compliance and event replay.

You: I keep saying this but — names should be verbs for actions, nouns for systems
Agent: (adds to Important Concepts & Insights, under "From the user")

       User: "names should be verbs for actions, nouns for systems"
```

### `/red-pen`

**Setup:** Run `/red-pen` in your project. It adds a Writing Conventions section to CLAUDE.md: the shared core (know the reader, omit what they know, pace by uncertainty, checkable over fluent) a one-line rule of thumb per output type — spec/plan, code comment, code/diff/commit, chat — and a reader roster (who reads this project's output, what they know, what they decide, where they stop reading).

**Ongoing:** Always-on — no invocation needed. Before writing anything, the agent decides which output type it is producing, writes to that type's rules, and runs a cut pass before delivering. Your side:
- Say `red-pen this` or `/red-pen <file>` to edit a file or section against the rules — the file is edited and you get a short report: what was found, one before/after paragraph, and a small symptom table
- Say `too long` or `too wordy` — the agent re-runs the cut pass on its last output and resends, no explanation
- Sentences stay short (about 20 words in numbered steps, 25 elsewhere), active, and consistent in their terms, borrowed from Simplified Technical English at about 80% strength; every cut is checked for lost facts
- Ask for a plan, spec, or design note — it opens with a preamble saying who it's for and how to read it, then what it needs from you, not an overview
- Override a default for the project (a higher spec tripwire, a different reader) — it's recorded in the Writing Conventions block, and so is any cut you reject, so the next pass starts calibrated
- The report after an edit is by symptom, not word count: `scripts/symptoms.py --compare before.md after.md` counts restated phrases, "This is / That is" openers, bold leads, dated markers, header density, sentence and paragraph length, passive voice, and likely term switches

**Example — editing a target:**
```
You: /red-pen docs/caching-design.md
Agent: Wrote docs/caching-design.md. Every rule and anchor is preserved.
       One stale claim found: the doc calls the cache backend undecided,
       and NOTES.md settled it.

       Here is one paragraph before and after, as an example of the change:
       [the before paragraph]
       [the after paragraph]

       | Symptom                          | Before  | After |
       | The same rule stated             | 4 times | once  |
       | Overview and Next Steps sections | 2       | 0     |
```

**Example — always-on, a plan request:**
```
You: write up a plan for the rate limiter
Agent: This plan is for you as the one approving the limiter design;
       it assumes the context in issue #41.

       One decision is yours: per-user token bucket or global sliding
       window. I lean per-user, because the noisy-neighbor complaint is
       why this exists; revisit if we add tenant-level quotas.

       Assumptions:
       - [ ] Redis is already in the deploy (it is, per docker-compose)
       - [ ] 429 with Retry-After is acceptable to the mobile client

       Risks:
       - Bucket state could drift if Redis fails over mid-refill.

       Scope out: no admin UI for limits, no per-endpoint overrides.
```

### `/warmup`

**Setup:** Run `/warmup` in your project. It audits your CLAUDE.md (or creates one), then sets up Required Reading, a post-compaction rule, loading canaries, and auto-memory entries. It also bootstraps `.gitignore` (with `.DS_Store`) and `.claude/settings.json` (with a low-friction permissions allowlist, privacy defaults, and session-kit plugin enablement) — only when those files don't already exist. All managed sections in CLAUDE.md/AGENTS.md are marked with `<!-- managed by /warmup -->` breadcrumbs.

**Ongoing:** You rarely invoke `/warmup` directly after setup. Its infrastructure works in the background — canaries verify files loaded, the post-compaction rule triggers re-reads after context compression. Invoke it again when:
- A rule or file isn't loading reliably (it walks an escalation ladder: tighten wording → improve positioning → add redundancy → promote to auto-memory)
- You want to add a new file to the Required Reading chain
- You suspect compaction dropped something mid-session

**Example:**
```
You: /warmup
Agent: I've audited your CLAUDE.md. Here's what I set up:
       - Required Reading: NOTES.md, PLAN.md
       - Post-Compaction Rule: re-read Required Reading after compaction
       - Session Start Canary: report git status before doing other work
       - Auto-memory entry: "always read NOTES.md"

You: (later) It keeps forgetting to read NOTES.md
Agent: The Required Reading rule is present and auto-memory is set,
       but the rule is positioned at the bottom of CLAUDE.md where
       compaction is likely dropping it. I'll move it to the top
       and strengthen the wording. I'll also add a cross-file
       reinforcement pointer at the top of NOTES.md pointing back
       to CLAUDE.md.
```

### `/dictation`

**Setup:** Run `/dictation` in your project. It scans project jargon, proposes a correction table (focused on terms voice engines are likely to mangle), and writes the table to CLAUDE.md with a `<!-- managed by /dictation -->` breadcrumb.

**Ongoing:** Always-on — known corrections are applied silently. When input is garbled beyond the table, the agent presents disambiguation options instead of guessing. Your side:
- When the agent misinterprets a recurring term, say something like "add 'pleat' means 'plet' to the correction table" — or just correct it and the agent will offer to add it
- One-off typos don't need table entries; the table is for systematic, recurring patterns

**Example:**
```
You: push the jason config to the Maine branch and update the cloud API key
Agent: (silently corrects to "JSON config", "main branch", and "Claude API key",
        proceeds with the task)

You: we need to fix the pleet workflow
Agent: I'm not sure what "pleet" refers to. Did you mean:
       A. plet (the dev orchestrator)
       B. fleet (deployment fleet)
       C. Something else

You: A
Agent: Got it. Want me to add "pleet → plet" to the correction table?
```

### `/feedback-foo`

**Setup:** Run `/feedback-foo` (or `/foo`, `/feedback`, `/observation`) in your project. It creates FEEDBACK_FOO.md (a tracker for process observations with open/resolved lifecycle) and adds a Self-Improvement directive to CLAUDE.md telling the agent to notice and surface patterns proactively.

**Ongoing:** Always-on detection — the agent notices recurring patterns, drift, and friction without being asked. When it detects something, it surfaces a lightweight proposal ("I've noticed X twice — want me to note it in NOTES.md or promote it to a CLAUDE.md discipline?"). Invoke `/feedback-foo` when you want to:
- Review open observations in FEEDBACK_FOO.md
- Promote a confirmed pattern to a CLAUDE.md discipline
- Create a named discipline block for a workflow you want enforced

**Example:**
```
Agent: I've noticed you always ask me to check for stale imports
       after moving files — that's the third time this session.
       Want me to track this in NOTES.md, or is it confirmed
       enough for a CLAUDE.md discipline?

You: discipline

Agent: Added to CLAUDE.md:
       ## Post-Move Discipline
       **After moving any file, grep for stale imports and update them.**
       Created FOO_3 in FEEDBACK_FOO.md → [resolved] promoted to discipline.

You: (later, during a code review discussion)
     that's a great insight — every time we add a new API route we
     forget to update the OpenAPI spec. add a foo for that

Agent: Added FOO_4 to FEEDBACK_FOO.md:
       ### FOO_4: OpenAPI spec falls behind when adding routes [drift]
       Observed during code review. Routes added without updating
       the OpenAPI spec. Not yet a discipline — monitoring frequency.
```

## How They Fit Together

```
/start → bootstraps the whole suite (or any tier) in one pass
                      (the on-ramp — use this for a new project)

/stable-label     → makes cross-references greppable and permanent
                     (machine-verifiable navigation)

/fast-chat        → makes every interaction faster
                     (structured codes replace prose)

/multi-adversarial-review
                  → gates committed work behind independent reviewers
                     (stable commit, disposition, commit, next model)

/notes            → captures what was decided and why
                     (institutional memory across sessions)

/red-pen          → makes every output cheaper to read
                     (mode-specific rules and a cut pass)

/warmup           → ensures everything loads reliably
                     (the foundation the others rely on)

/dictation        → removes input friction
                     (correction table for voice, typos, shorthand)

/feedback-foo     → detects patterns, tracks observations, creates disciplines
                     (FOO = Feedback, Observation, Oversight)
```

The skills are independent — install any subset, or use `/start` to bootstrap a coordinated set in one pass. The order above runs from most used to least. They are designed to complement each other: `/stable-label` gives `/notes` entries greppable IDs, `/fast-chat` speeds up the decisions `/notes` captures, `/multi-adversarial-review` puts committed work in front of a model that did not write it (prose included, using `/red-pen`'s vocabulary), `/red-pen` keeps the prose that remains worth reading, `/warmup` makes sure `/notes` and the rest load every session, `/dictation` keeps voice input from garbling the whole conversation, and `/feedback-foo` turns recurring friction into tracked observations and named disciplines.

## Origin

Developed and refined over hundreds of AI-assisted development sessions, then extracted as a standalone suite for use in any Claude Code project.

`/fast-chat` was strongly inspired by [snarktank's Ralph skills](https://github.com/snarktank/ralph).

`/multi-adversarial-review` was developed in [vog_kit](https://github.com/amattn/vog_kit) while building the Vog language and is now maintained here; vog_kit carries the Codex-host variant and the prior-art survey it was built from.

`/red-pen`'s sentence-level rules borrow from ASD-STE100 Simplified Technical English at about 80% strength, a framing from Kruno Golubić's [ASD-STE100: What It Is and What It Has to Do with LLMs](https://kgolubic.com/posts/asd-ste100-and-llms/) and the Andrej Karpathy post it discusses.

`/red-pen` was inspired by Ayman Nadeem's [Plan Mode Is Dead](https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html).

## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). You're free to use, share, and adapt these skills — including in commercial projects — as long as you provide attribution and share any adaptations under the same license. See [LICENSE](LICENSE) for the full text.
