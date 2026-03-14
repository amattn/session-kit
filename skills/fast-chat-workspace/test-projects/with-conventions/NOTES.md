# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL on Fly.io.

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support.

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support.

### DEC_3: Deployment — Fly.io (2026-03-14)
Team already has experience with it.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
- Auth: JWT vs session tokens?
- Caching strategy?
