Done in `src/webhook_client.py` (+11 lines). `send()` now posts up to 3 times on 5xx, sleeping 0.2s then 0.4s between attempts; a 4xx returns False on the first response. 2xx/3xx handling and transport errors (still raise) are unchanged.

Two calls you can overrule:
- Worst case `send()` now blocks ~15.6s (3 × 5s timeout + 0.6s backoff). Fine from a background job; not fine inline in a request handler — I couldn't see the call sites in this checkout.
- No jitter, no constructor knobs. Attempts and base delay are module constants, per "pick a default and we'll revisit" in NOTES.md.

No test suite in the repo, so I verified the six paths (2xx, 3xx, 4xx, 5xx→2xx, 5xx→4xx, 5xx×3) with a scratch script against `httpx.MockTransport`; a `tests/test_webhook_client.py` from that is a natural follow-up.

Commit message:

```
Add retry to WebhookClient.send: exponential backoff on 5xx

Mechanics:
- 3 attempts, 0.2s base, doubling (sleeps 0.2s, 0.4s)
- 4xx returns False on first response — identical resend gets the same answer
- 3xx and transport errors unchanged (False / raise)

Design:
- Attempts and base delay are module constants, not constructor args — "pick a default and we'll revisit" (NOTES.md)
- No jitter: 6 partner endpoints and 3 replicas is too few senders to stampede
```
