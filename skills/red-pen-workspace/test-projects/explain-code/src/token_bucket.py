import logging
import math

import redis

log = logging.getLogger(__name__)

# KEYS[1] = bucket key; ARGV = capacity, refill_per_sec, requested
# Uses Redis server time so all replicas share one clock.
_LUA = """
local cap = tonumber(ARGV[1])
local rate = tonumber(ARGV[2])
local want = tonumber(ARGV[3])
local t = redis.call('TIME')
local now = tonumber(t[1]) + tonumber(t[2]) / 1e6
local b = redis.call('HMGET', KEYS[1], 'tokens', 'ts')
local tokens = tonumber(b[1]) or cap
local ts = tonumber(b[2]) or now
tokens = math.min(cap, tokens + (now - ts) * rate)
local ok = 0
if tokens >= want then
  tokens = tokens - want
  ok = 1
end
redis.call('HSET', KEYS[1], 'tokens', tokens, 'ts', now)
redis.call('EXPIRE', KEYS[1], math.ceil(cap / rate) * 2)
return {ok, tostring(tokens)}
"""


class TokenBucket:
    """Per-API-key rate limiter shared across replicas through Redis."""

    def __init__(self, client: redis.Redis, capacity: int = 200, refill_per_sec: float = 100.0):
        self._client = client
        self._capacity = capacity
        self._rate = refill_per_sec
        self._script = client.register_script(_LUA)

    def check(self, api_key: str, cost: int = 1) -> tuple[bool, int]:
        """Return (allowed, retry_after_seconds)."""
        try:
            ok, tokens = self._script(keys=[f"rl:{api_key}"], args=[self._capacity, self._rate, cost])
        except redis.RedisError:
            # Fail open: a Redis outage must not take down balance serving.
            log.warning("rate limiter unavailable; allowing request")
            return True, 0
        if ok:
            return True, 0
        missing = cost - float(tokens)
        return False, max(1, math.ceil(missing / self._rate))
