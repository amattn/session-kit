# session-kit

A suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time.

Extracted from patterns discovered during 500+ sessions of AI-assisted development. Each skill addresses a specific friction point that compounds over time — lost context, slow decision-making, garbled input, fragile cross-references.

## Skills

| Skill | What it does |
|-------|-------------|
| `/warmup` | Session bootstrap and compaction recovery. Ensures skills, disciplines, and key files load reliably and survive context compaction. |
| `/fast-chat` | Structured interaction patterns. Numbered questions, lettered options, batch answer codes (`1A, 2B, 3 let's discuss pros/cons`), and a review prompt with R/O stable tail. Always-on communication style that makes decisions faster. |
| `/dictation` | Project-specific correction table. Originally designed for voice-to-text errors, but also useful for recurring typos and emergent shorthand — any systematic input pattern where the user means something other than what they literally typed. |
| `/notes` | Institutional memory. Captures decisions, rationale, and conventions in NOTES.md so future sessions don't re-litigate settled questions. |
| `/stable-label` | Greppable stable references. Gives every referenceable thing an append-only ID (`REQ_3`, `DEC_14`) that never renumbers and always resolves to exactly one definition. |
| `/feedback-foo` | Process improvement — pattern detection, observation tracking, and discipline creation. FOO = Feedback, Observation, Oversight. Proactively notices recurring patterns, tracks process observations with a resolution lifecycle, and helps formalize workflows as named disciplines. (Also invocable as `/foo`, `/feedback`, or `/observation`. Renamed from `/sharpen`.) |

## Install

### Option 1: Claude Code Marketplace

```bash
/plugin marketplace add amattn/session-kit
```

```bash
/plugin install session-kit@session-kit-marketplace
```

### Option 2: Global Installation

Copy the skills into your Claude Code skills directory so they're available across all projects:

```bash
cp -r skills/* ~/.claude/skills/
```

### Option 3: Project-Level Installation

Copy the skills into your project for per-project use:

```bash
mkdir -p .claude/skills
cp -r /path/to/session-kit/skills/* .claude/skills/
```

## The Skills

### `/warmup` — Session Bootstrap & Compaction Recovery

AI agents don't reliably read project files at session start, and context compaction mid-session can silently drop critical instructions. `/warmup` is the reliability layer — it uses every available tactic (auto-memory, Required Reading sections, discipline blocks, loading canaries) to ensure that what matters gets loaded and stays loaded.

Why it matters: every other skill in session-kit depends on the agent actually reading and following project directives. `/warmup` is what makes that reliable instead of aspirational.

What it adds over baseline Claude: the baseline can set up individual pieces (compaction recovery, required reading) but doesn't build the complete layered system — Required Reading + canaries + post-compaction rule + breadcrumbs + auto-memory guidance + cross-platform AGENTS.md — as integrated infrastructure. The skill also provides a systematic diagnostic checklist and escalation ladder for when rules aren't being followed reliably.

Best for: long sessions that hit context limits, projects with CLAUDE.md directives that get ignored, any project where you've said "it keeps forgetting to do X."

### `/fast-chat` — Structured Interaction Patterns

Replaces prose-heavy back-and-forth with structured codes. Numbered questions with lettered options, batch answer codes (`1A, 2B, 3ok`), and a standard review prompt with an R/O stable tail (R — show me recommendations, O — ok, approve). Silence is not approval — the review stays open until you say O. This is an always-on communication style, not just a tool you invoke.

Why it matters: every decision point in AI-assisted work is a potential bottleneck. Open-ended questions ("what do you think?") force the user to do generative work. Structured options let them do evaluative work — picking from a list instead of inventing from scratch. The speed gain compounds across hundreds of decisions per session and hundreds of sessions per project.

What it adds over baseline Claude: behavioral activation. Claude already *knows* these interaction patterns, but doesn't consistently *use* them — even when conventions are written in CLAUDE.md. The skill provides the activation energy to apply structured options to every decision point, use the review prompt for approvals, and avoid open-ended questions. The patterns themselves aren't novel; the consistent application is.

Best for: decision-heavy sessions, review workflows, voice-input users, anyone tired of typing paragraphs when a single code would do.

### `/dictation` — Correction Table

Maintains a project-specific table for voice-to-text errors, recurring typos, and emergent shorthand. Originally designed for dictation (voice engines predictably mangle project jargon), but the table is useful for any systematic input pattern where the user means something other than what they literally typed.

Why it matters: each uncorrected error costs a correction cycle — the user says it, the agent misunderstands, the user corrects, the agent apologizes. A correction table eliminates this for known patterns, and a learning loop captures new ones as they appear.

What it adds over baseline Claude: the setup puts the correction table in CLAUDE.md (loaded every session) rather than an ad-hoc file. When input is garbled beyond the table, the skill presents structured disambiguation options instead of guessing. And the "What Does NOT Go" boundaries prevent table bloat — one-off typos and standard abbreviations (k8s, img) stay out.

Best for: voice-input users, projects with unusual jargon or internal tool names, anyone who finds themselves repeatedly correcting the same misinterpretation.

### `/notes` — Institutional Memory

The most common failure mode in multi-session AI work: decisions get re-litigated because nobody remembers why they were made. `/notes` maintains a living `NOTES.md` that captures decisions, rationale, rejected alternatives, and conventions. Every session starts with an accurate picture of what's been decided and why.

Why it matters: without institutional memory, session 12 reopens questions that session 3 settled. The rationale is gone, so the same arguments play out again. `/notes` makes this nearly impossible — the reasoning is written down, in the user's own words, before the conversation moves on.

What it adds over baseline Claude: the CLAUDE.md discipline block is the killer feature — it makes note-taking behavior persist across sessions, not just the current one. The skill also enforces consistent structure (same sections every project) and preserves user quotes verbatim where baseline Claude tends to paraphrase.

Best for: multi-session projects, design-heavy work with many decisions, teams where context is lost between sessions or handoffs.

### `/stable-label` — Greppable Stable References

Gives every referenceable thing an append-only ID using the `XXX_N` convention (`REQ_3`, `DEC_14`). IDs never renumber, never get reused, and always resolve to exactly one definition. `grep REQ_3` returns the definition and every reference across the entire project.

Why it matters: without stable IDs, cross-references are fragile text that breaks when things get renamed. With them, any ID is a permanent, greppable anchor — in docs, in code comments, in docstrings, anywhere text lives. Both humans and agents can trace a requirement from spec to implementation in seconds.

What it adds over baseline Claude: convention enforcement is the biggest win — without the skill, Claude invents ad-hoc formats (kebab-case, dashes, zero-padding) that vary per session. The skill ensures consistent `XXX_N` format every time. Lifecycle operations are the second major differentiator: splits get provenance notes, merges keep tombstone redirects so every ID stays greppable, promotions get bidirectional cross-references, and crosscutting concerns get domain-specific faceted IDs instead of just prose. The baseline handles simple operations fine but loses ID traceability during lifecycle changes.

Best for: spec-driven projects, requirements tracking, any project with cross-referenced documents where you need to trace a decision from origin to implementation.

### `/feedback-foo` — Process Improvement

FOO = Feedback, Observation, Oversight — a bucket concept for items observed in the wild that need triage or action. Combines pattern detection, observation tracking, and discipline creation into one place. Proactively notices recurring patterns ("I've seen this twice, should we write it down?"), tracks process observations with a resolution lifecycle (open → resolved), and helps formalize important workflows as named disciplines. Also invocable as `/foo`, `/feedback`, or `/observation`. (Renamed from `/sharpen` — the old name was too conceptual; the natural inclination is to say "add an observation" or "add a feedback item.")

Why it matters: process improvements come from two directions — the agent notices patterns, and the user reports friction. Both need somewhere to go. Without `/foo`, observations get lost in conversation and patterns go unnoticed. With it, informal habits become named disciplines, friction becomes tracked observations, and the process improves over time.

What it adds over baseline Claude: when told about a recurring failure, baseline Claude apologizes and fixes the immediate problem. The skill treats it as a process improvement opportunity — creates a tracked observation, strengthens the relevant discipline, and flags escalation to tooling if prose keeps failing. The methodology (routing, discipline creation, prose→tooling escalation) is confirmed by evals. The proactive detection — the always-on capability where the agent notices patterns without being told — is the highest-value feature and requires real-world usage to fully validate.

Best for: long-running projects with evolving workflows, teams noticing the same friction repeatedly, anyone who wants the agent to get better at working with them over time.

## How to Use

Each skill has a one-time **setup** (first invocation creates project files) and an **ongoing** usage pattern.

### `/warmup`

**Setup:** Run `/warmup` in your project. It audits your CLAUDE.md (or creates one), then sets up Required Reading, a post-compaction rule, loading canaries, and auto-memory entries. All managed sections are marked with `<!-- managed by /warmup -->` breadcrumbs.

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
Agent: 1. Add a note about edge cases
       2. Keep the current examples

You: do 1, O
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

### `/notes`

**Setup:** Run `/notes` on a project without NOTES.md. It creates NOTES.md with suggested sections (Project Context, Invariants, Important Concepts, Taxonomy, Key Design Decisions, Open Questions), references it from CLAUDE.md, and adds a Notes Discipline block that enforces note-taking in every future session.

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

### `/stable-label`

**Setup:** Run `/stable-label` in your project. It scans existing artifacts, proposes a prefix table (e.g., `DEC` for decisions, `REQ` for requirements), adds convention rules to CLAUDE.md, and writes the prefix table to NOTES.md under Taxonomy / Conventions.

**Ongoing:** IDs are assigned automatically when you create or commit to something — a new requirement, a design decision, a feature. The agent won't assign IDs to exploratory output (brainstorms, summaries, option lists). Invoke `/stable-label` when you want to:
- Add a new prefix to the table
- Run a consistency pass (Quick for a single ID, Standard for a batch, Sweep for a whole prefix)
- Manage ID lifecycle — splitting, merging, deprecating, or promoting items

**Example:**
```
You: add a new requirement: API responses must be under 200ms
Agent: Added to the requirements spec:
       REQ_7 — API responses must complete within 200ms (p95)

You: let's go with Redis caching to meet that
Agent: (adds to NOTES.md)

       ### Caching strategy: Redis (2026-03-14)
       DEC_12 — Use Redis for response caching to meet REQ_7.
       - Rejected: CDN-only — doesn't help for authenticated endpoints

You: ok now implement the caching middleware
Agent: (writes code with traceability)

       # Cache middleware for API responses
       # Implements DEC_12 (Redis caching) to satisfy REQ_7 (200ms p95)
       class ResponseCache:
           ...

You: (later) grep REQ_7
       spec.md:         REQ_7 — API responses must complete within 200ms
       NOTES.md:        DEC_12 — Redis caching to meet REQ_7
       middleware.py:   # Implements DEC_12 to satisfy REQ_7
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
/warmup          → ensures everything loads reliably
                    (the foundation — without it, nothing else is guaranteed)

/fast-chat       → makes every interaction faster
                    (structured codes replace prose)

/dictation       → removes input friction
                    (correction table for voice, typos, shorthand)

/notes           → captures what was decided and why
                    (institutional memory across sessions)

/stable-label    → makes cross-references greppable and permanent
                    (machine-verifiable navigation)

/feedback-foo    → detects patterns, tracks observations, creates disciplines
                    (FOO = Feedback, Observation, Oversight)
```

The skills are independent — install any subset. But they're designed to complement each other: `/warmup` ensures `/notes` loads every session, `/stable-label` gives `/notes` entries greppable IDs, `/fast-chat` speeds up the decisions `/notes` captures, `/dictation` keeps voice input from garbling the whole conversation, and `/feedback-foo` turns recurring friction into tracked observations and named disciplines.

## Origin

Developed and battle-tested during [plet-skills](https://github.com/amattn/plet-skills) development (8+ parts, hundreds of sessions). Extracted as a standalone suite for use in any Claude Code project.

`/fast-chat` was strongly inspired by [snarktank's Ralph skills](https://github.com/snarktank/ralph).

## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). You're free to use, share, and adapt these skills — including in commercial projects — as long as you provide attribution and share any adaptations under the same license. See [LICENSE](LICENSE) for the full text.
