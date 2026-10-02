Token bucket. Partner traffic is bursty (the 2k rps incident), and a bucket lets a partner burst up to the bucket size while the refill rate caps their average; `Retry-After` falls out of the refill rate. Sliding-window counter is the alternative if you'd rather not allow bursts at all.

Implementation is one Redis Lua script per API key: refill, take, or reject in one call.
