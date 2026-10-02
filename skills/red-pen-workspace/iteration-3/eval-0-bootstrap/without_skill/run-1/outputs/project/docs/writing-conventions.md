# Writing Conventions

These apply to everything written for tidewatch: docs, the README, code comments, docstrings, commit messages, PR descriptions, and the Slack summaries the service publishes.

They are starting defaults, not a record of existing practice. The project had no prose to derive them from. Change any rule that does not fit, and keep this file current when you do.

## Principles

1. **Lead with the point.** The first sentence says what the reader needs most: the conclusion, the decision, or the action required. Background comes after.
2. **Write for a reader who was not there.** Assume someone arriving cold, months later. Define terms, name things in full, and include the unit, the timezone, and the station.
3. **Be specific.** Give the number, the command, the file path, the error text. "The poller retries 3 times, 30 s apart" beats "the poller retries a few times".
4. **Cut what carries nothing.** Drop preamble, hedges, intensifiers ("very", "simply", "just"), and closing summaries that repeat the body.
5. **One term per thing.** Pick a word and keep it. See the glossary below.

## Style

- Plain, direct English. Short sentences. Active voice where the actor matters.
- Present tense for how the system behaves ("the poller fetches"), imperative for instructions ("run", "set").
- Sentence case for headings. No trailing punctuation in headings.
- No emojis in docs, comments, or commit messages.
- Spell out an abbreviation on first use, unless it is in the glossary.
- Prose for reasoning, lists for parallel items, tables for comparisons. Do not break a chain of reasoning into bullets.

## Formatting

- Markdown for all docs. One sentence or one paragraph per line; do not hard-wrap.
- Backticks for anything the reader might type or search for: file paths, commands, function names, config keys, environment variables.
- Fenced code blocks with a language tag (`python`, `sh`, `json`).
- Relative links between files in the repo.

## Data and units

Tide data is easy to misread, so be explicit every time.

- **Times:** ISO 8601 with an offset or `Z` in docs, logs, and code (`2026-10-02T14:30:00Z`). Store and compute in UTC. In Slack summaries, show the station's local time and name the timezone.
- **Heights:** always give the unit and the datum (`1.82 m above MLLW`). Never a bare number.
- **Units:** SI, with a space between number and unit (`30 s`, `1.8 m`). Convert at the display edge only.
- **Stations:** name plus ID on first mention (`Seattle (9447130)`), name alone after that.

## Glossary

| Use | Meaning | Not |
| --- | --- | --- |
| station | A physical tide gauge with an ID | sensor, site, gauge |
| reading | One observed water level at one time | sample, data point, measurement |
| poll | One fetch cycle against a tide-gauge API | scrape, pull, sync |
| summary | The daily message published to Slack | report, digest, post |

Add a row when a new term appears in more than one place.

## Code comments and docstrings

- Comment the why, not the what. If the code needs a comment to explain what it does, rename or restructure first.
- Every public function and module has a docstring. The first line is a one-sentence summary in the imperative ("Fetch readings for a station."). Document arguments, return value, and raised exceptions when they are not obvious from the signature and type hints.
- `TODO` comments say what is needed and why, and link an issue if one exists.
- Delete commented-out code. Version control keeps it.

## Commit messages

- Subject line: imperative mood, 72 characters or fewer, no trailing period ("Add retry backoff to poller").
- Blank line, then a body when the change needs one. The body explains why the change was made and anything a reviewer would not see in the diff.
- One logical change per commit.

## Pull requests

- Title follows the commit subject rules.
- Description covers what changed, why, and how it was tested. Call out anything risky or anything deliberately left out.

## Slack summaries

These are the project's user-facing writing. Readers see them in passing, in a busy channel.

- The first line stands alone: date, station, and the day's headline figures.
- Keep it scannable. One line per high or low tide; no paragraphs.
- Local time with timezone, heights with unit and datum, as above.
- State problems plainly. If data is missing or stale, say which station and since when; do not publish a summary that looks complete when it is not.
- Same structure every day, so a change in the data stands out.

## Error and log messages

- Say what happened, to what, and what happens next: `Fetch failed for station 9447130 (HTTP 503); retrying in 30 s`.
- Include identifiers and values a person would need to investigate.
- No blame, no jokes, no exclamation marks.

## Checklist before publishing

- Does the first sentence carry the point?
- Would someone new to the project follow it without asking a question?
- Does every time have a timezone and every height a unit and datum?
- Are the terms the ones in the glossary?
- Can anything be deleted without losing meaning?
