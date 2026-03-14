For an inventory API, here are the practical options:

```
A. UTC everywhere
   - Store, transmit, and log in UTC
   - Clients convert to local time for display
   - No ambiguity across time zones or DST transitions

B. UTC for storage, ISO 8601 with offset for API responses
   - Store in UTC internally
   - API responses include offset (e.g., 2026-03-14T10:00:00-07:00)
   - Clients get timezone-aware timestamps without extra work

C. Server-local time zone
   - Timestamps match wherever the server runs
   - Breaks if you move regions or run multi-region

D. Recommendations — tell me what you'd suggest
E. Ok — approve as-is
```

Recommendation: **A.** UTC everywhere is the standard for APIs. It eliminates DST bugs, works cleanly across regions, and every HTTP/REST convention assumes it. Let clients handle display formatting — that's a UI concern, not an API concern. B adds complexity without real benefit for an inventory system where "what time zone is the user in?" isn't something the backend should need to know.
