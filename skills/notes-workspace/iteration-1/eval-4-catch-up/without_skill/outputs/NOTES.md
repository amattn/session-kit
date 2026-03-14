# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Framework: FastAPI over Flask** — chosen for its native async support, which aligns better with the API workload. Flask was considered but lacks built-in async capabilities.
- **Deployment: Fly.io** — the team already has experience with Fly.io, reducing ramp-up time and operational risk.
- **API style: REST only (no GraphQL for now)** — REST is simpler and sufficient for current needs. GraphQL can be added later if requirements demand it.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- Database choice — PostgreSQL vs SQLite?

---

## Taxonomy / Conventions

*(None yet)*
