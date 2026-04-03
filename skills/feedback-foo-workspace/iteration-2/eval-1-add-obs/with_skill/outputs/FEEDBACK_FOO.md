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

### FOO_4: Agent forgets to run tests after making changes [workflow]

User-reported pattern: after making code changes, the agent proceeds without
running the test suite. Needs more data points to confirm frequency, but
worth tracking now. If confirmed, candidate for a CLAUDE.md discipline
(e.g., "Run tests after every code change before reporting completion").

## Resolved

### FOO_3: Commit messages inconsistent [convention]

`[resolved]` → Added commit style section to CLAUDE.md. Themed bullet lists
with verb-prefixed subject lines.
