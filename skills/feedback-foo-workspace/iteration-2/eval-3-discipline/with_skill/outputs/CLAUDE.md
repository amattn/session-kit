# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Self-Improvement
<!-- managed by /foo -->

When you notice a recurring pattern, convention, drift, or friction not yet
captured in project instructions — surface it immediately and propose where
to write it down. If you've seen it twice, it's a pattern.

The human approves all changes. Your job is to notice and propose.

## Rename Consistency Discipline
<!-- managed by /foo -->

**After every rename (file, variable, function, module), complete all three steps before moving on.**

1. Run a consistency pass — search the codebase for all references to the old name and update them
2. Update NOTES.md — record what was renamed and why, so future sessions have the context
3. Check for stale references — grep for the old name one more time to confirm nothing was missed (imports, configs, docs, tests, comments)

Do not proceed to the next task until all three steps are done. Skipping step 3 is how stale references survive — the consistency pass catches the obvious ones, the final check catches what the pass missed.

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.**

## Key Files

- `NOTES.md` — institutional memory
