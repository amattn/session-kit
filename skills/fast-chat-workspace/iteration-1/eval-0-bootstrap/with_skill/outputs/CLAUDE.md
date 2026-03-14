# CLAUDE.md

## Project

inventory-api — REST API for managing inventory.

## Key Files

- `NOTES.md` — institutional memory

## Interaction Conventions
<!-- managed by /fast-chat -->

Use **numbers-letters style** when presenting choices — numbered questions, lettered
options, wrapped in fenced code blocks. Indent options 3 spaces from the number.

Shorthands:
- **NL** — reformat the most recent query in numbers-letters style
- **NLR** — numbers-letters with your recommendations
- **1b1** or **11** — discuss items one by one instead of batching

Batch answers: "1A, 2C, 3ok" — re-present with only unanswered items.
No answer = still open. Never assume approval.

When reviewing, use the standard review prompt: situational options adapted to
context, followed by Recommendations and Ok as the stable tail.
Always suggest concrete options — never ask open-ended questions when options are possible.
