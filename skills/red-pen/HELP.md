# /red-pen — Quick Reference

**Setup:** Run `/red-pen` in your project. It adds a Writing Conventions section to CLAUDE.md: the shared core (know the reader, omit what they know, pace by uncertainty, checkable over fluent) a one-line rule of thumb per output type — spec/plan, code comment, code/diff/commit, chat — and a reader roster (who reads this project's output, what they know, what they decide, where they stop reading).

**Ongoing:** Always-on — no invocation needed. Before writing anything, the agent decides which output type it is producing, writes to that type's rules, and runs a cut pass before delivering. Your side:
- Say `red-pen this` or `/red-pen <file>` to edit a file or section against the rules — the file is edited and you get a short report: what was found, one before/after paragraph, and a small symptom table
- Say `too long` or `too wordy` — the agent re-runs the cut pass on its last output and resends, no explanation
- Sentences stay short (about 20 words in steps, 25 elsewhere), active, and consistent in their terms, borrowed from Simplified Technical English at about 80% strength; every cut is checked for lost facts
- Ask for a plan, spec, or design note — it opens with a preamble saying who it's for and how to read it, then what it needs from you, not an overview
- Override a default for the project (a bigger spec budget, a different reader) — it's recorded in the Writing Conventions block, and so is any cut you reject, so the next pass starts calibrated
- The report after an edit is by symptom, not word count: `scripts/symptoms.py --compare before.md after.md` counts restated phrases, "This is / That is" openers, bold leads, dated markers, and header density

**Example — editing a target:**
```
You: /red-pen docs/caching-design.md
Agent: Wrote docs/caching-design.md. Every rule and anchor is preserved.
       One stale claim found: the doc calls the cache backend undecided,
       and NOTES.md settled it.

       Here is one paragraph before and after, as an example of the change:
       [the before paragraph]
       [the after paragraph]

       | Symptom                          | Before  | After |
       | The same rule stated             | 4 times | once  |
       | Overview and Next Steps sections | 2       | 0     |
```

**Example — always-on, a plan request:**
```
You: write up a plan for the rate limiter
Agent: This plan is for you as the one approving the limiter design;
       it assumes the context in issue #41.

       One decision is yours: per-user token bucket or global sliding
       window. I lean per-user, because the noisy-neighbor complaint is
       why this exists; revisit if we add tenant-level quotas.

       Assumptions:
       - [ ] Redis is already in the deploy (it is, per docker-compose)
       - [ ] 429 with Retry-After is acceptable to the mobile client

       Risks:
       - Bucket state could drift if Redis fails over mid-refill.

       Scope out: no admin UI for limits, no per-endpoint overrides.
```
