Token bucket.

- Partners are bursty (the 2k rps one). Token bucket lets short bursts through while holding the average rate; fixed window lets 2x through at the boundary, leaky bucket queues (you already rejected queueing in favor of 429), sliding log costs memory per key.
- Fits what's already decided: one Lua script in Redis, keyed by API key, returns tokens-left so you can set `Retry-After`.
- Default, per "pick one and revisit": 100 rps sustained, burst 200, per key. Two numbers, no other knobs.

If you'd rather not allow bursts at all, sliding window counter is the fallback.
