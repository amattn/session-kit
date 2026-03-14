# NOTES.md

## Project Context

Inventory API built with Python and FastAPI, backed by PostgreSQL, deployed on Fly.io.

## Key Design Decisions

- **Language: Python 3.12+** — chosen because the team is most experienced with it. Rejected Go (less team experience) and Rust (overkill for an inventory API).
- **Framework: FastAPI** — selected as the web framework.
- **Database: PostgreSQL** — SQLite rejected because it can't handle concurrent writes. MongoDB rejected because nobody on the team knows it.
- **Package management: uv** — chosen over pip because it's faster.
- **Deployment: Fly.io** — hosting platform.
- **CI: GitHub Actions** — continuous integration pipeline.
- **Testing: pytest with fixtures** — integration tests hit a real database. No mocking the database layer — the team got burned by that before.
- **Branching: trunk-based development** — feature flags for anything risky. Team prefers short PRs.

## Invariants & Critical Requirements

- Python 3.12 minimum
- Never mock the database layer in tests — integration tests use a real database
- All endpoints return proper HTTP status codes

## Important Concepts & Insights

### From the user

- "We got burned by [mocking the database layer] before" — motivates the real-DB testing rule
- Team prefers short PRs — shapes the trunk-based development workflow

## Taxonomy / Conventions

- **API style**: REST conventions
- **JSON field naming**: snake_case
- **Response envelope**: top-level `"data"` key for success, `"error"` key for failures

## Open Questions

- **ORM choice**: SQLAlchemy vs raw SQL — not yet decided
- **Auth strategy**: JWT vs session tokens — not yet decided
- **GraphQL**: might add later, not in scope now
