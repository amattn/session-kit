Added a Writing Conventions section to CLAUDE.md: the shared core (name the readers, omit what they know, pace by uncertainty, surface by stakes, cut pass) and a one-line rule per output type — spec/plan, code comment, code/diff/commit, chat — with `/red-pen` as the pointer to the full rules. Nothing was there to keep; CLAUDE.md had no style or commit conventions.

One question: who reads what this project produces besides you? I left the reader roster out on the lean that a small service has one reader, the engineer in the thread, which the block already covers. If someone outside engineering reads specs, or the Slack summary wording gets reviewed by whoever consumes it, name them and I'll add rows (what they know, what they decide, where they stop reading).

From here, `/red-pen <file>` edits a file or section against these rules, and "too long" or "red-pen this" mid-conversation re-runs the cut pass on the last reply.
