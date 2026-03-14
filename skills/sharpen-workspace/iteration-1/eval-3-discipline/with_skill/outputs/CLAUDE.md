# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Self-Improvement
<!-- managed by /sharpen -->

When you notice a recurring pattern, convention, drift, or friction not yet
captured in project instructions — surface it immediately and propose where
to write it down. If you've seen it twice, it's a pattern.

The human approves all changes. Your job is to notice and propose.

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.**

## Rename Consistency Discipline
<!-- managed by /sharpen -->

**After every rename (file, variable, function, module), complete all three steps before continuing.**

1. Run a consistency pass — search the codebase for all references to the old name and update them
2. Update NOTES.md — record what was renamed and why, so the next session has context
3. Check for stale references — grep for the old name one more time to confirm nothing was missed (imports, comments, configs, docs, tests)

Do not proceed to the next task until all three steps are done. The order matters: fix references first, then record the decision, then verify.

This discipline exists because agents repeatedly skipped the consistency pass after renames (SPI_1, observed sessions 2, 4, 5), leaving stale references that caused runtime failures discovered much later.

## Key Files

- `NOTES.md` — institutional memory
