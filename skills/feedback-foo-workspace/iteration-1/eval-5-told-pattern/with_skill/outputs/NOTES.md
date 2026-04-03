# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Observations

### NOTES.md updates skipped after decisions — 3rd occurrence this session
Agent failed to update NOTES.md after a decision three times in one session, despite the NOTES.md Discipline in CLAUDE.md. The existing discipline states the rule but doesn't prevent the failure. Promoted to SHARPEN.md as SPI_4. See also: proposed discipline strengthening in CLAUDE.md.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
