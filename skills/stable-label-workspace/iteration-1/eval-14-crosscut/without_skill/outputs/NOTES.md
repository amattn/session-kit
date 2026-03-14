# NOTES.md — inventory-api

## Key Design Decisions

### DEC_1: Database — PostgreSQL (2026-03-14)
Chose over SQLite for concurrent write support.

### DEC_2: Framework — FastAPI (2026-03-14)
Chose over Flask for async support.

## Invariants & Critical Requirements

### REQ_1: Python 3.12 minimum

### REQ_2: Proper HTTP status codes

### REQ_3: No database mocking in tests

### REQ_4: snake_case JSON responses

### REQ_5: 200ms response time
All API endpoints must respond within 200ms under normal load.
This is a crosscutting concern that affects both the API layer and the database query layer. API-side work (serialization, middleware, routing) and database-side work (query execution, indexing, connection pooling) must each be budgeted to fit within the overall 200ms envelope.

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
| API    | API layer concerns |
| DBA    | Database layer concerns |
