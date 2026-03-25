# /fast-chat — Quick Reference

**Setup:** Run `/fast-chat` in your project. It adds an Interaction Conventions section to CLAUDE.md with the NL/NLR/1b1 shorthands, batch answer format, and the standard review prompt.

**Ongoing:** Always-on — no invocation needed. The agent presents choices as numbered questions with lettered options and uses the review prompt (R/O tail) for approvals. Your side:
- Answer with batch codes: `1A, 2B, 3ok`
- Say `NL` to reformat a question as numbered-letters options
- Say `NLR` for options with the agent's recommendation marked
- Say `1b1` to discuss items one at a time instead of batching
- Say `R` during a review to get NL-formatted recommendations
- Say `O` to approve — implicitly accepts any simple displayed rec
- Just type instructions (add/change/remove) — no prefix needed
- Unanswered items stay open — silence is never treated as approval

**Example — review flow:**
```
Agent: [presents section for review]

   R. Show me recommendations
   O. Ok, approve

You: fix the typo in paragraph 2
Agent: [fixes typo, re-presents section]

   R. Show me recommendations
   O. Ok, approve

You: R
Agent: 1. Edge case handling
          A. Add a note about edge cases
          B. Skip for now
       2. Examples section
          A. Expand with more examples
          B. Keep as-is

You: 1A, 2B, O
```

**Example — batch decisions:**
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

You: 1A, 2B
```
