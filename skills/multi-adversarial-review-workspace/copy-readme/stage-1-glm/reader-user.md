Authority coverage: complete
- README.md (artifact, in full)
- CLAUDE.md
- NOTES.md (all 628 lines)
- CHANGELOG.md
- .claude-plugin/plugin.json, .claude-plugin/marketplace.json
- skills/*/HELP.md — dictation, fast-chat, feedback-foo, multi-adversarial-review, notes, red-pen, stable-label, warmup

**Overall** — Works for the evaluator browsing before install ("The Skills" sells each one with sourced, honest claims). Works less well for the stated reader: the weekly user looking up one skill. My `/stable-label` lookup succeeded on the first pass — Setup/Ongoing/Example, verbatim with HELP.md, nothing to reread. My `/mar` lookup made me read the Setup paragraph twice ("Nothing to bootstrap. You need at least one reviewer route…" packs five tool names and two jargon terms into two sentences; `cn` stopped me cold). I skipped ~300 lines of "The Skills" marketing to reach "How to Use," which is where my answers live; I already knew the names, so the table was skippable. The `500+ sessions` claim in the intro is the one thing I could not source anywhere.

**Strong**
1. The uniform Setup / Ongoing / Example shape in How to Use — the lookup reader's three needs, one place per skill.
2. HELP.md seeding is verbatim for /stable-label, /dictation, /warmup — README matches runtime docs.
3. One command per fenced block in Install — follows the recorded convention.
4. "Best for" lines — scannable triage without reading paragraphs.
5. Honest hedging ("requires real-world usage to fully validate") that matches the record's caveats rather than overselling.

**Needs work**

- **F1 (unsourced, high)** — Intro: "Extracted from patterns discovered during 500+ sessions." The record says "hundreds of sessions" (NOTES.md Project Context), and the README's own Origin section repeats "hundreds." No file supports 500+. Reader: anyone weighing the suite on evidence. Propose: refer to owner — restore "hundreds" or produce a source. Same lens: "8+ parts" in Origin has no record source.
- **F2 (buried / no-route, high)** — How to Use sits after ~300 lines of The Skills; the Skills table rows are not links. Reader: the one-skill lookup, every visit. Propose: anchor-link each table row to its How to Use section (mechanical).
- **F3 (restated, medium)** — /stable-label's guarantee ("append-only ID… never renumber… exactly one definition") appears nearly verbatim in the table, The Skills, and How They Fit Together. Reader: the top-to-bottom evaluator. Propose: merge — table keeps name + one clause.
- **F4 (undefined, medium)** — MAR Setup: "Pi (or cn / OpenCode)". `cn` is glossed nowhere; `Pi` gets none either. Reader: the weekly user executing the one setup step /mar has. Propose: gloss both in one clause, or refer to owner for canonical route names.
- **F5 (history, low)** — Skills table, /feedback-foo row: "(Renamed from /sharpen.)" Migration history inside the lookup table. Reader: the scanning lookup user. Propose: cut from the table; the rename lives in the skill section and HELP's migration note.
- **F6 (stale sibling, low)** — README /notes Setup lists "(Project Context, Invariants, Important Concepts, Taxonomy, Key Design Decisions, Open Questions)" — correct per the record (FOO_6 order, 2026-03-24) — but skills/notes/HELP.md omits Project Context and uses the old order. Not a README defect. Propose: refer to owner (fix HELP.md).

**Judgment** — F1 (owner must source or soften the number), F5 (cut history from table), F6 (owner reconciles HELP.md).
**Mechanical** — F2 (anchor links), F3 (merge table row with section opener), F4 (gloss `cn`/`Pi`).

**Readiness for this reader: needs work.** The /stable-label lookup is ready as-is; the /mar lookup is one gloss away; F1 must be resolved before the intro's evidence claim can be trusted.
