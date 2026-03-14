# NOTES.md

## Technology Stack

- **Language:** Python 3.12 minimum. Chosen over Go (less team experience) and Rust (overkill for an inventory API).
- **Framework:** FastAPI.
- **Database:** PostgreSQL. SQLite rejected (can't handle concurrent writes). MongoDB rejected (nobody on the team knows it).
- **Package management:** uv (faster than pip).

## Architecture & API Conventions

- REST conventions for the API.
- snake_case for JSON fields.
- Always return proper HTTP status codes.
- All endpoints return JSON with a top-level `"data"` key for success and `"error"` key for failures.

## Development Workflow

- Trunk-based development with short PRs.
- Feature flags for anything risky.

## Deployment & CI

- Deployment on Fly.io.
- GitHub Actions for CI.

## Testing

- pytest with fixtures.
- Integration tests hit a real database — no mocking the database layer (got burned by that before).

## Open Questions

- SQLAlchemy vs raw SQL?
- Auth approach: JWT vs session tokens?
- GraphQL — may add later, not now.
