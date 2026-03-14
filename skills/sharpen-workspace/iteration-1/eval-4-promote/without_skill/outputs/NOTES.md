# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Conventions

### Rename Consistency Pass
SPI_1 validated — agents were skipping stale-reference checks after renames (observed sessions 2, 4, 5). Promoted to a CLAUDE.md directive requiring a consistency pass (search for old name, update all references) after every rename before proceeding.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
