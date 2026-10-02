# Stage 2 disposition: Codex, copy target

Reviewed: README.md at be4d8f6, cumulative on the stage 1 disposition. Route: codex exec, model gpt-6-astra, reasoning effort high (CLI defaults, read from the transcript header). Lenses: reader-evaluator, reader-user, each with the record lens. Capability: No Writing Anywhere; write audit clean. Both reviewers reported full authority coverage. Every finding was verified against the files.

Codex upheld the stage 1 fixes and the one rejection, and corrected one stage 1 statement: "hundreds" does not contradict "500+", it only fails to support it.

| ID | Finding | Kind | Disposition |
|---|---|---|---|
| E-F1 | Install options 2 and 3 use `skills/*`, which also copies every `*-workspace` directory. | no-route | `accepted-deferred`, tag `meaning`. Verified. The install scope is the owner's. Home: owner question 3. |
| E-F2, U-F6 | The /dictation example corrects "Maine" to "main" silently; the record says to confirm when a correction changes the action, with this example. | stale | `accepted-deferred`, tag `meaning`. The example says "the Maine branch", which may be the unambiguous case. Home: owner question 4. |
| E-F3 | What installing activates, and /mar's reviewer prerequisite, appear only after the install decision. | buried | `accepted-fixed`, tag `reorder`. Two sentences at the top of Install. |
| E-F4, U-F5 | "Each skill has a one-time setup" contradicts /mar's "Nothing to bootstrap". | stale | `accepted-fixed`, tag `stale`. The sentence now says most, and names the exception. |
| E-F5, U-F9 | "500+ sessions" and "8+ parts". | unsourced | "500+": `accepted-fixed` on the owner's ruling (now "hundreds"). "8+ parts": `accepted-deferred`. Home: owner question 5. |
| E-F6 | Which skill first. | buried | `accepted-deferred`. The owner chose to reorder the table; the order and its scope are owner question 1. |
| E-F7, U-F8 | The /fast-chat review example answers R with a numbered list and no lettered options; the record and the skill's HELP.md require options. | stale | `accepted-fixed`, tag `stale`. README example now matches HELP.md. |
| E-F8 | /notes: "most common failure mode", "nearly impossible", "same sections every project". | unsourced | `accepted-deferred`, tag `meaning`. Home: owner question 6. |
| E-F9, U-F3 | Bare `grep REQ_3` has no file operand. | unsourced | `accepted-fixed`, tag `gloss`. The prose now gives a project-wide search. The transcript-style example keeps the shorthand. |
| E-F10, U-F7 | The /red-pen example leads with a word count and has no before/after pair, against the skill's current report shape. | stale | `accepted-fixed`, tag `stale`. Example replaced in README and HELP.md; /red-pen v0.2.3. |
| E-F11 | /red-pen table row: "for the editing cost generated text never pays". | argument-first | `accepted-fixed`, tag `cut`. The rationale stays in the section. |
| U-F1 | `references/routes.md` named but not linked. | no-route | `accepted-fixed`, tag `gloss`. Linked. |
| U-F2 | "you disposition every finding": unclear whether you or the agent. | undefined | `accepted-fixed`, tag `gloss`. Now "the lead (your agent, with you ruling on anything contested)". |
| U-F4 | The /stable-label example turns "under 200ms" into "within 200ms (p95)". | unsourced | `accepted-deferred`, tag `meaning`. Home: owner question 7. |
| U-F10 | Install option 3 puts two commands in one fence, against the recorded convention. | scaffolding | `accepted-fixed`, tag `mechanical`. Split. Stage 1's claim that the convention was followed was only partly true. |

Readiness after this stage: the user reader is ready for the /stable-label and /mar lookups. The evaluator is ready once the owner rules on the install scope.
