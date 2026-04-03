# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

### Rename Consistency Discipline — created via /foo
User confirmed the three-step rename pattern (consistency pass, NOTES.md update, stale reference check) is mature enough for a discipline. Added to CLAUDE.md. Resolves FOO_1.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
