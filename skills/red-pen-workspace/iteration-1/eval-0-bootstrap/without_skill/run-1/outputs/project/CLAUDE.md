# CLAUDE.md

## Project

tidewatch — a small Python service that polls tide-gauge APIs and publishes a daily summary to Slack.

## Key Files

- `src/poller.py` — fetch loop
- `src/summary.py` — summary rendering

## Writing Conventions

All prose in this repo (docs, comments, docstrings, commits, PRs, and the
Slack summary text) follows `docs/WRITING.md`. Read it before writing any
of those. Highlights:

- Plain English, active voice, lead with the point, no emoji.
- Use the terminology table in `docs/WRITING.md` (e.g. "tide gauge",
  "poller", "summary", "reading"); do not introduce synonyms.
- Commit subjects: imperative, under 50 characters, optional area prefix
  (`poller:`, `summary:`, `slack:`, `docs:`).
- Docstrings on all public functions; Google style; comments say *why*.
- Slack summary format is user-facing: follow the template in
  `docs/WRITING.md` and call out any format change in the PR.
