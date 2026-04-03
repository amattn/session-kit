# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Self-Improvement
<!-- managed by /foo -->

When you notice a recurring pattern, convention, drift, or friction not yet
captured in project instructions — surface it immediately and propose where
to write it down. If you've seen it twice, it's a pattern.

The human approves all changes. Your job is to notice and propose.

## Consistency Pass After Renames
<!-- managed by /foo -->

**After renaming any file, variable, function, or class, run a consistency pass before proceeding.**

1. Search the codebase for all references to the old name
2. Update every stale reference (imports, config files, tests, documentation)
3. Verify no references to the old name remain
4. Only then continue with the next task

Skipping this step causes broken imports and stale references that compound over time.

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.**

## Key Files

- `NOTES.md` — institutional memory
