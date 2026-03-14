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
All API endpoints must respond within 200ms under normal load. This is a crosscutting concern — see API_1 for the API layer facet and DBA_1 for the database layer facet.

## API Layer Concerns

### API_1: 200ms response time budget — API layer (2026-03-14)
API endpoints must return responses within the 200ms budget (REQ_5). This includes serialization, middleware, and any orchestration overhead. See also DBA_1 for the database portion of the budget.

## Database Layer Concerns

### DBA_1: 200ms response time budget — database layer (2026-03-14)
Database queries must complete well within the 200ms budget (REQ_5) to leave room for API-layer overhead. Includes query execution, connection pool latency, and any ORM overhead. See also API_1 for the API portion of the budget.

## Taxonomy / Conventions

### Stable Label Prefixes

| Prefix | Artifact type |
|--------|--------------|
| DEC    | Design decisions |
| REQ    | Requirements / invariants |
| API    | API layer concerns |
| DBA    | Database layer concerns |
