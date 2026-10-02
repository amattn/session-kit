Token bucket, a burst allowance that refills at a fixed rate.

- It caps each partner's average rate, which is what stops a repeat of the 2k rps incident, and still lets a short burst through up to the bucket size.
- Sliding window counter is the pick instead if you want no bursts at all.
- Ruled out: fixed window lets a client send 2x the limit across a window boundary; leaky bucket queues requests, which you already rejected; sliding window log stores a timestamp per request.

Still to pick: bucket size and refill rate. I'll hardcode one default for all partners rather than add a knob. What sustained rate per partner is acceptable?
