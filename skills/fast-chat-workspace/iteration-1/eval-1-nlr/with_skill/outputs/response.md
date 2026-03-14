Here are your three questions reformatted with recommendations:

```
1. What database should we use?
   A. PostgreSQL
   B. MySQL
   C. SQLite ← recommended
   D. Other — please specify

2. What ORM should we use?
   A. Prisma ← recommended
   B. Drizzle
   C. TypeORM
   D. Raw SQL / query builder (e.g., Knex)
   E. Other — please specify

3. How should we handle auth?
   A. Session-based (cookie + server-side session store)
   B. JWT (stateless tokens) ← recommended
   C. OAuth2 / OpenID Connect (delegated to a provider)
   D. API keys only
   E. Other — please specify
```

**Recommendations:**

**1C — SQLite.** For an inventory API, SQLite keeps the stack simple — no separate database server to manage, easy to back up, and surprisingly capable for single-server workloads. If you expect multi-server deployments or heavy concurrent writes, PostgreSQL (1A) becomes the better choice, but SQLite is the right starting point until those needs are real.

**2A — Prisma.** Strong type safety, auto-generated migrations, and the schema-as-source-of-truth model fits well with a REST API where the data model is central. Drizzle (2B) is a solid lighter-weight alternative if you prefer staying closer to SQL.

**3B — JWT.** For a REST API, stateless JWT auth keeps things simple — no session store to manage, works naturally with multiple clients, and scales horizontally without shared state. If you need login via Google/GitHub/etc., you'd layer OAuth2 (3C) on top, but JWT is the right base mechanism.

Reply with codes (e.g., `1C, 2A, 3B`) or ask to discuss any item.
