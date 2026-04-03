# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Self-Improvement
<!-- managed by /sharpen -->

When you notice a recurring pattern, convention, drift, or friction not yet
captured in project instructions — surface it immediately and propose where
to write it down. If you've seen it twice, it's a pattern.

The human approves all changes. Your job is to notice and propose.

## Rename Discipline

After every rename (file, variable, function, class, module, endpoint, etc.), complete all three steps in order before moving on:

1. **Consistency pass** — grep the codebase for all remaining references to the old name. Fix every stale reference (imports, strings, comments, configs, tests, docs).
2. **Update NOTES.md** — record what was renamed, why, and confirm the consistency pass was done.
3. **Stale-reference check** — run the build/tests (or a targeted grep if no build exists) to verify nothing was missed.

Do not skip or reorder these steps. Do not move to the next task until all three are complete. If a rename touches multiple names, each name gets its own pass through all three steps.

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.**

## Key Files

- `NOTES.md` — institutional memory
