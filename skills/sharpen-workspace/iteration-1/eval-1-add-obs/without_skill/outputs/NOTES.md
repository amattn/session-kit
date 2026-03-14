# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Observations

### SPI_4: Agent forgets to run tests after changes
User-reported friction. Tracked in SHARPEN.md as an open observation. Next step: consider adding a "run tests after code changes" rule to CLAUDE.md once the pattern is confirmed with specific session examples.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
