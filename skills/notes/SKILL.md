---
name: notes
version: 0.2.1
description: "Maintain living development notes as institutional memory. Use when the user asks to 'notes', 'start notes', 'update notes', 'capture this decision', 'note this', 'add to notes', 'reorganize notes', or 'bootstrap notes'. Also trigger when a decision is made that should be recorded, when the user asks about past decisions, or when NOTES.md needs reorganization. Maintains a NOTES.md file that captures the why behind project decisions — rationale, rejected alternatives, user insights, invariants, and conventions."
user-invocable: true
---

# /notes — Living Development Notes

> **Quick Reference:** See [HELP.md](HELP.md) for setup, usage, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.
> For detailed mechanics or edge cases, the full SKILL.md has the complete specification.

Maintain institutional memory across multi-session AI-assisted development. NOTES.md captures what other project artifacts don't: the *why* behind decisions, rejected alternatives, user insights, and conventions.

---

## The Job

1. Detect whether NOTES.md exists in the project
2. If not, run the bootstrap flow
3. If yes, operate on it using the Notes Discipline

---

## Bootstrap

When invoked on a project with no NOTES.md:

1. **Write `NOTES.md` to the project root** using the inline template in § NOTES.md Template → Template content below, substituting variables as you write (do not copy from disk — the template ships inline so the skill stays self-contained):
   - `{{PROJECT_NAME}}` — the project name (directory name is a reasonable default; ask if ambiguous)
   - `{{DATE}}` — today's date in YYYY-MM-DD
   - `{{PROJECT_DESCRIPTION}}` — one-sentence description from available context (README, CLAUDE.md, repo structure, conversation); if unknown, leave the `_(Replace this paragraph…)_` placeholder for the user to fill in
2. **The template ships with** all suggested section headers and the default Stable Label Prefixes table already populated — see § NOTES.md Template below.
3. **Reference from AGENTS.md and/or CLAUDE.md** — add NOTES.md as a key file so every session loads it. If /warmup is also installed, add it to § Required Reading.
4. **Add the Notes Discipline block to AGENTS.md and/or CLAUDE.md** — see § Notes Discipline for AGENTS.md/CLAUDE.md below. Without this, the note-taking behavior doesn't survive to the next session.
5. **Inform the user** — explain what was created, that the template ships with default stable-label prefixes (the user can rename or customize in § Taxonomy / Conventions), and how the Notes Discipline works. Offer to seed Open Questions (`OPN_N`) by scanning the project for obvious unresolved topics — an empty Open Questions section is a missed opportunity, but let the user decide whether to seed now or later.

---

## NOTES.md Template

The canonical NOTES.md scaffold ships inline in § Template content below — the skill carries its own template so the bootstrap never reads an external asset file. It ships with:

- **Always-on `## Quick Reference` front-matter section** (between the H1 intro and the first content section). Combines two purposes that share the "orient before content" job:
  - **Convention pointer** as the body — a brief in-file orientation block that primes the reader/agent before they encounter any IDs. States the ID format, append-only rule, section-label-vs-ID distinction, and the entry header format. Points to AGENTS.md § Stable Label Convention for the full rules.
  - **`### Sections` sub-H3 as the TOC** — always present, even for a fresh empty NOTES.md. Users add H3 entries (`DEC_1`, `INS_2`, etc.) to the TOC as they create them. A stale TOC is worse than no TOC.
- All 8 suggested sections (see § Suggested Starting Sections) as headers with placeholder italics describing what belongs in each
- A pre-populated **Stable Label Prefixes** table under § Taxonomy / Conventions — the 7-prefix defaults that pair with /stable-label: `DEC`, `ICR`, `INS`, `OPN`, `MON`, `TAX`, `FOO`. Each section header in the template references which prefix it uses.
- The `TAX_N`-as-enumeration-unit semantic note (e.g., `TAX_1` = "8 phases" as a whole, not one phase)
- A pointer to AGENTS.md § Stable Label Convention for the append-only rules

### Entry header format

Every entry that gets a stable-label ID uses this format in its header:

```
### PREFIX_N: YYYY-MM-DD - Title
```

The colon after the ID marks where structured metadata ends. The date follows. Then a ` - ` separator and the free-form title. Titles can contain dashes (or anything else) — the format is unambiguous because the structured fields are positionally fixed before the title starts.

Bulleted sections (Open Questions, Things to Monitor, Invariants) use the same format inside the bullet:

```
- **OPN_1: YYYY-MM-DD - Title** — body text
```

This format choice trades one colon for parse stability: titles can be any prose without breaking grep-and-extract scripts.

**Why this lives in /notes (not /stable-label):** the template is the NOTES.md scaffold, and /notes owns NOTES.md. /stable-label owns the convention *rules* (append-only, no renumber) which live in AGENTS.md. The two skills cooperate: if /stable-label is also installed, it adapts to the pre-seeded table; if /stable-label is *not* installed, the table is harmless scaffolding text and the user can ignore or delete it.

**Customizing the defaults:** the prefix table in the template is opinionated but not load-bearing. Users may rename prefixes, drop unused ones, or add project-specific ones at bootstrap time. After IDs are in the wild, the append-only rules from /stable-label take over — prefixes can be added but not renamed without breakage.

### Template content

When bootstrapping NOTES.md, write this content to `NOTES.md` at the project root. Substitute `{{PROJECT_NAME}}`, `{{DATE}}`, and `{{PROJECT_DESCRIPTION}}` as you write — do not write the literal `{{…}}` placeholders into the project's NOTES.md.

````markdown
# NOTES.md — {{PROJECT_NAME}}

Living institutional memory for {{PROJECT_NAME}}. Captures the **why** behind decisions, rejected alternatives, user insights, and conventions. See AGENTS.md (or CLAUDE.md) § NOTES.md Discipline for update rules.

---

## Quick Reference

**Stable label IDs** use `XXX_N` format (e.g., `DEC_1`, `OPN_3`). **Append-only** — never renumber, never reuse. Bare prefixes appearing in section headers like `(TAX)` are **section labels**, not IDs.

**Entry header format:** `### PREFIX_N: YYYY-MM-DD - Title`

Examples:
- `### DEC_1: 2026-05-27 - Adopt Postgres for the event store`
- `- **OPN_3: 2026-05-27 - What auth scheme?**` (bullet form for list-shaped sections)

The colon marks the end of structured metadata (ID, date). Everything after the date's ` - ` is free-form title — titles can contain dashes freely.

**Full prefix table:** § Taxonomy / Conventions below.
**Full convention rules:** AGENTS.md § Stable Label Convention.
**Skill suite:** [session-kit](https://github.com/amattn/session-kit) — `/notes` defines this template; `/stable-label` defines the ID convention.

### Sections

- [Project Context](#project-context)
- [Invariants & Critical Requirements (ICR)](#invariants--critical-requirements-icr)
- [Important Concepts & Insights (INS)](#important-concepts--insights-ins)
- [Taxonomy / Conventions (TAX)](#taxonomy--conventions-tax)
- [Key Design Decisions (DEC)](#key-design-decisions-dec)
- [Open Questions (OPN)](#open-questions-opn)
- [Things to Monitor (MON)](#things-to-monitor-mon)
- [Artifact Approval Status](#artifact-approval-status)

_As you add H3 entries (`DEC_1`, `INS_2`, etc.), add them under their parent section here. A stale TOC is worse than no TOC._

---

## Project Context

**{{PROJECT_NAME}}** — {{PROJECT_DESCRIPTION}}.

Bootstrap: {{DATE}}.

_(Replace this paragraph with: what is this project, where did it come from, one-liner on how it works. List anything explicitly TBD so future sessions don't make assumptions.)_

---

## Invariants & Critical Requirements (ICR)

_Load-bearing rules that must not be violated. Each stated as a checkable rule, justified, and scoped. Small but high-impact. Assigned `ICR_N` IDs. The `(ICR)` in this heading is a section label, not an ID — see § Stable Label Convention above._

_Example format — replace with real entries:_

- **ICR_1: YYYY-MM-DD - All times stored in UTC.** Why: avoid timezone bugs across users and servers. Scope: every persisted timestamp.

---

## Important Concepts & Insights (INS)

### From the user

_Direct quotes from the user about principles, values, or preferences — verbatim. Quotes resist drift across sessions and preserve the user's voice._

### Emergent

_Insights crystallized during design conversation. Paraphrase freely. Assigned `INS_N` IDs._

_Example format — replace with real entries:_

### INS_1: YYYY-MM-DD - Insight title

Body explaining the insight and why it matters.

---

## Taxonomy / Conventions (TAX)

### Stable Label Prefixes

| Prefix | Artifact type                          | Source section                       |
|--------|----------------------------------------|--------------------------------------|
| DEC    | Design decisions                       | Key Design Decisions                 |
| ICR    | Invariants & critical requirements     | Invariants & Critical Requirements   |
| INS    | Insights & principles                  | Important Concepts & Insights        |
| OPN    | Open questions                         | Open Questions                       |
| MON    | Things to monitor                      | Things to Monitor                    |
| TAX    | Taxonomy groups (enumerations)         | Taxonomy / Conventions               |
| FOO    | Feedback / observations / oversight    | FEEDBACK_FOO.md (when /foo runs)     |

**TAX semantics:** each `TAX_N` is a complete **enumeration unit** (e.g., "8 phases", "3 bug types", "5 feature types"). Members are referenced by name in prose by default. Promote to sub-IDs (`TAX_N_M` or `TAX_N_NAME`) only if a specific taxonomy starts being cross-referenced enough to warrant it.

**Convention rules:** see AGENTS.md § Stable Label Convention. Append-only; never renumber, never reuse; always use the full registered prefix.

_(Customize the table for this project: rename prefixes, drop unused ones, add project-specific ones. Append-only once IDs exist in the wild.)_

---

## Key Design Decisions (DEC)

_What was decided, why, rejected alternatives, status. Typically the largest and most active section. Assigned `DEC_N` IDs. Capture rejected alternatives — the "why not" is as valuable as the "why."_

_Example format — replace with real entries:_

### DEC_1: YYYY-MM-DD - Adopt Postgres for the event store

Chose Postgres for ACID guarantees on the event log.

**Why:** event ordering correctness is load-bearing; we will reconstruct state from this log.

**Rejected alternatives:**
- **DynamoDB** — cheaper at scale but eventual consistency makes ordering reasoning harder
- **SQLite** — simpler ops but no concurrent writers

---

## Open Questions (OPN)

_Unresolved topics, things to investigate, items awaiting user input. Assigned `OPN_N` IDs._

_Example format — replace with real entries:_

- **OPN_1: YYYY-MM-DD - What auth scheme?** JWT vs session cookies vs OAuth-only. Needs a security review before deciding.

---

## Things to Monitor (MON)

_Watchlist items: drift risks, size concerns, potential problems. Assigned `MON_N` IDs._

_Example format — replace with real entries:_

- **MON_1: YYYY-MM-DD - NOTES.md size.** Currently small; revisit if it exceeds ~500 lines or starts crowding context.

---

## Artifact Approval Status

_Section-by-section tracking of what's been reviewed and approved. Most useful when there's no separate plan file._
````

---

## Suggested Starting Sections

These are a **suggested starting point**, not a rigid template. The structure should evolve with emergent content — new sections will appear, existing ones may merge, split, or occasionally be retired (content migrated elsewhere). The structure should serve the project, not constrain it.

The order below reflects natural reading flow: stable reference material first (orient quickly), then the growing decision log. A new reader — or an agent recovering from compaction — gets the high-signal context before hitting detailed history.

The first five are the most important — they carry the most weight and get referenced and updated most frequently:

1. **Project Context** — Brief "what is this," "where did it come from," one-liner on how it works. Near the top of the document. Mostly static after kickoff.
2. **Invariants & Critical Requirements** — Load-bearing rules that must not be violated. Each stated as a checkable rule, justified, and scoped. Small but high-impact.
3. **Important Concepts & Insights** — Principles, user values, design insights. Sub-categories: "From the user" (direct quotes) and "Emergent" (crystallized during design).
4. **Taxonomy / Conventions** — Canonical vocabulary definitions, naming conventions, formatting rules. Prevents vocabulary disputes from resurfacing.
5. **Key Design Decisions** — What was decided, why, rejected alternatives, status (decided/open/revisiting). Change rationale and review pass changes belong here as dated entries. Typically the largest and most active section — placed after reference sections so it doesn't push them out of view.

The rest are useful but lower-traffic:

6. **Open Questions** — Unresolved topics, things to investigate, items awaiting user input.
7. **Things to Monitor** — Watchlist items: drift risks, size concerns, potential problems.
8. **Artifact Approval Status** — Section-by-section tracking of what's been reviewed and approved. Most useful when there's no separate plan file tracking this.

---

## Notes Discipline

These rules are the core of the skill. They make NOTES.md trustworthy.

1. **Update immediately.** When a decision is made, update NOTES.md before moving on. Don't batch updates. "I'll catch up later" always fails — decisions accumulate faster than memory.
2. **Decisions are permanent until revisited.** A decision in NOTES.md is settled. Don't re-litigate without the user raising it.
3. **Capture rejected alternatives.** The "why not" is as valuable as the "why." Prevents future sessions from suggesting the same rejected approach.
4. **Quote the user, paraphrase everything else.** When the user expresses a principle or preference, capture it in their exact words — quotes resist drift across sessions, preserve tone and emphasis, and give the user ownership over the notes. Paraphrase freely for everything else: agent reasoning, conversation context, rationale analysis, rejected alternatives. The user's voice should stand out from the surrounding summary.
5. **Keep it scannable.** Use headers, bold, bullet points. A fresh agent should be able to scan NOTES.md in seconds and know what's settled.
6. **Reference from CLAUDE.md.** NOTES.md only works if it's loaded into every session. Add it as a key file in CLAUDE.md.
7. **Cascade awareness.** Decisions captured in NOTES.md may need to propagate to other project artifacts. CLAUDE.md or other directive files may define project-specific cascading instructions. After capturing a decision, check whether it affects other artifacts.
8. **Consistency passes.** After significant NOTES.md updates, run a consistency pass on affected artifacts to catch drift.
9. **Watch for reorg signals.** Periodically assess whether NOTES.md structure still fits the project. When drift signals appear (see § Reorganization), suggest a reorg to the user.

### Notes Discipline for CLAUDE.md

During bootstrap (or when adopting the pattern on an existing project), add this block to CLAUDE.md so the discipline is enforced every session:

```
## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.** This is not
optional and not deferrable. The pattern of "I'll catch up on notes later" always fails —
decisions accumulate faster than memory, and by the end of a session the rationale is lost.

During build/review sessions where decisions come rapid-fire:
- Each user decision (approve, reject, rename, reorder, add, remove) gets a NOTES.md
  entry *before* presenting the next item
- If you realize you've fallen behind, stop and catch up immediately — do not continue
  accumulating debt
- Batch answers (e.g., "1A, 2C, 3D") still get individual NOTES.md entries for each
  decision

The cost of writing notes is seconds. The cost of lost rationale is re-litigating settled
decisions in the next session.
```

---

## What Does NOT Go In NOTES.md

- **Full requirement or content text** — that belongs in the project's primary artifacts. Tracking approval status is fine — just don't duplicate content.
- **Implementation details** — that's in the code or spec
- **Task tracking** — that's in state files or issue trackers
- **Temporary session state** — "I'm currently working on X" doesn't belong

---

## Signs Content Has Outgrown NOTES.md

Content often starts in NOTES.md because it's the easiest place to capture something. That's fine — but watch for these signals that an entry should graduate to its own document:

- **It develops its own internal structure** — sub-sections, scenarios, matrices, tables. Notes entries are relatively flat; internal hierarchy means it's becoming a document.
- **A single entry dominates its parent section** — longer than everything else in the section combined. A document wearing a notes hat.
- **It stops getting updated *and* matches the other signals** — static content is fine (settled decisions are valuable institutional memory). But a large, structured, static block likely belongs elsewhere. Static content that doesn't match the other signals may just need to float lower in the file.

When content shows these signs, extract it to its own file and leave a pointer in NOTES.md. The pointer preserves discoverability; the extraction keeps NOTES.md focused on living institutional memory.

---

## Reorganization

Periodically suggest a reorganization when signs of drift appear:

- **Entries landing in the wrong section** — content doesn't fit existing headers
- **Sections growing unwieldy** — too many unrelated entries in one section
- **Thematic clusters emerging** — related entries scattered across multiple sections
- **Stale sections** — headers with outdated or rarely-updated content
- **Extracted sections** — content graduated to its own document; replace with a pointer as historical reference

### Reorg pass

1. **Inventory** — read the full NOTES.md and identify thematic clusters
2. **Propose new structure** — suggest renames, merges, splits, reordering, and any content that should graduate to its own document
3. **Get approval** — present the proposed structure to the user before executing
4. **Execute** — move entries to their new homes, extract graduated content, update any TOC, verify nothing was lost

Reorganization is not cleanup for its own sake — it keeps the file's structure aligned with how the project actually thinks.

---

## Scaling: Hierarchical Prefixes for Large Projects

The default prefix style — `DEC_1`, `ICR_3`, `OPN_7` — works for small to mid-size projects (up to ~50 entries per section). As NOTES.md grows past that, two pressures emerge:

1. **Section headers become the navigation surface** — readers skim H2/H3 to find the right neighborhood before drilling in
2. **Cross-references want section-level anchors** — "see § Architecture decisions" beats grepping 200 `DEC_N` entries

The **hierarchical prefix** style addresses both by making each section header itself a stable-label ID. The pattern composes a *scope prefix* (typically the file or directory name — `NOTES`, `SPEC`, `GUIDE`) with a *section prefix* (the section's role — `DEC`, `INV`, `TAX`, `PLN`):

```
## NOTES_DES: Key Design Decisions
### NOTES_DES_1: Architecture & Routing
#### Squash architecture redesign (2026-03-22)
#### Worktree + shared artifacts merge strategy (2026-03-26)

### NOTES_DES_2: State & Data
#### State file design (2026-03-22)
```

In this pattern:
- `NOTES_DES` is the **section ID** — greppable as a unit; cross-references like "see NOTES_DES" jump to the section
- `NOTES_DES_1`, `NOTES_DES_2` are **sub-category IDs** — clusters within the section
- Individual H4 entries stay greppable by their dated titles

When multiple NOTES.md files exist (see § Multiple NOTES.md Files), each gets its own *scope* prefix so cross-references stay unambiguous: `NOTES_DES_3` (root NOTES.md) vs `SPEC_DES_3` (`specs/NOTES.md`). The scope prefix replaces the plain `DEC` — within a hierarchical project, `DEC_3` alone is ambiguous; `NOTES_DES_3` is not.

**When to graduate from plain to hierarchical:**

- Any single section exceeds ~50 entries and starts feeling unwieldy
- Multiple NOTES.md files exist and bare prefixes (`DEC_N`) would collide across files
- Natural sub-clusters are emerging in a large section (e.g., DEC entries split cleanly into architecture / data / execution / verification)

**Migration is additive, not destructive.** Append-only rules apply: existing `DEC_N` IDs stay valid. New entries adopt the hierarchical scheme; old entries are not retro-renamed. Both forms coexist during the transition and grep continues to work for both. Update the prefix table in § Taxonomy / Conventions to register the new scope prefixes.

**Don't graduate prematurely.** The plain style is easier to write, easier to read, and sufficient for the vast majority of projects. The hierarchical style pays off only when the section/sub-category structure is doing real navigation work — until then, it's overhead.

---

## Multiple NOTES.md Files

### When to create a second NOTES.md

Start with a single root `NOTES.md`. Most projects never need more than one. When a second notes file is warranted, it goes in a subfolder as that subfolder's `NOTES.md` (e.g., `guide/NOTES.md`) — never as a second file at root (no `NOTES-2.md`). A subfolder gets its own NOTES.md when:

- **It has its own decision history** — the subfolder represents a distinct workstream with its own design conversations, not just a directory of files
- **Different people or agents work on it** — if worked on independently, its decisions shouldn't clutter the root notes
- **The root NOTES.md is getting too large** — splitting by scope is a size management strategy

Don't create one just because a subfolder exists. The bar is: "does this area have its own ongoing conversation?"

### Routing

When multiple files exist, define a routing table in CLAUDE.md:

```
## NOTES.md Routing

| File | Scope |
|------|-------|
| `NOTES.md` (root) | Main project — design decisions, conventions |
| `guide/NOTES.md` | Guide/presentation — content decisions |

**Default rule:** If working in `guide/`, write to `guide/NOTES.md`.
Otherwise write to root `NOTES.md`. If ambiguous, ask.
```

Key principles:
1. **Scope determines destination** — route by topic, not by which file you're editing
2. **One default, explicit exceptions** — root NOTES.md is the default; other files are listed exceptions
3. **Cross-references over duplication** — if a decision affects another scope, add a pointer rather than duplicating
4. **When ambiguous, ask** — one clarification round-trip costs less than mis-routed notes

### Loading

Reference each NOTES.md in CLAUDE.md. For projects with many scoped files, consider loading only the root by default and scoped files on demand — keeps context usage manageable.

---

## Size Management

NOTES.md is loaded every session, so its size impacts available context. When it starts crowding out working context:

- **Reorganize** — tighten structure, eliminate redundancy
- **Graduate content** — extract entries that have outgrown NOTES.md
- **Split into scoped files** — if covering too many concerns, split with routing rules
- **Float stale content down** — settled, rarely-referenced content sinks toward the bottom; top stays high-signal

The goal: keep NOTES.md focused on living institutional memory — the content that actively informs the next decision.

---

## How It Fits

```
CLAUDE.md             → references NOTES.md as a key file
                        (ensures every session loads it)

NOTES.md              → captures decisions that shape the project
                        (institutional memory, the "why")

Project artifacts     → the primary work products shaped by decisions
                        (the "what" — code, specs, content, etc.)
```

NOTES.md sits between project config (CLAUDE.md) and the project's primary artifacts. It's the connective tissue that explains why the project looks the way it does.
