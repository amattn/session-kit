# NOTES.md — inventory-api

> **Re-read this file at every session start and after every context compaction.**

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Active Constraints

- Database: PostgreSQL (not SQLite) — chosen for concurrent write support
- Key files must be re-read after compaction (see CLAUDE.md Session Bootstrap)

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?

## Session Log

(Record decisions here as they are made, one entry per decision, with date and rationale.)
