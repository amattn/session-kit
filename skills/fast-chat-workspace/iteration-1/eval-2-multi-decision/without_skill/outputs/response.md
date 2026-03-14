Here are the three open decisions for inventory-api. Given the existing stack (Python/FastAPI/PostgreSQL on Fly.io), here are the options:

```
1. ORM
   a. SQLAlchemy (async mode) — mature, huge ecosystem, well-documented FastAPI integration
   b. Raw SQL via asyncpg — maximum control, no abstraction overhead
   c. SQLModel — built by FastAPI's author, thin wrapper over SQLAlchemy, Pydantic-native

2. Auth strategy
   a. JWT (stateless) — no server-side session store needed, scales horizontally trivially
   b. Session tokens (server-side) — easier revocation, but requires a session store (Redis or DB)
   c. JWT with refresh tokens + short-lived access tokens — balances statelessness with revocability

3. Caching approach
   a. Redis — standard choice, works well on Fly.io, supports TTL and invalidation
   b. In-process LRU (e.g., cachetools) — simplest, no external dependency, but per-instance only
   c. Redis + in-process LRU (two-tier) — hot path in memory, shared state in Redis
```

**Recommendations:**

1. **1A — SQLAlchemy async.** The project is a standard CRUD inventory API, so an ORM saves significant boilerplate. SQLAlchemy 2.0's async mode pairs well with FastAPI, and the ecosystem (Alembic for migrations, etc.) is unmatched. SQLModel (1C) is appealing but less mature for complex queries.

2. **2C — JWT with refresh tokens.** For an inventory API, you want stateless auth for scalability on Fly.io but also the ability to revoke access. Short-lived access tokens (15 min) with longer refresh tokens stored server-side gives you both.

3. **3A — Redis.** A single-instance cache (3B) breaks as soon as you scale to multiple Fly.io machines. Redis is simple to run on Fly.io (Upstash or Fly Redis), handles TTL natively, and is the standard pairing with FastAPI. The two-tier approach (3C) adds complexity that isn't justified until you have measured latency problems.

Reply with your picks (e.g., "1A, 2C, 3A") and I'll record them in NOTES.md.
