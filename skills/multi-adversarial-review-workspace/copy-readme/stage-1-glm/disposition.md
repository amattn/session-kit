# Stage 1 disposition: GLM 5.3 via Pi, copy target

Reviewed: README.md at 3c81a3f. Lenses: reader-evaluator, reader-user, each with the record lens. Capability: No Writing Anywhere; write audit clean on the primary checkout and the worktree. Both reviewers reported full authority coverage. Every finding below was verified against the files before disposition.

| ID | Finding | Kind | Disposition |
|---|---|---|---|
| E-F1, U-F1 | Intro says "500+ sessions"; NOTES.md and the README's own Origin say "hundreds". "8+ parts" in Origin is unsourced too. | unsourced | `accepted-deferred`, tag `meaning`. A number is the owner's. Home: owner question 1. |
| E-F2 | Table row for /fast-chat uses "R/O stable tail" before R and O are defined. | undefined | `accepted-fixed`, tag `gloss`. The row now says what R and O are. |
| E-F3 | No guidance on which skill to try first; the record holds a usage ranking. | buried | `accepted-deferred`, tag `meaning`. Positioning is the owner's. Home: owner question 2. |
| E-F4, U-F6 | README lists the /notes sections in the current order; `skills/notes/HELP.md` still had the old one. | stale | `accepted-fixed`, tag `stale`. HELP.md corrected to match the README and the recorded decision; /notes v0.1.3. |
| U-F2 | How to Use sits about 300 lines down and table rows were not links. | no-route | `accepted-fixed`, tag `reorder`. Each skill name in the table links to its How to Use entry. |
| U-F3 | The /stable-label guarantee appears in the table, The Skills, and How They Fit Together. | restated | `rejected`. The table is the summary layer and the section is its detail; a rule in a summary and again in its detail is one rule in two layers, which is how a reader who stops at the table and a reader who reads on are both served. |
| U-F4 | "Pi (or cn / OpenCode)" names tools the reader was never given. | undefined | `accepted-fixed`, tag `gloss`. Glossed in README and in the skill's HELP.md. |
| U-F5 | "(Renamed from /sharpen.)" is history inside the lookup table. | history | `accepted-fixed`, tag `cut`. Removed from the table row; the rename stays in the skill's section and its HELP.md. |

Strong, from both reviewers, to preserve: the title to table to install path; the "What it adds over baseline Claude" paragraphs with their hedging; one command per fenced block; the uniform Setup / Ongoing / Example shape; the "Best for" lines.

Readiness after this stage: evaluator needs the owner's answer on the session count; user is ready.

Owner questions:
1. Session count: "500+" in the intro versus "hundreds" in Origin and NOTES.md, and the unsourced "8+ parts".
2. Whether the README should say which skill to start with.
