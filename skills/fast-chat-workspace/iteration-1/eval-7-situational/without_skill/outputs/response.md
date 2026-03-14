Good analysis. A few thoughts based on what you've laid out and the nature of an inventory API:

**PostgreSQL looks like the stronger fit here.** An inventory system is inherently write-heavy — stock updates, order processing, concurrent transactions from multiple users or services. The single-writer limitation in SQLite is a real bottleneck for that use case. PostgreSQL's MVCC handles exactly this scenario well.

The operational overhead concern is valid, but manageable — Docker makes standing up Postgres straightforward, and most cloud providers offer managed instances.

SQLite would be a reasonable choice if this were a single-user tool or a local prototype, but for a REST API serving concurrent clients, PostgreSQL is the safer bet.

```
1. Which database do you want to go with?
   A. PostgreSQL (recommended — better concurrency fit for a multi-client API)
   B. SQLite (simpler setup, but concurrent writes will be a constraint)

2. ORM / query layer?
   A. SQLAlchemy (mature, well-documented, async support via asyncio extension)
   B. Tortoise ORM (async-native, Django-like feel)
   C. Raw asyncpg / aiosqlite (no ORM, full control)
   D. Recommendations

3. Migration tooling?
   A. Alembic (standard pairing with SQLAlchemy)
   B. Other — specify
   C. Recommendations
```
