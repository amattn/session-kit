I set up writing conventions for tidewatch. The project had only a `CLAUDE.md`, so there was nothing existing to derive conventions from; I wrote a concrete set tailored to what the service does (a Python poller that publishes Slack summaries).

**Created `docs/WRITING.md`** covering:

- **Voice and tone** — plain English, active voice, "you" for the reader, no filler, no emojis.
- **Terminology** — a use/not table so the same thing is always called the same name (`tide gauge` not station/sensor, `poller` not fetcher, `summary` not report/digest), `tidewatch` always lowercase, unit handling.
- **Formatting** — Markdown structure, sentence-case headings, 80-column wrap, backticks for identifiers, ISO 8601 dates, times in UTC or with an explicit zone, one decimal place for tide heights.
- **Code comments and docstrings** — comments explain why, Google-style docstrings on every public function/class, `TODO(name):` form.
- **Commit messages** — imperative subject, 50 chars or fewer, no trailing period, 72-column body, issue refs in the body.
- **Log messages** — lowercase `key=value` style, no secrets, consistent level usage.
- **Slack summaries** — since that's the user-facing output: headline tides first, one line per event, under 15 lines, explicit "no data" lines for missing gauges, `mrkdwn` not Markdown.
- A short pre-merge checklist.

**Updated `CLAUDE.md`** with a "Writing Conventions" section that points to `docs/WRITING.md` and lists the five rules most likely to matter in day-to-day edits, so they're applied without needing to open the full doc each time.

A couple of choices you may want to adjust: I picked Google-style docstrings and UTC-first times as defaults; if the team prefers NumPy/reST docstrings or local-time summaries, those are one-line changes in `docs/WRITING.md`.
