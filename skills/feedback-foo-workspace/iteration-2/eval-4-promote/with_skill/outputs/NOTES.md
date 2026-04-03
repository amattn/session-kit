# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Decisions

### FOO_1 promoted to CLAUDE.md directive
Agents were skipping consistency passes after file/variable renames (observed sessions 2, 4, 5). Pattern confirmed — promoted from FEEDBACK_FOO.md to a CLAUDE.md directive: "Consistency Pass After Renames" with a four-step checklist (search old name, update references, verify, proceed). FOO_1 marked resolved in FEEDBACK_FOO.md.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
