# SHARPEN.md
<!-- managed by /sharpen -->

Process observations that need active lifecycle tracking. Observations
start in NOTES.md; promote here when they need monitoring across sessions.
See /sharpen for detection sources, routing, and discipline creation.

## Open

### SPI_2: Review cycles take too many round-trips [friction]

The "anything else?" pattern forces 3+ rounds when structured options would take 1.
/fast-chat's review prompt helps but agents don't always use it.
`[resolved]` → Added interaction conventions to CLAUDE.md.
`[reopened]` → Still happening in sessions 7 and 8 despite the fix.

## Resolved

### SPI_1: Agents skip consistency pass after file renames [convention]

Noticed in sessions 2, 4, and 5. After renaming a file or variable, agents
proceed without checking for stale references. Three occurrences — confirmed pattern.

`[resolved]` → Created "Rename Consistency Discipline" in CLAUDE.md. Three-step
post-rename checklist: consistency pass, NOTES.md update, stale reference check.

### SPI_3: Commit messages inconsistent [convention]

`[resolved]` → Added commit style section to CLAUDE.md. Themed bullet lists
with verb-prefixed subject lines.
