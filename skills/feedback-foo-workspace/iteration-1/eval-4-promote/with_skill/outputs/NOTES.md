# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Decisions

### SPI_1 promoted to CLAUDE.md discipline
Agents were skipping consistency passes after renames (observed sessions 2, 4, 5). Pattern confirmed and validated. Promoted to "Rename Consistency Discipline" in CLAUDE.md — requires grepping for stale references after every rename before proceeding. SPI_1 marked resolved in SHARPEN.md.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
