Three decisions to make. Here they are in NLR format — my recommendations marked inline.

```
1. ORM approach?
   A. SQLAlchemy ORM (full models, relationships, migrations via Alembic) ← recommended
   B. SQLAlchemy Core (table definitions + raw-ish SQL, no model objects)
   C. Raw SQL with asyncpg
   D. Other — please specify

2. Auth strategy?
   A. JWT (stateless, access + refresh tokens) ← recommended
   B. Server-side sessions (session ID in cookie, state in Redis/DB)
   C. API keys only (simpler, no user login flow)
   D. Other — please specify

3. Caching approach?
   A. Redis — external cache for API responses and hot queries ← recommended
   B. In-process cache (e.g., cachetools / lru_cache)
   C. HTTP cache headers only (let clients/CDN handle it)
   D. No caching for now — add when perf data exists
   E. Other — please specify
```

**Recommendations:**

**1. SQLAlchemy ORM (1A)** — You're on FastAPI + PostgreSQL, which is the bread-and-butter SQLAlchemy stack. The ORM gives you Alembic migrations out of the box, relationship loading, and Pydantic model integration that pairs naturally with FastAPI's response models. Core or raw SQL only make sense if you have complex query performance concerns, which an inventory API is unlikely to hit early.

**2. JWT (2A)** — Stateless auth fits a REST API well. No server-side session store to manage, scales horizontally without sticky sessions on Fly.io, and FastAPI has first-class support via `fastapi-jwt-auth` or `python-jose`. Use short-lived access tokens (15 min) with longer refresh tokens.

**3. Redis (3A)** — Since you're already on PostgreSQL and likely deploying a multi-instance setup on Fly.io, an external cache avoids per-instance cache inconsistency. Redis on Fly.io is straightforward (Upstash or self-hosted). Cache inventory lookups and list queries, invalidate on writes.

---

Respond with codes (e.g., `1A, 2A, 3A`) or pick different options. If you want to discuss any of these one at a time, say `1b1`.
