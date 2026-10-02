# Writing Conventions

These rules apply to all prose in tidewatch: README and docs, code comments and
docstrings, commit messages, PR descriptions, log messages, and the Slack
summaries the service publishes. When in doubt, favor the shorter, plainer
option.

## Voice and tone

- Write in plain, direct English. Prefer short sentences and common words.
- Use the active voice. "The poller retries the request" rather than "The
  request is retried by the poller."
- Address the reader as "you" in docs. Do not use "we" to mean the project.
- No hedging, no filler, no marketing language. Say what something does, not
  how great it is.
- No emojis anywhere, including Slack summaries.

## Terminology

Use these terms consistently; do not introduce synonyms.

| Use              | Not                              |
|------------------|----------------------------------|
| tide gauge       | tide station, sensor, gauge site |
| poller           | fetcher, crawler, scraper        |
| summary          | report, digest, briefing         |
| high tide / low tide | HT / LT, high water / low water |
| station ID       | station id, StationID, site code |

- Write the project name as `tidewatch`, always lowercase, in code and prose.
- Spell out units on first use in a document, then abbreviate: meters (m),
  feet (ft). Never mix unit systems within one summary.

## Formatting

- Markdown for all docs. One `#` title per file, then `##` sections. Do not
  skip heading levels.
- Wrap prose at 80 columns. Do not wrap tables or URLs.
- Use sentence case for headings ("Retry policy", not "Retry Policy").
- Use backticks for file paths, commands, environment variables, identifiers,
  and literal values: `src/poller.py`, `TIDEWATCH_SLACK_WEBHOOK`, `None`.
- Dates are ISO 8601 (`2026-10-01`). Times include a timezone or are stated as
  UTC (`06:42 UTC`). Never use ambiguous formats like `10/1/26`.
- Numbers: use digits, not words, for quantities and measurements. One decimal
  place for tide heights (`1.8 m`), none for counts.
- Lists: use `-` for bullets. Keep items parallel in structure. End items with a
  period only if they are full sentences.

## Code comments and docstrings

- Comments explain why, not what. Delete a comment that restates the code.
- Every public function and class has a docstring. Use the Google style:
  one-line summary, blank line, then `Args:`, `Returns:`, `Raises:` as needed.
- The summary line is imperative and ends with a period: `Fetch the latest
  reading for a station.`
- Mark temporary work with `TODO(name): description`. Do not leave bare `TODO`.

## Commit messages

- Subject line: imperative mood, no trailing period, 50 characters or fewer.
  `Add retry backoff to poller`, not `Added retry backoff.` or `fixes`.
- Optional body after a blank line, wrapped at 72 columns, explaining why the
  change was made and anything non-obvious about how.
- Reference issues at the end of the body (`Fixes #12`), not in the subject.
- One logical change per commit.

## Log messages

- Lowercase, no trailing punctuation, key facts as `key=value` pairs:
  `poll failed station=9414290 attempt=3 status=503`
- Do not log secrets, webhook URLs, or full API responses.
- Use levels consistently: `debug` for per-request detail, `info` for
  lifecycle events, `warning` for recoverable problems, `error` for failures
  that drop data.

## Slack summaries

The daily summary is the project's user-facing output. It is read on phones.

- Lead with the headline fact: the day's high and low tides for each gauge.
- One line per tide event: `Half Moon Bay  high 06:42 UTC  1.8 m`.
- Keep the whole message under 15 lines. If there are more gauges, link to a
  full report instead of growing the message.
- State the data source and the time the summary was generated at the end, in
  one line.
- If data for a gauge is missing or stale, say so explicitly on its line
  (`no data since 2026-09-30 22:00 UTC`). Never omit a gauge silently.
- Use Slack's `mrkdwn`, not Markdown. Bold only the gauge names.

## Checklist before merging prose

- Active voice, no filler.
- Terms match the table above.
- Dates and times are unambiguous.
- Headings in sentence case, no skipped levels.
- Code identifiers in backticks.
