`src/token_bucket.py` is the per-API-key rate limiter for ledgerd. Its state lives in Redis rather than in process memory so that all three replicas behind the load balancer enforce one shared limit.

It is a token bucket: each key gets a burst allowance that refills at a fixed rate. The defaults are a 200-token capacity refilling at 100 tokens/sec, so a key can burst 200 requests and then sustain 100/sec. Each request spends `cost` tokens (default 1), so an expensive endpoint can charge more.

How a call to `check(api_key, cost)` works:

- **Redis does the work.** One Lua script reads the bucket at `rl:<api_key>`, adds the tokens earned since the last call, deducts `cost` if enough are left, and writes the result back. Redis runs scripts atomically, so two replicas hitting the same key can't both spend the last token.
- **Redis supplies the clock.** The script calls `TIME` instead of using the replica's clock, so clock skew between replicas can't add or remove tokens.
- **New and idle keys start full.** A missing key is treated as a full bucket. The key expires after `ceil(capacity / rate) * 2` seconds (4s with the defaults), twice the time it takes an empty bucket to refill. An expired key is therefore full anyway, and Redis doesn't keep a key for every client ever seen.
- **A denial carries a retry hint.** The second return value is the number of whole seconds until enough tokens exist, at least 1. The script returns the token count as a string because Redis would truncate a Lua float to an integer.

The one deliberate policy choice: if Redis errors, `check` fails open and allows the request, because a Redis outage must not take down balance serving.

The cost: during an outage nothing is rate-limited, and the warning is logged once per request, so expect a flood of log lines.

One trap for callers: a `cost` above `capacity` can never succeed. `check` still returns a retry-after, but retrying will never work.
