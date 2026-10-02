Added a Writing Conventions block to CLAUDE.md (marked `<!-- managed by /red-pen -->`): a rule of thumb per output type — spec/plan, code comment, code/diff/commit, chat — plus the shared core, with /red-pen as the pointer for the full rules. CLAUDE.md had no existing style or commit conventions, so nothing needed merging.

One question: who reads what this project produces? I seeded the roster with two rows from the project description — you as maintainer, and the people reading the daily Slack post (they know tides, not code, and stop at the first line). If the only reader is you, I'll drop the table; if there's an on-call rotation or a product owner, name them and I'll add rows.

`/red-pen <file>` edits a file or section against these rules; "too long" or "red-pen this" works mid-conversation.
