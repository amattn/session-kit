# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Session Bootstrap

**At the start of every session, before doing any work, read these files in full:**

1. `NOTES.md` — institutional memory (decisions, rationale, open questions)
2. `CLAUDE.md` — this file (project rules and conventions)

This is not optional. These files contain decisions that took significant effort to reach. Skipping them risks re-litigating settled questions or contradicting established conventions.

**After context compaction, re-read the files listed above.** Compaction loses detail — the source files are the ground truth. If you notice your memory of project conventions feels vague or incomplete, stop and re-read before continuing.

## Key Files

- `NOTES.md` — institutional memory
- `src/` — application source code

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.** Do not defer. The pattern of "I'll catch up on notes later" always fails — decisions accumulate faster than memory, and by session's end the rationale is gone.

- Each decision (approve, reject, rename, add, remove) gets a NOTES.md entry immediately
- If you realize you've fallen behind, stop and catch up before continuing

## Compaction Safety

When context gets compacted, critical directives can be lost. To guard against this:

- **Always re-read CLAUDE.md and NOTES.md after compaction** — do not rely on summary
- **Keep NOTES.md concise and scannable** — bullet points over prose, decisions over discussion
- **Front-load the most important context** — put project identity and active constraints at the top of each file
