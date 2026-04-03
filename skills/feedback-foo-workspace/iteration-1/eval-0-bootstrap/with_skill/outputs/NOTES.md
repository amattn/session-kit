# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process

### /sharpen bootstrapped
Set up process improvement tracking. Created SHARPEN.md for lifecycle-tracked observations. Added self-improvement directive to CLAUDE.md. No existing process observations found to seed — starting fresh.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
