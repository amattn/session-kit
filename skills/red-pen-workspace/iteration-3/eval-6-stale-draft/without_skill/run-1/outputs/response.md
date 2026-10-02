I rewrote `docs/design.md` in place. The main problem was that it contradicted decisions already recorded in `NOTES.md`. The project isn't a git repo, so there is no diff to review; the changes are listed below.

**Stale claims fixed**

- **Rate limiting:** the draft said the approach "has not yet been decided" and proposed a per-IP counter in process memory. `NOTES.md` decided all three points in September: Redis state, keyed per API key, 429 with `Retry-After`. The section now says exports go through that limiter.
- **Database:** the draft said the database choice for ledgerd "is also still open". ledgerd runs on Postgres, so I removed the sentence.
- **Local filesystem:** the draft listed it as a storage option while noting it doesn't work across replicas. With three replicas it is ruled out, and the doc now says so. Postgres large objects and S3 remain.

**Cuts and restructuring**

- Removed the Overview, which only described the document's own layout.
- Removed unsupported filler: "addressing it is important for partner satisfaction" and "This is a reasonable default".
- Renamed Background to Problem and moved Approach ahead of Rate limiting and Storage.
- "Decide on rate limiting" is gone from Next steps, replaced by the narrower question that is still open.

**Additions**

- One fact from `src/webhook_client.py`: webhook delivery is at-least-once, so a partner may receive the "export ready" event twice.
- An Open questions section for gaps the draft did not address. I did not invent answers to any of them:
  - Storage: Postgres large objects or S3.
  - Whether exports need their own, lower rate limit.
  - The request endpoint and its parameters.
  - How the download URL is authorized.
  - What happens when the job fails or the webhook cannot be delivered.
  - Whether 24 hours is the right expiry.
  - What runs the background job.

Two of my own sentences are inferences rather than facts from the repo, so check them: that Postgres large objects would share the database with balance and transaction queries, and that an export costs far more than a page of `/transactions`.
