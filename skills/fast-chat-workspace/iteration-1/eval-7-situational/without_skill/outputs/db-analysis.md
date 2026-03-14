# Database Analysis

## PostgreSQL

**Pros:**
- Excellent concurrent write support via MVCC
- Rich data types (JSONB, arrays, full-text search)
- Mature ecosystem, well-supported by FastAPI/SQLAlchemy
- Strong community, extensive documentation

**Cons:**
- More operational overhead than SQLite
- Requires a separate server process
- Overkill for simple read-heavy workloads

## SQLite

**Pros:**
- Zero configuration, embedded in the application
- Single file, trivial backups
- Fast for read-heavy workloads
- No separate server needed

**Cons:**
- Single writer at a time (WAL mode helps but not enough)
- No built-in replication
- Not ideal for concurrent web services
- Limited data type support
