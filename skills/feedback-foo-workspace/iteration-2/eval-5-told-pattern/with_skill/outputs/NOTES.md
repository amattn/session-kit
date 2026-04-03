# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Observations

### Agent fails to update NOTES.md after decisions — third occurrence
Pattern confirmed: agent skipped NOTES.md updates after decisions three times this session despite the existing NOTES.md Discipline in CLAUDE.md. The prose discipline alone is not sufficient — the agent re-interprets it each time and still drifts. Promoted to FEEDBACK_FOO.md as FOO_4 for active tracking. Proposed strengthening the CLAUDE.md discipline with explicit self-check language.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
