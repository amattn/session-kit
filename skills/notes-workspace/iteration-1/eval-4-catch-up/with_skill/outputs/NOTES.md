# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Framework: FastAPI over Flask** (2026-03-14, decided) — Chose FastAPI for its native async support. Flask was the main alternative but lacks built-in async, which matters for an API that will handle concurrent inventory operations.

- **Deployment: Fly.io** (2026-03-14, decided) — Team already has experience with Fly.io, reducing ramp-up time. No other deployment targets were seriously evaluated given existing team familiarity.

- **API style: REST only, no GraphQL for now** (2026-03-14, decided) — REST is simpler and sufficient for current needs. GraphQL was considered but deferred — it can be added later if query flexibility becomes a real requirement. Avoiding premature complexity.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- Database choice — PostgreSQL vs SQLite?
- ~~Framework choice — FastAPI vs Flask?~~ Resolved: FastAPI (see Key Design Decisions)
- ~~Deployment target — undecided~~ Resolved: Fly.io (see Key Design Decisions)

---

## Taxonomy / Conventions

*(None yet)*
