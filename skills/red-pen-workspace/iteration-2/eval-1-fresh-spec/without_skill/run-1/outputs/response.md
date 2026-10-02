Written to `docs/rate_limiting.md`.

**What it builds on.** NOTES.md already records three decisions from September (state in Redis, 429 + `Retry-After`, keyed per API key), so the plan takes those as settled and spends its space on what is still open.

**What it proposes.**
- Token bucket in Redis via a single Lua script, one key per API key. Chosen because partner traffic is bursty and this lets a legitimate batch through while still capping the average.
- One hardcoded default for all partners: 100 rps sustained, 500 burst. Per your "pick a default and revisit" preference, the only knob is a shadow/enforce switch.
- Fail open if Redis is unreachable, with an alert. If Redis is down the balance cache is down too, and failing closed would turn a blip into a partner outage.
- A week of shadow mode before enforcing, so the default gets checked against real per-key traffic instead of shipped as a guess.

**The two open questions in NOTES.md, each with a recommendation so review can be yes/no:**
- Per-partner limits: not now, but add a nullable override column on the partner record that an engineer can set. No UI, no tiers.
- Mobile: a separate per-user limit (20 rps / 60 burst), phased in after partner limiting. Sharing one bucket across 40k users would recreate the noisy-neighbor problem inside the app.

**For product specifically:** the doc has a short section on what product owns (the partner notice, the stance on tiers, whether the limit is documented publicly) and a rollout table with exit criteria per phase.

Two things I noticed but did not change:
- `docs/design.md` (transaction export) proposes a per-IP in-process counter for export requests. That predates the September decisions and conflicts with them. The plan flags it under Out of scope; worth a one-line fix in that doc so it does not get built separately.
- The plan ends with a list of decisions to add to NOTES.md once approved. I left NOTES.md untouched since nothing is decided yet.

The limit numbers are my proposal, not measurements. Shadow mode is there to correct them before anyone sees a 429.

If it would help to share this with product as a page rather than a repo file, I can publish it as an artifact.
