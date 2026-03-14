# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Interaction Conventions

When presenting choices, use a **numbered questions / lettered options** format wrapped in fenced code blocks. Indent lettered options 3 spaces from the number.

Example:
```
1. Which database layer?
   A. SQLite
   B. PostgreSQL
   C. Other — please specify

2. Auth strategy?
   A. JWT
   B. Session cookies
   C. None for now
```

**Shorthands the user may say:**
- **NL** — reformat the last question in numbers-letters style
- **NLR** — same, but include your recommendation and rationale
- **1b1** (or **11**) — walk through items one at a time instead of batching

**Batch answers:** the user can reply with codes like `1A, 2C` to answer multiple questions at once. Re-present only the unanswered items afterward. No answer means the item is still open — never assume approval for items the user didn't address.

**Review prompt:** when presenting work for approval, end with structured options. Use situational choices that fit the context (e.g., Add / Change / Remove), and always close with these two stable options:
- **[second-to-last]. Recommendations** — tell me what you'd suggest
- **[last]. Ok** — approve as-is

**General principles:**
- Always suggest concrete options rather than asking open-ended questions. Options let the user evaluate rather than generate.
- Show your work first, surface concerns, then recommend — before asking for approval.
- When the user's intent is ambiguous, present your best interpretations as lettered options rather than guessing.

## Key Files

- `NOTES.md` — institutional memory
