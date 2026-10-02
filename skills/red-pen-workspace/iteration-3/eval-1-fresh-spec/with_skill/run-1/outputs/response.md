The plan is in `docs/rate_limiting.md`. It needs three decisions from product before enforcement, each with my lean:

- **The partner limit.** I put 100 rps per API key with bursts to 200, but that is a guess: the only traffic number on record is the 2k rps incident. The plan runs log-only first so a measured number replaces it.
- **Whether the mobile app is limited.** Lean: exempt in v1.
- **One limit for all partners or per-partner quotas.** Lean: one limit.

Choices I made that you can overrule: token bucket for the algorithm, requests pass through if Redis is unreachable, and limits are hardcoded rather than configurable.

The Redis, 429 + `Retry-After`, and per-API-key decisions from NOTES.md are taken as settled. `docs/design.md` contradicts them (its "Rate limiting" section proposes a per-IP in-process counter); I left that file alone.

The doc runs about 415 words against a 300-word norm because of the open items, and says so in its first line.
