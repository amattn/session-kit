# CLAUDE.md

## Project

tidewatch — a small Python service that polls tide-gauge APIs and publishes a daily summary to Slack.

## Key Files

- `src/poller.py` — fetch loop
- `src/summary.py` — summary rendering
- `docs/writing-conventions.md` — writing conventions for docs, comments, commits, and Slack summaries

## Writing

Follow `docs/writing-conventions.md` for all prose: docs, comments, docstrings, commit messages, PR descriptions, and Slack summary text. The essentials:

- Lead with the point; write for a reader arriving cold.
- Be specific: numbers, commands, paths, exact error text.
- Times in ISO 8601 with a timezone; heights with a unit and datum.
- Use the glossary terms: station, reading, poll, summary.
- Sentence-case headings, no emojis, no filler.
