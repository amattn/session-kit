# NOTES.md — api-project

## Project Context

REST API for managing inventory. Python-based, early stage.

---

## Key Design Decisions

- **Framework: FastAPI** (decided 2026-03-14) — Chosen over Flask. FastAPI provides async support, automatic OpenAPI docs, and Pydantic validation out of the box — good fit for a REST API project. Flask was the other candidate but offers less built-in API tooling.

- **Deployment: Fly.io** (decided 2026-03-14) — Platform for hosting the API. Provides simple container-based deployment with global edge infrastructure. Other targets were not formally evaluated; user selected Fly.io directly.

- **CI: GitHub Actions** (decided 2026-03-14) — Continuous integration pipeline. Standard choice for GitHub-hosted repos — no additional service to manage, good ecosystem of reusable actions.

---

## Invariants & Critical Requirements

*(None yet)*

---

## Open Questions

- Database choice — PostgreSQL vs SQLite?

---

## Taxonomy / Conventions

*(None yet)*
