# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

### Rename Discipline — enforced in CLAUDE.md
Added a mandatory three-step post-rename checklist to CLAUDE.md: (1) consistency pass via grep, (2) NOTES.md update, (3) stale-reference verification through build/tests. Motivated by repeated pattern of agents skipping consistency checks after renames (see SHARPEN.md SPI_1).

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
