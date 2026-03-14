# NOTES.md — api-project

## Project Context

REST API for managing inventory.

---

## Key Design Decisions

### Database: PostgreSQL (2026-03-14)

Chose PostgreSQL over SQLite. Need concurrent writes from multiple services.

### Framework: FastAPI (2026-03-14)

Chose FastAPI over Flask for async support.

---

## Open Questions

- Deployment target — undecided
- CI/CD — undecided
