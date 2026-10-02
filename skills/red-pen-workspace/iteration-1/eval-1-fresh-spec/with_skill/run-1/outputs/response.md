Written to `docs/rate_limiting.md`, 348 words. It's over the 300 default because the one product-owned question got its own section.

That question: is v1 partners-only, with one shared limit? I lean yes and leave mobile unlimited; the incident was partner traffic and you asked for a default, not knobs.

What I chose, one line each so you can overrule: token bucket (partners batch-sync, bursts should pass); 100 rps sustained / burst 200 per API key, 20x under the 2k rps incident; log-only for a week before enforcing, so the number becomes a measurement; fail open if Redis is down.

One assumption to verify before enforcing: the mobile app authenticates per user and does not sit behind a single shared API key. If it does, 40k users share one bucket.

Also, `docs/design.md` still proposes a per-IP in-process counter for export, which contradicts NOTES.md. The plan flags it as stale; I didn't edit it.
