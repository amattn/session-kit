`WebhookClient.send` now makes up to 3 attempts when the partner returns a 5xx and returns immediately on anything else. The change is confined to `src/webhook_client.py`, and `send` still returns a bool.

I could not run it against real `httpx` because it isn't installed in this environment. I checked the retry logic with a stubbed HTTP client instead: the 5xx, 4xx and success sequences I tried all produced the expected number of calls and sleeps. There are no tests in the repo and I didn't add any.

- **Backoff:** the wait before the second attempt is a random 0–0.5s, and before the third a random 0–1s. The jitter is there so the three replicas don't retry a struggling partner in step. The two constants sit at the top of the module rather than in config.
- **Timeouts and connection errors are not retried.** They raise out of `send` exactly as before, since you asked for 5xx only. A partner that is down hard usually shows up as a timeout rather than a 5xx, so say if you want those retried too.
- **429 fails fast**, along with every other 4xx.
- **`send` can now block longer.** The worst case is about 16.5s (three 5s timeouts plus up to 1.5s of sleep), up from 5s. That matters if anything calls it from a request handler.

Commit message:

```
Retry webhook delivery on 5xx with exponential backoff

WebhookClient.send now makes up to 3 attempts when the partner
endpoint returns a 5xx, sleeping a random 0-0.5s before the second
attempt and 0-1s before the third. The jitter keeps replicas from
retrying the same partner in step.

Any non-5xx response ends the loop at once: 2xx returns True, 3xx and
4xx (including 429) return False without a retry. If all three
attempts get a 5xx, send returns False.

Timeouts and connection errors are not retried and still raise, as
before. A send that hits three slow 5xx responses can now block for
about 16.5s instead of 5s.
```
