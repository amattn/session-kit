I set up writing conventions for tidewatch. The project had only a `CLAUDE.md` and no source files yet, so I wrote the conventions around the kinds of text this project will produce rather than around existing code.

**Created `docs/WRITING.md`** — the full conventions doc, covering:

- **General style** — plain English, active voice, lead with the point, be specific, no filler, no emoji, US spelling.
- **Terminology table** — one canonical term each for "tide gauge", "poller", "summary", "reading", "high/low tide", "tidewatch", with the synonyms to avoid. Also fixes units (meters), time format (24-hour with tz abbreviation), and dates (ISO 8601).
- **Documentation** — Markdown/ATX headings, sentence-case headings, 80-column wrap, fenced code blocks with language tags, link to source by path, delete stale docs instead of marking them outdated.
- **Code comments and docstrings** — comments explain *why*; docstrings on all public functions/classes/modules, Google style, imperative one-line summary; note units and timezones; `TODO(name):` only; no commented-out code.
- **Commit messages** — imperative subject under 50 chars, optional area prefix (`poller:`, `summary:`, `slack:`, `docs:`, `ci:`), body wrapped at 72 explaining why, `Fixes #N` at the end, one logical change per commit.
- **Pull requests** — title follows commit rules; What / Why / How to verify sections; flag any change to the Slack output format.
- **Slack summary output** — the strictest section, since this is the most-read thing the project produces: a fixed template (date and gauge on line one, then one line per high/low with time then height), explicit "no readings since…" line when data is missing, no greetings or commentary, under 15 lines, fixed-width code block.
- **Error and log messages** — `component: what happened (key=value, ...)` for logs; user-facing errors say what went wrong and what to do next; no stack traces in Slack.

**Updated `CLAUDE.md`** — added a "Writing Conventions" section that points to `docs/WRITING.md` and lists the highlights (style, terminology, commit format, docstrings, Slack template), so future sessions apply them without being told.

A few of the specifics (meters vs. feet, the exact Slack layout, the commit prefixes) are reasonable defaults rather than things I could derive from the code — adjust them in `docs/WRITING.md` if your team already does it differently, and the `CLAUDE.md` summary will still point to the right place.
