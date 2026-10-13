# `src/token_bucket.py`: how it works

## What it's for

This is the **per-API-key rate limiter** for ledgerd. ledgerd runs as three replicas behind a load balancer, and all three share one Redis. The limiter keeps its state in Redis, so a key's limit applies **across the whole service**, not separately on each replica. A client can't get 3x the limit just because the load balancer spreads its requests around.

The defaults are `capacity=200` and `refill_per_sec=100`. Each API key can burst up to 200 requests, then sustain 100 requests per second.

## The token bucket idea (30-second version)

Each API key has a bucket that holds up to `capacity` tokens.

- Tokens refill continuously at `refill_per_sec`.
- A request costs `cost` tokens (default 1).
- If the bucket has enough tokens, they're removed and the request is allowed.
- If it doesn't, the request is rejected and nothing is removed.

Nothing runs in the background to add tokens. Each time a key is checked, the code works out how many tokens have accumulated since its last check. This is called "lazy refill."

## The two halves of the file

### 1. The Lua script (`_LUA`, lines 10–28): the real logic

The bucket math runs **inside Redis** as a Lua script, for two reasons:

- **Atomicity.** Redis runs a script start to finish with no other commands interleaved. Doing read → compute → write from Python would be a race: two replicas could both read "1 token left" and both allow a request. In a script, that can't happen.
- **One clock.** The script gets the time from Redis (`redis.call('TIME')`), not from each replica's system clock. If the three replicas' clocks drifted apart, the refill math would be wrong. Using Redis time gives everyone the same clock.

What the script does, step by step:

| Lines | What happens |
|---|---|
| 11–13 | Read the arguments: `cap`, `rate`, `want` (the cost). |
| 14–15 | Get the current Redis time as fractional seconds. `TIME` returns `[seconds, microseconds]`. |
| 16–18 | Load the bucket hash (`tokens`, `ts` = time of the last update). If the key doesn't exist yet, treat the bucket as **full**, last updated now. |
| 19 | Refill: add `elapsed * rate` tokens, capped at `cap`. Tokens are floats, so partial tokens build up smoothly. |
| 20–24 | If there are enough tokens, subtract the cost and set `ok = 1`. |
| 25 | Save the new token count and timestamp. This happens on denials too, so the refill isn't counted twice next time. |
| 26 | Set a TTL of `ceil(cap / rate) * 2` seconds (4 s with the defaults). A bucket refills completely in `cap / rate` seconds, so an idle key looks the same as a missing one. Expiring it just frees memory and changes no behavior. |
| 27 | Return `{ok, tostring(tokens)}`. |

**Why `tostring(tokens)`?** When Redis converts a Lua number into a reply, it **truncates it to an integer**. Sending the count as a string keeps the fractional part (e.g. `"0.37"`), which Python needs to compute an accurate retry time.

### 2. The `TokenBucket` class (lines 31–51): the Python wrapper

- **`__init__`** stores the config and calls `client.register_script(_LUA)`. This gives back a callable that uses `EVALSHA`, so Redis receives a hash instead of the full script on each call. If Redis has lost its script cache (e.g. after a restart), redis-py notices and resends the script automatically.
- **`check(api_key, cost=1)`** is the only method you'll call. It returns `(allowed, retry_after_seconds)`:
  - The Redis key is `rl:{api_key}`.
  - **Allowed** → `(True, 0)`.
  - **Denied** → `(False, n)`. `n` is how long until enough tokens build up: `ceil((cost - tokens) / rate)`, at least 1 second. It's meant to go straight into an HTTP `Retry-After` header. At 100 tokens/sec it will almost always be `1`.
  - **Redis error** → `(True, 0)` and a log warning. This is **fail-open**, and it's on purpose. See below.

## The key design decision: fail open

```python
except redis.RedisError:
    # Fail open: a Redis outage must not take down balance serving.
```

If Redis is unreachable, every request is **allowed**. The team chose this because serving balances matters more than enforcing limits. A rate-limiter outage shouldn't become a ledgerd outage. You should know what that costs:

- While Redis is down, **there is no rate limiting at all**, on any replica.
- The warning is logged **once per request**. During an outage under load, that can flood the logs.
- Fail-open only triggers on *exceptions*. If Redis is slow rather than down, each `check()` blocks for as long as the Redis client's timeout allows. So the `socket_timeout` / `socket_connect_timeout` you set on the `redis.Redis` client you pass in decide how much latency a sick Redis adds to every request.

## Edge cases and gotchas

- **`cost > capacity` can never succeed.** The bucket never holds more than `capacity` tokens. A request like that is always denied, yet the caller is told to retry in about 1 second, forever. If heavy operations ever get large costs, keep them at or below `capacity`, or validate the cost.
- **`cost` should be a positive integer.** `cost=0` is always allowed. A negative cost would *add* tokens. Nothing checks for either.
- **Redis version.** Calling `TIME` and then writing in the same script requires Redis 5+ (script effects replication). Multi-field `HSET` requires 4.0+. On anything modern this is fine.
- **Clock jumps.** Everything runs on the Redis server's clock. If Redis fails over to a node whose clock is behind, `now - ts` could be negative for a moment and briefly drain tokens. It's rare and fixes itself.
- **The raw API key is part of the Redis key name** (`rl:<key>`). Anyone with Redis access (or reading `MONITOR` / `KEYS` output) can see API keys. Keep that in mind if the keys are secrets.
- **Config is per instance.** Every replica must build `TokenBucket` with the same `capacity` / `refill_per_sec`. Otherwise they'll apply different math to the same shared bucket.

## Typical usage

```python
limiter = TokenBucket(redis.Redis(host=..., socket_timeout=0.05))

allowed, retry_after = limiter.check(api_key)
if not allowed:
    return 429, {"Retry-After": str(retry_after)}
```

## If you're going to change it

- Keep the logic **inside the Lua script**. Moving any read-modify-write into Python brings back the race between replicas.
- Keep using **Redis `TIME`**, not `time.time()`, for the same reason.
- If you change the return format, remember Lua numbers are truncated to integers on the way back.
- Changing fail-open to fail-closed is a product decision (availability vs. abuse protection), not just a code change. Talk to the team first.
