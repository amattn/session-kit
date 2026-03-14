# NOTES.md

We decided to use Python. Also FastAPI is good. The database will be PostgreSQL because SQLite can't handle concurrent writes. We rejected MongoDB because nobody knows it.

Deployment is on Fly.io. GitHub Actions for CI. We might add GraphQL later but not now.

The API should follow REST conventions. Use snake_case for JSON fields. Always return proper HTTP status codes.

Python 3.12 minimum. We're using uv for package management instead of pip because it's faster.

Open question: should we use SQLAlchemy or raw SQL? Also need to figure out auth — JWT vs session tokens.

The team prefers short PRs. We do trunk-based development. Feature flags for anything risky.

Convention: all endpoints return JSON with a top-level "data" key for success and "error" key for failures.

We considered using Go but Python was chosen because the team is more experienced with it. Also considered Rust but it's overkill for an inventory API.

Testing: pytest with fixtures. Integration tests hit a real database. No mocking the database layer — we got burned by that before.
