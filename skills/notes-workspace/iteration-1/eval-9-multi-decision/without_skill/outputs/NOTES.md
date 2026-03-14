# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Framework: FastAPI** — chosen for the REST API. FastAPI provides async support, automatic OpenAPI docs, and strong typing via Pydantic, which fits well for an inventory management API.
- **Deployment: Fly.io** — selected as the deployment target. Provides simple container-based deployments with global edge infrastructure.
- **CI: GitHub Actions** — chosen for continuous integration. Native GitHub integration, free tier for public repos, and broad ecosystem of reusable actions.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- Database choice — PostgreSQL vs SQLite?

---

## Taxonomy / Conventions

*(None yet)*
