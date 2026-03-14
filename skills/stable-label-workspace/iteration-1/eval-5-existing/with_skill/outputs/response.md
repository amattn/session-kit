Here's your current stable-label setup for inventory-api:

**Convention rules** are in CLAUDE.md — append-only, never renumber, never reuse. Gaps are expected.

**Prefix table** (from NOTES.md § Taxonomy / Conventions):

| Prefix | Artifact type | Current count |
|--------|--------------|---------------|
| DEC    | Design decisions | 5 (DEC_1 through DEC_5) |
| REQ    | Requirements / invariants | 5 (REQ_1 through REQ_5) |

No gaps in either sequence — both run contiguously from 1 to 5.

No sub-groups are in use. No orphaned references or duplicate definitions noticed in a quick scan.

What do you need? Some options:

- **Assign IDs** to new items (e.g., label those open questions)
- **Add a prefix** for a new artifact type (e.g., `QST` for open questions, `OBS` for observations)
- **Run a consistency pass** to verify all references resolve correctly
- Something else
