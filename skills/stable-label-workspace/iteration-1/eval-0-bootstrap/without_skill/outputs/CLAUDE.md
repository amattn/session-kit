# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Key Files

- `NOTES.md` — institutional memory (includes stable label registry)

## Stable Labels

This project uses stable labels — greppable identifiers like `[DB-POSTGRES]` or `[NO-DB-MOCKS]` — as permanent references to decisions, invariants, and architectural anchors. The full registry lives in the **Stable Labels** section of `NOTES.md`. When referencing a decision or constraint in code comments, commit messages, or docs, use the label so it can be found later via grep.

**Conventions:**
- All labels are defined in the registry table in `NOTES.md`
- Format: `[UPPER-KEBAB-CASE]` in square brackets
- Prefix open/unresolved questions with `OPEN-`
- When a decision is made, add a new label and reference it inline
- Labels are never reused or reassigned; retire obsolete ones by noting "RETIRED" in the table
