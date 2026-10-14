# Stage 1b (Claude, same-host sanity pass): disposition

Reviewed b58cc31. Route: Claude general-purpose subagent, No Writing Anywhere (prompt-plus-audit). Not an independent gate: the lead is also Claude. Authority coverage: complete. Write audit clean.

| ID | Sev | Finding | State | Tag | Evidence checked |
|---|---|---|---|---|---|
| F1 | high | Worked example drops the staleness bound, invents an open item, miscounts openers (3 vs 2), shares ledgerd's 30s invariant | accepted-fixed | mechanical | Confirmed: Before L9 bound absent from After; "parked idea" not in Before; ledgerd NOTES L9. Replaced with a backup-retention text, fact list shown, counts from symptoms.py |
| F2 | high | Fact list comes after the cutting steps | accepted-fixed | mechanical | Confirmed L216-221. Listing is now step 1; survival check step 7 |
| F3 | high | "Default to less; the reader will ask" vs readers who cannot ask and the lost-facts check | accepted-deferred, then ruled | design | Owner ruled the lead's lean on 2026-10-14 ("1 you lean is correct"): "leave it out" means point to where it lives; a fact that lives nowhere else stays. Fixed in v0.3.2 |
| F4 | med-high | Cut-pass step 4 says a missed ask is costlier; § Surface by Stakes and NOTES say doubt goes to tell | accepted-fixed | status/canon | Confirmed vs NOTES L650. Step 5 now checks only that no ask-signal item sits in tell |
| F5a | medium | "No telegraphic fragments" vs commit bullets, PR labels, status example | accepted-fixed | mechanical | Confirmed; the record-style rules predate v0.3.0. Records exempted |
| F5b | medium | "No bold on every lead" vs Mode 4 bold labels | accepted-fixed | mechanical | Bold labels were the owner's v0.2.1 preference; stated as the exception |
| F5c | medium | Precedence: "house style wins" vs "shared core does not get overridden" | accepted-deferred, then ruled | design | Owner chose the lead's lean ("a"): house style, then recorded overrides, then mode, then core |
| F6 | medium | 300-word budget cannot be followed when editing a long section | accepted-deferred, then ruled | design | Confirmed from the iteration-4 run. Owner went further ("a"): no length targets anywhere; targets are symptom counts that reach zero, and 300 words is a tripwire |
| F7 | medium | The Job #2 says "return the edited text and a one-line account" | accepted-fixed | mechanical | Now points at § Editing a target |
| F8a | medium | Cut-pass "first sentence" vs the Mode 1 preamble | accepted-fixed | mechanical | Now "first sentence after any preamble" |
| F8b | medium | Asks "at the start of its owner's layer" vs the preamble ruling | rejected | - | No conflict: the start of a layer comes after the preamble, and the line prescribes no form |
| F9 | medium | Mode Selection routes PR descriptions to Mode 4 | accepted-fixed | mechanical | Routes to Mode 3's PR paragraph |
| F10 | medium | Commit default is the retired verb style | accepted-fixed | status/canon | The ruling quotes "session-kit's commit style"; CLAUDE.md defines it as `<prefix>:`. NOTES L481 corrected |
| F11 | medium | MAR copy-review has no kinds for the sentence rules | accepted-deferred, then ruled | design | Owner chose the lean ("a"): `term-switch` and `over-compressed` added to copy-review.md |
| F12a | low-med | symptoms.py usage: save the original, stdin, How It Fits counts | accepted-fixed | mechanical | `-` already reads stdin (symptoms.py L180); documented |
| F12b | low-med | symptoms.py counts every list item as a step | accepted-deferred, then ruled | design | Owner chose the lean ("a"): numbered items are steps. Also fixed a bug: list items were joined, so unpunctuated bullets ran together |
| F13 | low | Bootstrap block over its "about 250" words | accepted-fixed | mechanical | Was 292 with headings and mode table; now 268 |
| F14 | low | "no skill switched lattice" reads as "none did" | accepted-fixed | evidence | summary.md and NOTES say "the no-skill run" |
| V1 | - | Cut pass (now 10 steps) will be skipped on short chat replies | accepted-deferred, then ruled | design | Owner chose the lean ("a"): chat replies run the short pass, steps 2, 7, and 9 |
