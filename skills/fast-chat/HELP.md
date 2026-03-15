# /fast-chat — Quick Reference

**Setup:** Run `/fast-chat` in your project. It adds an Interaction Conventions section to CLAUDE.md with the NL/NLR/1b1 shorthands, batch answer format, and the standard review prompt.

**Ongoing:** Always-on — no invocation needed. The agent presents choices as numbered questions with lettered options and uses the review prompt (situational options + Recommendations + Ok) for approvals. Your side:
- Answer with batch codes: `1A, 2B, 3ok`
- Say `NL` to reformat a question as numbered-letters options
- Say `NLR` for options with the agent's recommendation marked
- Say `1b1` to discuss items one at a time instead of batching
- Unanswered items stay open — silence is never treated as approval

**Example:**
```
Agent: A few decisions needed:
       1. Database engine?
          A. SQLite
          B. PostgreSQL ← recommended
          C. Other
       2. Auth strategy?
          A. JWT
          B. Session cookies
          C. Other
       3. Rate limiting?
          A. Per-user token bucket
          B. Global sliding window
          C. Skip for now
       4. Logging format?
          A. Structured JSON
          B. Plain text
          C. Other

You: 1A, 2B, 3 do you have any recommendations, 4 defer till later
Agent: For 3, I'd recommend A (per-user token bucket) — it prevents
       noisy-neighbor problems without penalizing well-behaved users.
       Noted 4 as still open. Applied 1A and 2B.
```
