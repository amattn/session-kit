Authority coverage: complete
Files read: README.md (full), CLAUDE.md, NOTES.md (full, 628 lines), CHANGELOG.md, .claude-plugin/plugin.json, .claude-plugin/marketplace.json, skills/{warmup,fast-chat,dictation,red-pen,notes,stable-label,multi-adversarial-review,feedback-foo}/HELP.md, plus skills/red-pen/SKILL.md and skills/multi-adversarial-review/SKILL.md to verify two concrete claims. (The grep/find tools failed in this environment; direct reads used instead.)

**Reader report.** I stopped after the Install section, as predicted — the table plus install answers both of my questions except "which one first." I read the /fast-chat table row twice ("R/O stable tail"). I did not understand R/O at point of use. I already knew skills, plugins, CLAUDE.md, and compaction, so /warmup's row landed without its gloss.

**Overall.** Works for the two-minute deciding reader: title → two-sentence value prop → complete skill table → three install options is exactly the funnel, and the table's "What it does" column is enough to pick candidates. It works less well for the reader asking "which skill first" — the document gives no signal, and the record contains one.

**Strong.**
1. The table → install path lets the reader stop exactly where the document predicts.
2. "What it adds over baseline Claude" paragraphs — the decisive install content, with honest hedging where the record is unproven (/feedback-foo detection).
3. Install blocks follow the recorded one-command-per-fence convention (NOTES).
4. Aliases and provenance are consistent everywhere and match the record (/mar, /foo aliases, "Renamed from /sharpen", Origin attributions).
5. How to Use matches the HELP.md files nearly verbatim, so the human's README and the agent's runtime reference agree — with one exception (F4).

**Needs work.**

- **F1 (high, unsourced).** "Extracted from patterns discovered during 500+ sessions of AI-assisted development." The record says "hundreds of sessions" (NOTES Project Context) and this README's own § Origin says "hundreds of sessions." "500+" appears nowhere in the record and contradicts the same document. Reader: the installer weighing credibility — it is the second sentence. Change: refer to the owner — cut to "hundreds" or source the figure; a number is a meaning finding. Same paragraph class: § Origin's "8+ parts" also has no record source.
- **F2 (medium, undefined).** Table row /fast-chat: "a review prompt with R/O stable tail." R/O is glossed only in § The Skills, after the stop point. Reader: the table scanner. Change: gloss inline ("R — show recommendations, O — approve") or cut the clause from the row.
- **F3 (medium, buried).** The reader's second decision — which skill to try first — gets no guidance; the table leads with /warmup (infrastructure, invisible value). The record ranks /stable-label > /fast-chat > /notes (NOTES 2026-10-01) and puts MAR among the most used. Reader: the first-timer picking an entry point. Change: refer to the owner — a "start here" hint or reordering is a positioning decision; the record already holds the evidence.
- **F4 (medium, stale — wrong artifact).** § How to Use /notes: "suggested sections (Project Context, Invariants, Important Concepts, Taxonomy, Key Design Decisions, Open Questions)" — but skills/notes/HELP.md lists an older order without Project Context. The record (FOO_6, CHANGELOG 0.7.0) supports the README; the HELP the installed agent reads is stale. Reader: the post-install user, whose agent and whose README disagree. Change: refer to the owner — fix HELP.md, README stays.

Verified against the record with no contradiction: 8-skill count, aliases, MAR targets and dispositions, /red-pen 300-word budget and "chose A over B because C; revisit if D" shape (SKILL.md), stable-label lifecycle claims, routes/stall/panel claims, install commands, CC BY-SA 4.0, all three Origin attributions.

**Judgment.** F1 (which number is true); F3 (entry-point recommendation); F4 (confirm README as canonical).
**Mechanical.** F2 (inline gloss or cut).

**Readiness for this reader: needs work** — the decision path works, but the headline credibility number contradicts the record and the document's own Origin section, and the "which first" question is answerable from the record the owner holds.
