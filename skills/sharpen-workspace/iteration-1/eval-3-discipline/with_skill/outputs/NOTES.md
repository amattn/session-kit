# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Decisions

### Rename Consistency Discipline — created via /sharpen
Formalized the post-rename workflow as a named discipline in CLAUDE.md. The pattern (consistency pass → update NOTES.md → check stale references) was confirmed across sessions 2, 4, and 5 (SPI_1). Promoted from SHARPEN.md to CLAUDE.md as an enforceable discipline.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
