# CLAUDE.md

## Project

tidewatch — a small Python service that polls tide-gauge APIs and publishes a daily summary to Slack.

## Key Files

- `src/poller.py` — fetch loop
- `src/summary.py` — summary rendering

## Writing Conventions
<!-- managed by /red-pen -->

**Decide the output type before writing, then write to its rules.** Full rules: /red-pen.

| Output | Rule of thumb |
|---|---|
| Spec / plan / design note | Preamble: who it is for and how to read it; asks go in their own section, not the preamble. `chose A over B because C; revisit if D`. Assumptions as a tick-list, risks as `X breaks if Y`. 300-word budget. |
| Code comment | Only why, an invariant, an external fact, or a deliberate omission. Never restate the code or narrate the session. |
| Code / diff / commit | Smallest diff that does the job. Match repo idioms. No speculative abstraction, no defensive noise, no placeholder stubs. Commit subject `<verb> <what>: <brief description>`; body only for a non-obvious decision. |
| Chat | Answer first. Length matches the question. No restating, no performative phrases. Formatting is rare. One question back at most. |

Everywhere: name the readers and omit what they know. One layer per distinct
stopping point, ordered by who stops first; one reader means answer first. Pace by
uncertainty: settled things get one line. Surface by stakes: record what has no real
alternative, tell in one line what you chose for a reason, ask when a reader owns it,
it is hard to reverse, the blast radius is large, or you guessed. No scaffolding that
carries no information. Checkable beats fluent. Numbers over adjectives. Run a cut
pass before delivering.

Readers (default for code, comments, chat: an insider who knows this codebase and this thread):

| Reader | Knows | Decides | Stops at |
|---|---|---|---|
| maintainer | the codebase, the gauge APIs | implementation, what ships | the end |
| Slack summary readers | the tides, not the code | nothing here; they act on the summary | the first line of the daily post |
