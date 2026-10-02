Token bucket, in Redis, keyed by API key.

Partners are bursty, so allow short bursts but cap the sustained rate. Fixed window lets 2x through at the boundary; sliding window is more work for no gain here; leaky bucket queues requests, which you already rejected.

Default: 100 rps sustained, burst of 200, same for every key. One Lua script per request for atomicity. Tune once we see real partner traffic.

Want me to implement it?
