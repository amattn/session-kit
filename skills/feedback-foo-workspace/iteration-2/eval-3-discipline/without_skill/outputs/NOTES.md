# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

### Rename Discipline added to CLAUDE.md
After repeated issues with stale references after renames (sessions 2, 4, 5), added a four-step discipline: consistency pass, update references, update NOTES.md, final check. This addresses FOO_1.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
