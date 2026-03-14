# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Observations

### Agent skips test runs after changes
User reports the agent keeps forgetting to run tests after making changes.
Promoted to SHARPEN.md as SPI_4 for active tracking.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
