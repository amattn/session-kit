# Stage 2 (GLM): disposition

Reviewed 6b6250c, cumulative on stage 1b. Route: pi zai/glm-5.3, thinking high, text mode, tools read,grep,find,ls. No Writing Anywhere (prompt-plus-audit under nono). The range b58cc31..6b6250c was given as a saved diff because the route has no shell. Authority coverage: complete. Write audit clean (primary, worktree, review root). Raw output: `review.md`.

GLM confirmed that all stage-1b fixes landed and found nothing they broke.

| ID | Sev | Finding | State | Tag | Evidence checked |
|---|---|---|---|---|---|
| F1 | medium | iteration-4 says the no-skill run was "2 to 3.5 times" longer | accepted-fixed | evidence | Confirmed from its own table: 3.4x, 1.7x, 1.2x. Now "1.2 to 3.4" in summary.md and NOTES. The same summary.md line said "No skill kept 46/46" (the F14 ambiguity); now "The no-skill run" |
| F2 | med-low | The short cut pass skips step 6, the provenance check | accepted-deferred, then ruled | design | Confirmed: short pass was steps 2, 7, 9. Owner chose "a": the short pass is now steps 2, 6, 7, 9 |
| F3 | med-low | A chat reply over two paragraphs matches neither pass | accepted-deferred, then ruled | design | Confirmed: Mode 4 had no tripwire. Owner chose "d": the short pass is the default in every mode; documents, edits, and anything over its tripwire get every step; chat's tripwire is two paragraphs; the script runs only on text in a file |
| F4 | low | HELP.md says the bootstrap writes CLAUDE.md only | accepted-fixed | mechanical | Now "AGENTS.md and/or CLAUDE.md", matching SKILL.md and /start |
| F5 | low | `git show HEAD:<path>` recovers the wrong original when the file has uncommitted changes | accepted-fixed | mechanical | The fallback is now conditioned on a clean file |
| F6 | low | CHANGELOG has no entry for 6b6250c | accepted-deferred | status/canon | The owner held versions until the chain is done; one CHANGELOG entry comes with the final bump |
| N1 | nit | Zero-target list names 25-word sentences, omits 20-word steps | accepted-fixed | mechanical | Now "(20 in a numbered step)" |
| N2 | nit | Cut-pass step 8 says "the mode's anti-patterns"; only Mode 1 has a list by that name | accepted-fixed | mechanical | Now "its mode's rules (Modes 1 to 4)" |

Rejected remark: GLM called itself "a same-family pass". It is not; GLM is the chain's first independent family.
