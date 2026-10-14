# Iteration 4: fact retention under the v0.3.0 sentence rules

One run per configuration. Facts enumerated before the runs; graded by an independent agent per case.

| Case | Config | Facts kept | Words | Avg sentence | Prose sentences >25 words |
|---|---|---|---|---|---|
| explain-code | new_skill | 15/15 | 315 | 14.7 | 0 |
| explain-code | old_skill | 15/15 | 334 | 18.3 | 0 |
| explain-code | without_skill | 15/15 | 1076 | 11.6 | 0 |
| explain-notes | new_skill | 10/11 | 289 | 13.5 | 1 |
| explain-notes | old_skill | 10/11 | 226 | 17.2 | 1 |
| explain-notes | without_skill | 11/11 | 493 | 14.3 | 1 |
| edit-target | new_skill | 20/20 | 1343 | 16.6 | 5 |
| edit-target | old_skill | 20/20 | 1092 | 19.9 | 7 |
| edit-target | without_skill | 20/20 | 1623 | 19.6 | 15 |

| Config | Facts kept, all cases |
|---|---|
| new_skill | 45/46 |
| old_skill | 45/46 |
| without_skill | 46/46 |

Findings:
- The sentence rules lost no facts relative to v0.2.5: 45/46 for both. The one miss, shared by both skill versions, is the 30-second balance invariant when explaining rate-limiting decisions; arguably out of scope for that question, but it is on the list.
- On the section edit all three kept 20/20 facts; the difference was meaning drift. v0.3.0 had none; v0.2.5 had two small meaning changes; the no-skill run added unsupported claims and switched "lattice" to "grid", the term-switch failure the new one-term-per-concept rule targets.
- No skill kept 46/46 but was 2 to 3.5 times longer and added claims the source does not support in two of three cases.
- Limits: one run each, fact lists written by the skill author, graders from the same model family. The explain-code case does not discriminate (15/15 everywhere).
