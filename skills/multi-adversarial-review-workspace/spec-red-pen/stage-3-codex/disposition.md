# Stage 3 (Codex): disposition

Reviewed 2025615, cumulative on stages 1b and 2. Route: codex exec, gpt-6-astra, reasoning effort high (pinned; transcript header verified). No Writing Anywhere: `-s danger-full-access` under the confirmed outer sandbox nono, so prompt-plus-audit. Authority coverage: complete. Write audit clean (primary, worktree, review root); the one inline-Python probe only read files. Raw output: `review.md` (final answer only; the review-root path is redacted).

Codex found that the owner rulings landed. It qualified one stage-1b fix (F1) and corrected one stage-2 endorsement (F5).

| ID | Sev | Finding | State | Tag | Evidence checked |
|---|---|---|---|---|---|
| F1 | medium | Cut-pass step 0 says "fix its symptoms" before step 1 lists the facts | accepted-fixed | mechanical | Confirmed: step 0 preceded the fact list, so stage-1b F2 was only half fixed. Step 0 now measures and changes nothing; steps 1 to 9 do the fixing |
| F2 | medium | The Job #3 detects "writing conventions", so a project with only a commit style skips bootstrap | accepted-fixed | mechanical | Confirmed against § Bootstrap step 1. Now detects the managed Writing Conventions block, and other style rules stay |
| F3 | medium | Editing pasted text has no output branch; § Editing a target assumes a file | accepted-deferred, then ruled | design | Confirmed: "red-pen this section" is a listed trigger, and step 3 writes a file and reports its path. Owner ruled: the user copies the result out, so the reply is the edited text in one fence plus one line on anything dropped |
| F4 | low | `symptoms.py` misses numbered steps written `1)` or inside a blockquote | accepted-fixed | mechanical | Confirmed with the same 24-word step: flagged with `1.`, missed with `1)` and `> 1.`. Now blockquote prefixes are stripped and `1)` counts; all three flag, a bullet does not |
| F5 | low | Worked example's opener row says "It is / That is" but the script counts a narrower set; the Before has 4 by the label | accepted-fixed | evidence | Confirmed: "It is simply" is not in the script's list. The row and the cut-pass target now use the script's label, "This is / That is" |

Residual risk, from Codex: no eval shows that a second pass keeps the first pass's facts. PLAN's iteration 5 already lists an idempotence case.
