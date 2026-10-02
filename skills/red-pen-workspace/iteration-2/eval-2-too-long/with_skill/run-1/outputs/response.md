Token bucket. One bucket per API key in Redis, refilled at the sustained rate you allow, with bucket size as the burst cap; a partner at 2k rps drains its bucket and gets 429s until it refills. Do refill-and-take in one Lua script so the three replicas don't race.

Sliding window counter is the alternative if you don't want to allow bursts at all. Fixed window isn't worth it: a partner can send 2x the limit across a window boundary.

The remaining call is bucket size and refill rate. What does a well-behaved partner peak at? That's the number I need to propose a default.
