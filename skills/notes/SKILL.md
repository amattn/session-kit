---
name: notes
version: 0.1.0
description: "Maintain living development notes as institutional memory. Use when the user asks to 'notes', 'start notes', 'update notes', 'capture this decision', 'note this', 'add to notes', 'reorganize notes', or 'bootstrap notes'. Also trigger when a decision is made that should be recorded, when the user asks about past decisions, or when NOTES.md needs reorganization. Maintains a NOTES.md file that captures the why behind project decisions — rationale, rejected alternatives, user insights, invariants, and conventions."
user-invocable: true
---

# /notes — Living Development Notes

Maintain institutional memory across multi-session AI-assisted development. NOTES.md captures what other project artifacts don't: the *why* behind decisions, rejected alternatives, user insights, and conventions.

---

## The Job

1. Detect whether NOTES.md exists in the project
2. If not, run the bootstrap flow
3. If yes, operate on it using the Notes Discipline

---

## Bootstrap

When invoked on a project with no NOTES.md:

1. **Create NOTES.md** with a Project Context section filled in from available context (CLAUDE.md, README, repo structure, git history)
2. **Add suggested section headers** as scaffolding (see § Suggested Starting Sections) — empty sections are fine
3. **Reference from CLAUDE.md** — add NOTES.md as a key file so every session loads it
4. **Add Notes Discipline to CLAUDE.md** — add the discipline block so it's enforced every session (see § Notes Discipline for CLAUDE.md)
5. **Inform the user** — explain what was created and how the Notes Discipline works

---

## Suggested Starting Sections

These are a **suggested starting point**, not a rigid template. The structure should evolve with emergent content — new sections will appear, existing ones may merge, split, or occasionally be retired (content migrated elsewhere). The structure should serve the project, not constrain it.

The first four are the most important — they carry the most weight and get referenced and updated most frequently:

1. **Key Design Decisions** — What was decided, why, rejected alternatives, status (decided/open/revisiting). Change rationale and review pass changes belong here as dated entries. Typically the largest and most active section.
2. **Invariants & Critical Requirements** — Load-bearing rules that must not be violated. Each stated as a checkable rule, justified, and scoped. Small but high-impact.
3. **Important Concepts & Insights** — Principles, user values, design insights. Sub-categories: "From the user" (direct quotes) and "Emergent" (crystallized during design).
4. **Taxonomy / Conventions** — Canonical vocabulary definitions, naming conventions, formatting rules. Prevents vocabulary disputes from resurfacing.

The rest are useful but lower-traffic:

5. **Open Questions** — Unresolved topics, things to investigate, items awaiting user input.
6. **Things to Monitor** — Watchlist items: drift risks, size concerns, potential problems.
7. **Project Context** — Brief "what is this," "where did it come from," one-liner on how it works. Near the top of the document. Mostly static after kickoff.
8. **Artifact Approval Status** — Section-by-section tracking of what's been reviewed and approved. Most useful when there's no separate plan file tracking this.

---

## Notes Discipline

These rules are the core of the skill. They make NOTES.md trustworthy.

1. **Update immediately.** When a decision is made, update NOTES.md before moving on. Don't batch updates. "I'll catch up later" always fails — decisions accumulate faster than memory.
2. **Decisions are permanent until revisited.** A decision in NOTES.md is settled. Don't re-litigate without the user raising it.
3. **Capture rejected alternatives.** The "why not" is as valuable as the "why." Prevents future sessions from suggesting the same rejected approach.
4. **Quote the user.** When the user expresses a principle or preference, capture it in their words. Paraphrasing loses nuance.
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
