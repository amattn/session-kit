Here is the current label setup for the inventory-api project.

## Convention

Every referenceable item gets a greppable stable label in `XXX_N` format. Labels are append-only -- they are never renumbered or reused, and gaps are expected. This convention is documented in `CLAUDE.md` under "Stable Label Convention."

## Active Prefixes

| Prefix | Artifact type | Defined in |
|--------|--------------|------------|
| `DEC`  | Design decisions | NOTES.md, "Key Design Decisions" |
| `REQ`  | Requirements / invariants | NOTES.md, "Invariants & Critical Requirements" |

The prefix table lives in NOTES.md under "Taxonomy / Conventions."

## Labels in Use

**Design Decisions (DEC_1 through DEC_5):**

- `DEC_1` — Database: PostgreSQL
- `DEC_2` — Framework: FastAPI
- `DEC_3` — Deployment: Fly.io
- `DEC_4` — CI: GitHub Actions
- `DEC_5` — Caching: in-memory

**Requirements (REQ_1 through REQ_5):**

- `REQ_1` — Python 3.12 minimum
- `REQ_2` — Proper HTTP status codes
- `REQ_3` — No database mocking in tests
- `REQ_4` — snake_case JSON responses
- `REQ_5` — Mobile app support

Next available IDs: `DEC_6`, `REQ_6`.
