`WebhookClient.send` in `src/webhook_client.py` now makes up to 3 attempts on 5xx with exponential backoff, and returns `False` on the first 4xx. The signature and `bool` return are unchanged, so call sites need no edits.

I checked it against a stubbed HTTP client (200, 503→200, 503→502→201, 500×3, 404, 429, 302); the repo has no test suite and httpx isn't installed here, so nothing ran against the real library and I added no test file.

Choices you can overrule:

- **429 fails fast**, per your wording. It is the one 4xx that arguably deserves a retry, and ledgerd itself answers rate limits with 429 + `Retry-After`, so partners may too.
- **Timeouts and connection errors are not retried.** They raise out of `send` on the first attempt, as before. You asked for 5xx only; say if you want them in the retry set.
- **Delays are 200ms then 400ms, each with ±50% jitter.** The 200ms base is my pick, as constants rather than config. Jitter is there because a partner outage fails many events at once.
- **The backoff is a blocking `time.sleep`**, so a failing delivery holds its caller for up to ~0.9s on top of the requests themselves.

Commit message:

```
Add retry to webhook client: exponential backoff on 5xx

Mechanics:
- 3 attempts, 200ms base doubling, ±50% jitter
- 4xx fails fast, 429 included; Retry-After not honored
- Timeouts and connection errors still raise, unretried

Design:
- send() still returns bool; call sites unchanged
- Retrying is safe: partners dedupe on event_id
```
