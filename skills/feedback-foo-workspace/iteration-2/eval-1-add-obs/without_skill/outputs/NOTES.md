# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

## Process Notes

### Run tests after changes
User noticed agents forget to run tests after making code changes. Should always run `pytest` after modifying code.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
