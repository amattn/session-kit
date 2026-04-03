# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Framework — FastAPI
Chose over Flask for async support.

### Timestamps — Always UTC
All timestamps use UTC. No local timezones in storage or API responses.

## Open Questions

- ORM: SQLAlchemy vs raw SQL?
