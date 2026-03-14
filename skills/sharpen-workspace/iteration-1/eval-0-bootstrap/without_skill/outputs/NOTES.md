# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

### Process Improvement System — PROCESS.md
Added `PROCESS.md` as a dedicated file for tracking process observations through a lifecycle: observed -> validated -> discipline -> retired. Observations are captured in the moment with a tally that increments on recurrence. Once validated, patterns can be promoted to enforceable disciplines that get added to both `PROCESS.md` and `CLAUDE.md`. This keeps process knowledge from being lost between sessions and gives a clear path from "I noticed something" to "this is now a rule."

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
