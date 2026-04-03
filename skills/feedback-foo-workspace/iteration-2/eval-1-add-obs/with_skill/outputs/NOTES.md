# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Observations

### Agent skips tests after changes
User reported recurring pattern: agent makes code changes but doesn't run
tests afterward. Promoted to FEEDBACK_FOO.md as FOO_4 for active tracking.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
