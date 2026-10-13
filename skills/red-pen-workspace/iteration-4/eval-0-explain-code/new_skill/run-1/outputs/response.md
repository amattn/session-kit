`src/token_bucket.py` caps each API key at a burst of 200 requests, refilling at 100 per second. It enforces that cap across all three replicas by keeping the state in the shared Redis.

The model is a token bucket: a burst allowance that refills at a fixed rate. Each key's bucket holds up to 200 tokens. A request spends `cost` tokens (default 1), and tokens come back at 100 per second up to the cap. An idle key is back to 200.

How `check(api_key, cost)` works:

- **One Lua script does the work.** Redis runs a Lua script atomically, so refill, spend, and write happen as one step. Two replicas checking the same key at once cannot spend the same token.
- **Redis supplies the clock.** The script reads Redis `TIME`, not the replica's clock, so drift between replicas does not matter.
- **State is a hash at `rl:<api_key>`** with two fields, `tokens` and `ts` (last update). A missing hash means a full bucket. Keys expire after 4 idle seconds (`ceil(200/100) * 2`). The bucket is full again by then, so expiry only frees memory.
- **It returns `(allowed, retry_after_seconds)`.** On a denial, `retry_after` is the time to refill the shortfall, rounded up, minimum 1. The script returns the token count as a string because Redis truncates Lua floats to integers.

Two behaviours to know before you change it:

- **It fails open.** On any `RedisError`, `check` logs a warning and allows the request, because a Redis outage must not take down balance serving.
- **A `cost` above 200 is never allowed.** The bucket cannot hold that many tokens, yet the caller still gets a finite `retry_after`, so a client that obeys it retries forever. This repo has no callers of `check`, so whether it bites depends on the services that call it.

The cost of failing open: while Redis is down, no replica rate-limits anything.
