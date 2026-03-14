# NOTES.md — api-project

## Project Context

REST API for managing inventory.

---

## Key Design Decisions

### Database: PostgreSQL (2026-03-14)

Chose PostgreSQL over SQLite. Need concurrent writes from multiple services.

### Framework: FastAPI (2026-03-14)

Chose FastAPI over Flask for async support.

### Deployment: Fly.io (2026-03-14)

Chose Fly.io for deployment.

### CI/CD: GitHub Actions (2026-03-14)

Chose GitHub Actions for CI.

---

## Open Questions

(none currently)
