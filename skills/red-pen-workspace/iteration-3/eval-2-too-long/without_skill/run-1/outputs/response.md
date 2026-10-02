Token bucket, per API key, in Redis.

It caps a partner's sustained rate, which is what stops a repeat of the 2k rps incident, while still letting short bursts through so normal partner batch calls don't get 429s. One small Lua script per request keeps it atomic across the three replicas.

Starting default, one limit for all partners: 100 rps refill, burst of 200. Those numbers are a guess, since I haven't seen normal partner traffic. Check them against real per-partner peaks before we ship.
