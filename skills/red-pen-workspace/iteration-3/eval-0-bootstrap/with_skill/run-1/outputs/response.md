Added a Writing Conventions section to `CLAUDE.md`: one rule of thumb per output type (spec/plan, code comment, code/diff/commit, chat) plus the shared rules. `CLAUDE.md` had no existing style rules, so nothing was replaced or overridden.

One question: who reads what tidewatch produces? The block currently assumes a single reader, an insider who knows the codebase. The daily Slack summary suggests at least one more, so I'd add this row unless you correct it (the Knows / Decides / Stops at cells are my guess):

| Reader | Knows | Decides | Stops at |
|---|---|---|---|
| Slack channel readers | tides and the gauges, not the code | whether to act on the day's summary | the first line of the summary |

`/red-pen <file>` edits a file or section against these rules, and "too long" or "red-pen this" works mid-conversation.
