# Writing Conventions

These rules apply to everything written in this repo that a person will read:
docs, code comments, docstrings, commit messages, PR descriptions, and the
text tidewatch itself publishes to Slack. When in doubt, favor short, plain,
and specific.

## General style

- Write in plain English. Prefer the common word over the technical one
  unless the technical one is more precise.
- Use active voice and present tense. "The poller retries three times," not
  "Three retries will be attempted by the poller."
- Lead with the point. Put the conclusion or instruction first, then the
  reasoning.
- One idea per sentence. One topic per paragraph.
- Be specific. "Retries after 30s" beats "retries after a short delay."
- Cut filler: "in order to," "basically," "it should be noted that," "simply."
- No emoji in docs, code, commits, or Slack output.
- Spell out acronyms on first use in a document (e.g. "NOAA CO-OPS API").
- Use US spelling.

## Terminology

Use these terms consistently; do not invent synonyms.

| Use              | Not                                  |
|------------------|--------------------------------------|
| tide gauge       | station, sensor, tide station        |
| poll / poller    | fetch loop, scraper, crawler         |
| summary          | report, digest, briefing             |
| reading          | observation, data point, sample      |
| high tide / low tide | high water / low water           |
| tidewatch        | Tidewatch, TideWatch, tide-watch     |

Units: meters for height, 24-hour local time with timezone abbreviation for
times (e.g. `14:32 PDT`). Dates are ISO 8601 (`2026-10-01`).

## Documentation (README, docs/)

- Markdown, ATX headings (`#`), one H1 per file.
- Wrap prose at 80 columns. Do not wrap inside tables or code blocks.
- Sentence case for headings: "Running the poller," not "Running The Poller."
- Use fenced code blocks with a language tag. Show exact commands and exact
  output where it helps.
- Link to source by path in backticks (`src/poller.py`), not by description.
- Keep a document's audience in mind: README is for someone running
  tidewatch; `docs/` is for someone changing it.
- Delete stale docs rather than leaving a "(outdated)" note.

## Code comments and docstrings

- Comments explain *why*, not *what*. If the code needs a comment to say
  what it does, rename or restructure it first.
- Every public function, class, and module gets a docstring. Private helpers
  get one only if the behavior is not obvious from the name and signature.
- Docstring format: one-line summary in the imperative ("Fetch the latest
  reading for a gauge."), blank line, then details if needed. Use Google
  style for `Args:` / `Returns:` / `Raises:` sections.
- Note units and timezones in docstrings for anything that returns a height
  or a timestamp.
- `TODO(name): description` for known gaps. No bare `TODO`, no `FIXME`,
  no `XXX`.
- Do not leave commented-out code.

## Commit messages

- Subject line: imperative, under 50 characters, no trailing period.
  "Add retry backoff to poller," not "Added retry backoff" or "poller fixes."
- Prefix with the area when it helps scanning: `poller:`, `summary:`,
  `slack:`, `docs:`, `ci:`.
- Blank line, then a body if the change needs explanation. The body says
  *why* and anything surprising; the diff already says *what*.
- Wrap the body at 72 columns.
- Reference issues at the end of the body: `Fixes #12`.
- One logical change per commit.

## Pull requests

- Title follows commit subject rules.
- Description has three short sections, in this order:
  - **What** — one or two sentences.
  - **Why** — the problem or motivation.
  - **How to verify** — the exact command or steps a reviewer can run.
- Mention anything that changes the Slack output format, since people
  downstream read it.

## Slack summary output

This is the text tidewatch publishes. It is the most-read thing the project
produces, so it has the tightest rules.

- Start with the date and the gauge name on the first line.
- Then the highs and lows for the day, one per line, time first, then
  height. Example:

  ```
  Tide summary for 2026-10-01 — Point Reyes
  High  04:12 PDT   1.84 m
  Low   10:47 PDT   0.21 m
  High  16:58 PDT   1.62 m
  Low   23:05 PDT   0.40 m
  ```

- If data is missing or stale, say so plainly on its own line:
  `No readings since 09:30 PDT (gauge may be offline).`
  Never silently omit a tide or publish a guess.
- No greetings, sign-offs, or commentary. No emoji.
- Keep the whole message under 15 lines so it reads without expanding.
- Use fixed-width alignment (Slack code block) so columns line up.
- Changes to this format are a user-visible change: call them out in the
  PR and bump the message format note in the README.

## Error and log messages

- Log lines: `<component>: <what happened> (<key=value>, ...)`.
  Example: `poller: request timed out (gauge=9415020, attempt=2/3)`.
- Errors shown to a person say what went wrong and what to do next:
  `Could not reach the gauge API. Check SLACK_WEBHOOK_URL and network access.`
- No stack traces in Slack output.
