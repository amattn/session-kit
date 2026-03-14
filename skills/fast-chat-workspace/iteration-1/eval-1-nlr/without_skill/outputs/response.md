Here are your three questions with options and recommendations:

```
1. What database should we use?
   a. PostgreSQL — battle-tested relational DB, strong ecosystem, excellent for structured inventory data
   b. MySQL — widely deployed, solid performance, broad hosting support
   c. SQLite — zero-config, good for prototyping or single-server deployments
   d. MongoDB — document store, flexible schema, less ideal for relational inventory data

2. What ORM should we use?
   a. Prisma — type-safe, great DX, auto-generated migrations
   b. Drizzle — lightweight, SQL-like syntax, strong TypeScript support
   c. TypeORM — mature, decorator-based, wide adoption
   d. Knex (query builder only) — not a full ORM, maximum SQL control

3. How should we handle auth?
   a. JWT with refresh tokens — stateless, scalable, standard for REST APIs
   b. Session-based auth (server-side sessions + cookies) — simpler, good for single-server setups
   c. OAuth2 / OpenID Connect via a provider (Auth0, Clerk, etc.) — offloads complexity, faster to ship
   d. API keys only — simplest, appropriate if this is a service-to-service API
```

**Recommendations:** 1A, 2A, 3A — PostgreSQL handles inventory workloads well (transactions, constraints, relational queries), Prisma pairs naturally with it and gives you type safety plus easy migrations, and JWT with refresh tokens is the standard pattern for a REST API that may need to scale beyond a single server.
