# SHARPEN.md
<!-- managed by /sharpen -->

## Open

### SPI_2: Review cycles take too many round-trips [friction]

The "anything else?" pattern forces 3+ rounds when structured options would take 1.
`[resolved]` → Added interaction conventions to CLAUDE.md (session 5).
`[reopened]` → Still happening in sessions 7 and 8 despite the fix.
`[escalated]` → Prose convention wasn't sufficient — agents kept drifting. Replaced
with a structured Interaction Discipline in CLAUDE.md with numbered enforceable rules.
If drift continues, next step is a validation script that flags open-ended "anything else?"
patterns in agent output.

## Resolved

### SPI_1: Agents skip consistency pass after renames [convention]

`[resolved]` → Added rename discipline to CLAUDE.md.
