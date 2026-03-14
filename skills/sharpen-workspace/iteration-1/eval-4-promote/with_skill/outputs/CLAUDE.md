# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Self-Improvement
<!-- managed by /sharpen -->

When you notice a recurring pattern, convention, drift, or friction not yet
captured in project instructions — surface it immediately and propose where
to write it down. If you've seen it twice, it's a pattern.

The human approves all changes. Your job is to notice and propose.

## Rename Consistency Discipline
<!-- managed by /sharpen -->

**After every file or variable rename, check for stale references before proceeding.**

1. After renaming a file, grep for the old filename across the project and update all imports, references, and configuration entries.
2. After renaming a variable, function, or class, search for the old name and update all call sites, type annotations, and documentation.
3. Do not proceed to the next task until the consistency pass is complete and no stale references remain.

Rationale: agents repeatedly skipped this step (sessions 2, 4, 5), causing broken references that were caught late. See SPI_1 in SHARPEN.md.

## NOTES.md Discipline

**Update NOTES.md after every decision, before moving to the next topic.**

## Key Files

- `NOTES.md` — institutional memory
