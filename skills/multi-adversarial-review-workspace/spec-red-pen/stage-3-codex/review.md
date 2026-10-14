Authority coverage: complete. Read these repository-relative files, except the absolute snapshot path:

- `skills/red-pen/SKILL.md` in full; `HELP.md`; `references/worked_example.md`; `scripts/symptoms.py`.
- `CLAUDE.md`; `CHANGELOG.md`; `NOTES.md`—every heading mentioning `/red-pen`, plus “Important Concepts & Insights.”
- `skills/multi-adversarial-review/references/copy-review.md`; `skills/start/SKILL.md`.
- `skills/red-pen-workspace/iteration-4/summary.md`.
- `skills/multi-adversarial-review-workspace/spec-red-pen/stage-1b-claude/disposition.md`; `stage-2-glm/review.md`; `stage-2-glm/disposition.md`.
- `<review-root>/authority/WRITING_DIRECTIVES.md`.

Checked the recent history and fixes across `b58cc31..2025615`. Read-only probes; checkout remains clean.

**Overall assessment**

The owner rulings landed, and most prior fixes hold. Five remaining issues affect execution or evidence. One qualifies stage 1’s fact-list fix; another corrects stage 2’s endorsement of the worked-example counts. The CHANGELOG deferral remains authorized.

**Strong**

- Precedence, omission-with-a-pointer, and enumeration protections now express the settled rulings consistently.
- The short/full pass selection and provenance check match stage 2’s decision.
- `/start` and MAR’s added finding kinds match their contracts. The eval summary reports the corrected ratios and meaningful limitations.

**Needs work**

- **F1 — Medium: step 0 still permits cutting before the fact inventory.**  
  Evidence: `skills/red-pen/SKILL.md:219` says “Fix its symptoms, then deliver”; step 1 at line 220 subsequently says “Before cutting anything, list the facts.” Following numbered order defeats the safeguard that stage 1 F2 marked fixed. **Change:** make step 0 measurement-only; put repair and delivery after inventory and fidelity checks. This preserves the owner’s pass-selection rule.

- **F2 — Medium: existing style rules can prevent bootstrap without providing a block to adjust.**  
  Evidence: `SKILL.md:28` branches on whether *writing conventions exist*, then requires showing “the current block.” But `SKILL.md:238` explicitly anticipates existing commit/comment conventions and says bootstrap complements them. A project with only “use conventional commits” satisfies the first branch but has no Writing Conventions block. **Change:** distinguish an existing red-pen block from partial project conventions; preserve the latter while adding the missing block.

- **F3 — Medium: editing pasted text has no executable output branch.**  
  Evidence: `SKILL.md:27` supports “red-pen this section,” while lines 285–293 require writing a file and reporting its path. For pasted prose with no destination, the agent must invent a file, ask an otherwise unnecessary question, or violate the prescribed report. The separate “too long” resend rule does not cover every inline invocation. **Change:** define inline targets explicitly: return their edited text in chat; reserve the file report for file-backed targets.

- **F4 — Low: valid numbered steps silently evade the 20-word counter.**  
  Evidence: `scripts/symptoms.py:88` recognizes only `1.`-style markers. In a read-only probe, the same 24-word instruction produced `long_steps=1` with `1.`, but zero long-step and long-sentence counts with `1)` or `> 1.`. That contradicts the numbered-item rule at `SKILL.md:68`. **Change:** normalize blockquote prefixes and recognize both ordered-list delimiters before classifying steps.

- **F5 — Low: the worked example’s opener count is mislabeled.**  
  Evidence: `references/worked_example.md:40` reports three sentences opening “It is / That is,” but its Before contains four. `scripts/symptoms.py:20` counts “It is worth” while excluding “It is simply,” explaining the discrepancy. Stage 2 verified the regex result, not the displayed metric. **Change:** report four for the stated metric, or label the narrower script metric accurately; align the cut-pass opener terminology accordingly.

**Viability**

An agent can follow the ordinary file-editing and writing paths. F1–F3 require procedural interpretation where the specification should supply the answer.

The weakest remaining assumption is repeat-pass stability: iteration 4 does not demonstrate that a second pass preserves the first pass’s facts and structure.

**Open design vs Mechanical work**

Owner choice: the inline-edit response contract in F3. Mechanical work: F1, F2, F4, F5, plus the already-deferred final CHANGELOG/version update. No settled editorial ruling needs reopening.

**Readiness by topic**

| Topic | Readiness |
|---|---|
| Coherence | Needs F1 |
| Followability | Needs F2–F3 |
| Source and owner-record fidelity | Substantially aligned |
| Consumers and counters | Needs F4–F5; `/start` and MAR aligned |
| Evidence honesty | Eval caveats sound; example metric needs correction |
| Scope | No additional removal justified by this spec review |
