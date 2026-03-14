# NOTES.md — session-kit

## Project Context

session-kit is a suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time. Extracted from patterns discovered during hundreds of sessions of plet-skills development. 6 skills total: `/notes`, `/warmup`, `/stable-label`, `/fast-chat`, `/dictation`, `/sharpen`.

**Origin:** Extracted from patterns discovered during plet-skills development (`../plet-skills/`).

---

## Key Design Decisions

### Suite scope and skill roster (2026-03-13)

Originally planned 7 extractable skills plus `/notes` (8 total). After merging /patterns into /sharpen and folding /discipline into /warmup + /sharpen, final count is 6 skills.

### Skill naming philosophy: nouns for systems, verbs for actions (2026-03-13)

Most skills in this suite are noun-shaped — they manage a system or artifact, not perform a one-shot action. `/notes` means "engage the notes system," not "take a note." Verb-form names (like `/mark`) undersell system-oriented skills by implying a one-shot action.

### Suite name: session-kit (2026-03-13)

Kept the original name. The suite name doesn't need to carry the value prop — the individual skill names already do that (`/fast-chat`, `/stable-label`, `/sharpen`). The suite name just says "here's a collection of session tools."

- **Rejected:** `/steady-session` — follows the [value]-[domain] pattern but feels ostentatious, "too much bragging." Promises a result rather than describing what the tool does.
- **Rejected:** `/session-craft` — aspirational but unnecessary weight
- **Chosen:** `session-kit` — neutral, modest, lets the skills do the branding

**Key insight:** Value-prop naming works for individual skills but not for the suite. Suite names should be modest containers; skill names should sell.

### /fast-chat naming (2026-03-13)

Renamed from `/chatux` (EX_1). The core value is speed — structured codes (1A, 2B, 3 with caveats) replace prose paragraphs, making communication dramatically more efficient.

- **Rejected:** `/chatux` — "ux" is jargon, doesn't convey the speed benefit
- **Rejected:** `/options` — names the mechanism (structured options) but misses the value prop
- **Rejected:** `/ask` — too vague
- **Rejected:** `/shorthand` — accurate mechanism name but doesn't convey speed
- **Chosen:** `/fast-chat` — mixes the value prop ("fast") with the domain ("chat"). Says exactly what it delivers.

**Key insight:** Skill names should mix the value proposition into the name, not just describe the mechanism. `/options` describes what you see; `/fast-chat` describes what you get.

### /sharpen naming (2026-03-13)

Renamed from `/feedback` (EX_2). The skill tracks meta-observations about process and tooling, with resolution lifecycle and promotion paths. The value prop is process improvement, not just collecting feedback.

- **Rejected:** `/feedback` — implies feedback TO someone; these are self-observations about process. Also confusable with product feedback.
- **Rejected:** `/observe` — describes the mechanism, not the value
- **Rejected:** `/process-sharpen` — descriptive but artifact name (`PROCESS-SHARPEN.md`) reads like a command, not a document
- **Rejected:** `/process-tuning` — reads naturally but redundant within session-kit (every skill is about process)
- **Chosen:** `/sharpen` → `SHARPEN.md` — conveys value prop (your process gets sharper), bold artifact name, suite context provides the "process" framing

**Caveat:** "sharpen" isn't an obvious destination for users who think in terms of "feedback" or "meta-feedback." The skill definition will need strong trigger words covering those synonyms. If SHARPEN.md sees low adoption, may need more user-facing guidance to connect the concept. Monitor this.

### /stable-label naming (2026-03-13)

Renamed from `/label` (EX_7). The skill is more than labels — it's a system for stable, greppable cross-references that never renumber and always resolve to exactly one definition. The labeling is the mechanism, but the value is the reference system.

- **Rejected:** `/label` — accurate for the mechanism but misses the "stable references" value
- **Rejected:** `/tag` — implies categorization (like git tags), leans verb
- **Rejected:** `/id` — too specific to the artifact format, not the system
- **Rejected:** `/ref` — accurate but doesn't convey the stability guarantee
- **Rejected:** `/ref_ids` — too specific, underscore in command name unusual
- **Chosen:** `/stable-label` — self-documenting ("the labels are stable"), memorable rhyme is a feature not a bug. User: "i love that b rhymes, makes it memorable"

### /notes eval findings and adjustments (2026-03-14)

Ran 10 eval pairs (with-skill vs baseline) on /notes. Key findings:

**Biggest differentiator:** Bootstrap — CLAUDE.md + discipline block is the killer feature. The baseline creates a reasonable NOTES.md but nothing persists the behavior to future sessions.

**Second differentiator:** User quotes. The skill consistently captures the user's exact words; the baseline paraphrases. User preference: quote the user, paraphrase everything else (agent reasoning, conversation context, rationale, rejected alternatives).

**Non-discriminating tests:** Add-a-note, implicit decisions, near-miss questions, and multi-decision bursts all performed similarly with and without the skill. Claude is already good at these — the skill doesn't need to over-specify them.

**Adjustments made:**
- Added "Where /notes Adds Value" section — focuses the skill on its unique value (discipline, structure, quotes) rather than things Claude handles well natively
- Strengthened quote guidance: "Quote the user, paraphrase everything else" — user's voice should stand out from surrounding summary
- Bootstrap now seeds Open Questions from project context (the with-skill bootstrap was emptier than baseline on this)
- Bootstrap step 5 (CLAUDE.md discipline) marked as "the most important step"

### /warmup design decisions (2026-03-14)

**Scope:** /warmup uses every tactic available to make skills load reliably at session start and after compaction. It's not just a CLAUDE.md helper — it's the reliability layer.

**Three jobs:**
1. Bootstrap CLAUDE.md with compaction-resistant wording, Required Reading, and discipline blocks
2. Loading canaries — verification that files were actually consumed, not just referenced
3. Reliability guidance — strategies for when system prompts or compaction fight CLAUDE.md directives

**Tactics** (use whatever works):
- CLAUDE.md wording and structure (discipline blocks, Required Reading sections)
- Auto-memory entries for non-negotiable behaviors (strongest tactic — loads before CLAUDE.md)
- Loading canaries for verification
- Breadcrumbs in CLAUDE.md (e.g., `<!-- managed by /warmup -->`) so users know what /warmup created and can invoke it to add/edit more

**Visibility model:**
- At runtime: canaries and discipline blocks do the talking. No splash screen.
- In CLAUDE.md: breadcrumbs marking /warmup-managed sections so users discover the skill organically.

**Mid-session compaction role:** auditor, not executor. The Post-Compaction Rule handles re-reading files. /warmup checks whether the rule exists and was followed, flags issues, offers to strengthen. Does not re-read files itself.

**Agent Harness Reference:** extracted to `references/harnesses.md` to keep SKILL.md lean and make the reference independently updatable. Covers Claude Code, Codex CLI, OpenCode, Cursor. Cross-platform strategy: AGENTS.md as single source of truth, strongly direct Claude Code to read it.

**Description pushiness:** per skill-creator best practices, description includes proactive triggers — fresh session with no canary, compaction detected mid-conversation, project with directive files but no loading structure.

### /stable-label design decisions (2026-03-14)

**Convention:**
- Three-letter prefixes default (`XXX_N`), two-letter acceptable when unambiguous
- Underscore separator — greppable + double-click selectable
- Append-only, never renumber, never reuse

**Prefix table location:** convention rules (behavioral directives) go in AGENTS.md and/or CLAUDE.md; prefix table (living reference data) goes in NOTES.md under Taxonomy / Conventions. Split because rules are directives, the table is reference data.

**Consistency passes:** defined as suggested approaches at different scales (Quick, Standard, Sweep, Structural), not rigid levels. Other skills can follow the guidelines independently — /stable-label doesn't police them.

**ID Lifecycle:** five patterns — splitting, merging, deprecation, promotion, crosscutting. All follow the same principle: retired IDs always resolve to meaningful content. Light guidelines, not hard rules — agent judgment is sufficient in most cases.

**Crosscutting:** when a concern spans multiple domains, each domain gets its own ID with domain-relevant content. Not duplicates — different facets. Cross-reference between them.

**Filenames:** zero-padded IDs optional guidance. Tradeoffs: two conventions (padded vs unpadded) + padding width is a guess (breaks at 1000). Let users decide.

### /dictation design decisions (2026-03-14)

**Scope broader than the name:** /dictation covers voice-to-text errors (primary use case), recurring typos, and emergent shorthand (like "1b1" for one-by-one). Kept the name because voice input is still the core value — the broader scope is noted in the intro and README rather than reflected in the name.

**Seed table focus:** Bootstrap should emphasize project-specific jargon over common tech terms. JSON/API/CLI are usually recoverable without a table — the value is in project names, internal tools, and compound terms voice engines split.

**Silent correction with a safety valve:** Most corrections applied silently. But when a correction changes meaning in a way that affects the action taken (e.g., "Maine" → "main"), briefly confirm.

### /fast-chat design decisions (2026-03-14)

**Standard review prompt structure:** The review prompt has two parts — a variable number of situational options (could be 2, 3, 4, whatever fits) adapted to context, followed by a stable tail (Recommendations + Ok) that appears in nearly every review. The situational options default to Add/Change/Remove for artifact reviews, but the count and content change per situation. The stable tail is always the last two letters, regardless of how many situational options precede them.

**Always-on framing:** /fast-chat is an always-on communication style, not just a bootstrap tool. The patterns should be adopted immediately in every interaction where decisions are being made — no explicit invocation required. Invoking `/fast-chat` runs bootstrap (persists conventions to AGENTS.md/CLAUDE.md), but the behavior is immediate.

**NLR formats:** Two common formats identified so far — inline marker (`← recommended`) and rationale paragraph at the end — but these aren't exhaustive. Other formats may emerge. NLR (agent proactively marking its pick when presenting options) is explicitly distinguished from the review prompt's "Recommendations" option (user asking the agent to surface concerns after seeing work). Different direction of flow.

**Patterns are grouped, not counted:** Originally "10 patterns," reduced when "fenced code blocks" folded into NL as a formatting rule, and the review prompt was promoted to its own top-level section. The mechanics/principles grouping does the organizational work — the exact count doesn't matter.

### Disciplines: prose first, tooling when prose drifts (2026-03-14)

From EXTRACTABLE.md EX_6 and PLET.md § "Skills for Judgment, Code for Compliance": disciplines are prose-based, and prose is re-interpreted each invocation — it drifts. When a prose discipline keeps getting violated (especially format compliance, schema rules, consistency checks), supplement with tooling (validation scripts shipped in `scripts/`). Escalation pattern: prose first → if agents drift → build a tool. Not every discipline needs this — most won't — but /sharpen should recognize when prose alone isn't working. /warmup's canaries are already an example of this pattern — prose says "load these files," canaries verify it happened. /stable-label's consistency passes are the most likely candidate for future tooling (a validation script enforcing no-duplicate-definitions, no-orphaned-references, no-renumbered-IDs). No tooling gaps are urgent yet, but /sharpen should recognize these patterns when drift appears.

### /sharpen detection sources (2026-03-14)

Detection sources are broader than just NOTES.md scanning. Five sources: conversation patterns (repeated corrections, consistent preferences), user interaction style (terse answers, shorthand, frustration signals), agent self-observation (own mistakes, inefficient workflows), project artifacts (git history, directive drift, code review comments), and cross-session signals (prior NOTES.md, recurring SHARPEN.md entries, stale auto-memory). NOTES.md remains the single intake *destination* for writing observations down, but these are the *inputs* that feed detection.

### /patterns merged into /sharpen (2026-03-14)

Merged /patterns (EX_4) into /sharpen (EX_2). Both skills deal with process improvement — /patterns detects recurring patterns proactively, /sharpen tracks process observations with a resolution lifecycle. The user shouldn't have to choose between them when thinking "this process thing should be captured."

**Merged skill features:**
- Proactive detection ("I've seen this twice") — from /patterns
- Resolution lifecycle (open → resolved) — from /sharpen
- Promotion paths (→ CLAUDE.md, → NOTES.md) — from both
- Discipline creation ("express this as a named discipline") — from /patterns

**Name: /sharpen** — conveys the value prop (your process gets sharper). /patterns is descriptive but flat.

**Artifact: SHARPEN.md** — observations with IDs, lifecycle states, and promotion paths.

**Result:** 6 skills total instead of 7.

### /discipline folded into /warmup + /sharpen (2026-03-14)

Dropped /discipline as a standalone skill. Its responsibilities split across two existing skills:

- **/warmup** gets the **format and enforcement** — discipline block structure (scannable, enforceable, composable), writing blocks into AGENTS.md and/or CLAUDE.md, loading and verifying via Required Reading and canaries
- **/sharpen** gets the **detection and creation** — recognizing "this workflow should be a discipline," helping users express informal habits as named disciplines, the meta-pattern of identifying what needs formalization

Individual skills (like /notes) create their own discipline during bootstrap, proving no separate /discipline skill is needed.

- **Rejected:** standalone /discipline skill — too much overlap with /warmup (format, enforcement) and /patterns (detection)
- **Chosen:** split across /warmup (infrastructure) and /sharpen (recognition)

---

## Invariants & Critical Requirements

*(None yet)*

---

## Important Concepts & Insights

### From the user

- "should a skill be a noun or verb?" — led to the nouns-for-systems principle
- "label is more than the labels. it's stable references." — drove the /stable-label rename
- "i love that b rhymes, makes it memorable but maybe too cute?" → decided it's a feature, not a bug
- "i'm not worried about long. the claude code ui is awesome at autocomplete" — length of slash commands is not a concern; clarity and descriptiveness win

---

## Taxonomy / Conventions

### Skill roster (in progress — names under review)

| # | Current name | Status | Source |
|---|-------------|--------|--------|
| 1 | /notes | **Implemented** | Existing |
| 2 | /fast-chat | **Implemented** | EX_1 |
| 3 | /sharpen | **Implemented** | EX_2 + EX_4 |
| 4 | /dictation | **Implemented** | EX_3 |
| 5 | /warmup | **Implemented** | EX_5 |
| 6 | ~~/patterns~~ | Merged into /sharpen | EX_4 |
| 7 | ~~/discipline~~ | Folded into /warmup + /sharpen | EX_6 |
| 8 | /stable-label | **Implemented** | EX_7 |

---

## Open Questions

- ~~Suite name~~ → resolved: session-kit
- ~~Skill 2 (/chatux) naming~~ → resolved: /fast-chat
- ~~Skill 3 (/feedback) naming~~ → resolved: /sharpen (monitor adoption — name may not be intuitive for "feedback" mental model)
- Opencode compatibility — skills should work with opencode as well as Claude Code. Need to investigate opencode's skill/plugin format and identify what (if anything) needs to differ.

---

## Things to Monitor

*(None yet)*

---

## Artifact Approval Status

*(None yet)*
