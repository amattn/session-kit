# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### FOO_2 escalation — directive to discipline
The session 5 fix (interaction conventions added to CLAUDE.md as a simple paragraph) didn't prevent the "anything else?" round-trip pattern from recurring in sessions 7 and 8. The directive was too soft — agents re-interpreted it each time and drifted back to the old behavior. Escalating to a named discipline with numbered, imperative rules. If the discipline doesn't hold after 2-3 sessions, next step is tooling (e.g., a prompt template that auto-structures review output).
