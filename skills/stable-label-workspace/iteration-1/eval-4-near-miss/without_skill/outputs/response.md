# Top 5 Features to Build

Based on the project context (inventory-api, Python/FastAPI/PostgreSQL, deployed on Fly.io), here are the top 5 features to build:

1. **CRUD endpoints for inventory items** — The core of the API. Create, read, update, and delete inventory records with proper HTTP status codes (per REQ_2) and snake_case JSON responses with top-level "data"/"error" keys (per REQ_4).

2. **Authentication and authorization** — Currently an open question (JWT vs session tokens, noted in NOTES.md). This is a prerequisite for any production deployment and must be resolved and implemented before launch.

3. **Offline sync support for the mobile app** — REQ_5 requires the API to support a companion mobile app with offline sync capabilities. This means conflict resolution, last-modified timestamps or versioning, and delta/batch sync endpoints.

4. **Database schema and migrations** — Stand up the PostgreSQL schema with a migration framework (Alembic is the standard choice for SQLAlchemy/FastAPI). The ORM question (SQLAlchemy vs raw SQL) from the open questions needs to be settled first.

5. **Integration test suite with CI pipeline** — REQ_3 mandates tests against a real database (no mocking). Set up a test PostgreSQL instance in GitHub Actions (DEC_4), write integration tests for all endpoints, and gate merges on passing tests.
