# FEEDBACK_FOO.md
<!-- managed by /foo -->

Process observations that need active lifecycle tracking. FOO = Feedback,
Observation, Oversight. Observations start in NOTES.md; promote here when
they need monitoring across sessions.
See /foo for detection sources, routing, and discipline creation.

## Open

### FOO_1: Agents skip consistency pass after file renames [convention]

Noticed in sessions 2, 4, and 5. After renaming a file or variable, agents
proceed without checking for stale references. Three occurrences — confirmed pattern.

### FOO_2: Review cycles take too many round-trips [friction]

The "anything else?" pattern forces 3+ rounds when structured options would take 1.
/fast-chat's review prompt helps but agents don't always use it.
`[resolved]` → Added interaction conventions to CLAUDE.md.
`[reopened]` → Still happening in sessions 7 and 8 despite the fix.

### FOO_4: Agent skips NOTES.md update after decisions despite discipline [drift]

Third occurrence this session. The NOTES.md Discipline in CLAUDE.md states
"Update NOTES.md after every decision, before moving to the next topic" but
the agent keeps drifting. Prose alone is not holding — this may need a
stronger enforcement mechanism (e.g., a self-check step appended to every
decision-making workflow, or a post-decision canary). Cross-ref: NOTES.md
process observations section.

## Resolved

### FOO_3: Commit messages inconsistent [convention]

`[resolved]` → Added commit style section to CLAUDE.md. Themed bullet lists
with verb-prefixed subject lines.
