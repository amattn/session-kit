# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

### Consistency Pass After Renames
FOO_1 validated — agents were skipping reference checks after file/variable renames.
Added mandatory consistency pass directive to CLAUDE.md. Moved FOO_1 to Resolved.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
