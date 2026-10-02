# CLAUDE.md

## Project

tidewatch — a small Python service that polls tide-gauge APIs and publishes a daily summary to Slack.

## Key Files

- `src/poller.py` — fetch loop
- `src/summary.py` — summary rendering

## Writing Conventions

All prose (docs, comments, docstrings, commit messages, log messages, Slack
summaries) follows `docs/WRITING.md`. Read it before writing or editing any
of these. Key points:

- Plain, direct English; active voice; no emojis.
- Use the terminology table in `docs/WRITING.md` (`tide gauge`, `poller`,
  `summary`); do not introduce synonyms.
- Commit subjects: imperative, no trailing period, 50 chars or fewer.
- Dates ISO 8601; times in UTC or with an explicit timezone.
- Google-style docstrings on every public function and class.
