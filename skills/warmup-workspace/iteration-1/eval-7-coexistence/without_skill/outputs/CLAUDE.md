# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## NOTES.md Discipline
<!-- managed by /notes -->

**Update NOTES.md after every decision, before moving to the next topic.** This is not optional and not deferrable. The pattern of "I'll catch up on notes later" always fails — decisions accumulate faster than memory, and by the end of a session the rationale is lost.

During build/review sessions where decisions come rapid-fire:
- Each user decision (approve, reject, rename, reorder, add, remove) gets a NOTES.md entry *before* presenting the next item
- If you realize you've fallen behind, stop and catch up immediately — do not continue accumulating debt

## Interaction Conventions
<!-- managed by /fast-chat -->

Use **numbers-letters style** when presenting choices. Always suggest options.

## Session Warmup

At the start of every session, **read these files immediately** before doing any other work:

1. `CLAUDE.md` (this file)
2. `NOTES.md`

This ensures institutional memory, project conventions, and key design decisions are loaded into context before any task begins.

**Compaction survival:** If context gets compacted mid-session, re-read both files before continuing work. The cost of re-reading is seconds; the cost of working without context is wrong decisions and re-litigation of settled questions.

### Why this matters

- `NOTES.md` contains design decisions and their rationale. Without it, you risk proposing alternatives that were already evaluated and rejected.
- `CLAUDE.md` contains interaction conventions and workflow discipline. Without it, you lose the session's operating norms.
- Other skills (`/notes`, `/fast-chat`) have their own sections above — warmup ensures their instructions are actually in context when needed.

## Key Files

- `CLAUDE.md` — project instructions, conventions, warmup config (this file)
- `NOTES.md` — institutional memory (decisions, rationale, open questions)
