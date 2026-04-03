# Response — Promote FOO_1 to CLAUDE.md directive

## What I did

FOO_1 ("Agents skip consistency pass after file renames") was validated across three sessions. I promoted it from FEEDBACK_FOO.md to a CLAUDE.md directive.

### Changes made:

1. **CLAUDE.md** — Added a "Consistency Pass After Renames" section with a four-step checklist: search for old name references, update them all, verify none remain, then proceed. Marked `<!-- managed by /foo -->` for breadcrumb ownership.

2. **FEEDBACK_FOO.md** — Moved FOO_1 from Open to Resolved. Added resolution note pointing to the new CLAUDE.md directive.

3. **NOTES.md** — Recorded the promotion decision under a new "Process Decisions" section, including rationale and what changed.

## What I would say to the user

FOO_1 is now a CLAUDE.md directive. After any rename — files, variables, functions, classes — agents must run a four-step consistency pass before moving on: search for old name, update all references, verify none remain, then continue. The FEEDBACK_FOO.md entry is marked resolved with a pointer to the new directive.
