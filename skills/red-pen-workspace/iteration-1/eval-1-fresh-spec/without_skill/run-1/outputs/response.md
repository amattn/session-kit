Written to `docs/rate_limiting.md`.

The plan builds on the three decisions already in `NOTES.md` (Redis state, 429 + Retry-After, keyed per API key) rather than reopening them, and picks defaults for the two open questions instead of adding config:

- **Token bucket, 100 rps sustained / 200 burst per partner key**, same for all 6 partners. 6 x 100 = 600 rps worst case, well under the 2k rps incident.
- **Mobile app exempt in v1.** It's what we're protecting, not what we're protecting against.
- **Fail open if Redis is down.** A Redis outage shouldn't take down balance serving.
- **Shadow mode first** (log would-be 429s, don't enforce) so we learn partners' real traffic shape before anyone gets rejected, then product notifies partners, then enforce.

It has separate "For product" and "For eng" sections, a metrics list, and a "Decisions this plan makes" list at the end so they can be copied into `NOTES.md` once agreed.

Two things I noticed while writing it:

1. `docs/design.md` (transaction export) proposes a per-IP in-process counter for exports. That contradicts the per-API-key / Redis decisions in `NOTES.md`. The plan flags it; that doc should be updated to use the shared limiter.
2. `CLAUDE.md` points at `src/api/` for route handlers, but that directory isn't in the tree. The plan says where the middleware conceptually goes; exact file paths will need confirming at implementation time.

The 100/200 numbers are a guess without traffic data. That's what the shadow period is for. If you already know a partner's normal rate, tell me and I'll adjust.
