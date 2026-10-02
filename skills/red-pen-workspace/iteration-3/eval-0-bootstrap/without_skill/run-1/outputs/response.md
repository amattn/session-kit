I added a writing conventions guide at `docs/writing-conventions.md` and pointed `CLAUDE.md` at it, with a short summary of the essentials so they apply in every session.

The project had no existing prose beyond `CLAUDE.md`, so these are my proposed defaults rather than a record of how you already write. The guide covers:

- **General style:** lead with the point, write for a reader arriving cold, be specific, cut filler, sentence-case headings, no emojis.
- **Data and units:** ISO 8601 times with a timezone, heights with unit and datum, SI units, station name plus ID on first mention.
- **Glossary:** one term per thing (station, reading, poll, summary).
- **Per-surface rules:** code comments and docstrings, commit messages, pull requests, Slack summaries, and error and log messages.
- **A short checklist** to run before publishing.

Some of the choices are guesses on my part, so please check these:

- **Units and datum:** I assumed metric and used MLLW in the examples.
- **Glossary terms:** I picked the four terms and their rejected synonyms from the project description, not from your code.
- **Commit format:** I chose plain imperative subjects, not Conventional Commits.
- **Location:** the guide lives in `docs/`, which did not exist before.

Nothing enforces these rules yet; there is no linter or hook. Tell me if you want any of the choices above changed or want enforcement added.
