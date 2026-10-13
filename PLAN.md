# PLAN.md — session-kit

## Current Status

8 skills implemented. 7 eval'd: findings applied to 5 of the original 6 (/foo needed none); /red-pen has three eval iterations and is at v0.2.1. /multi-adversarial-review is ported from vog_kit and not yet eval'd.

## Completed

### 1. Re-evaluate EXTRACTABLE.md ✓

Found the "Skills for Judgment, Code for Compliance" insight — prose disciplines drift, supplement with tooling when needed. Applied to /foo.

### 2. Eval: /notes ✓

10 test pairs. Key finding: CLAUDE.md discipline block is the killer feature. Adjustments: "quote the user, paraphrase everything else," bootstrap seeds Open Questions as an offer. Value-add sections moved from skills to README.

### 3. Eval: /dictation ✓

8 test pairs. Key finding: structured disambiguation is the main differentiator. Bootstrap format (CLAUDE.md with breadcrumb) matters. Adjustments applied.

### 4. Eval: /stable-label ✓

15 test pairs (11 + 4 lifecycle). Key findings: convention enforcement is the biggest win, lifecycle operations (split, merge, promote, crosscut) are the strongest differentiator. Added read/analyze vs create/modify heuristic for when NOT to assign IDs.

### 5. Eval: /fast-chat ✓

8 test pairs. Key finding: behavioral activation is the primary value — Claude knows the patterns but doesn't consistently use them without the skill. Eval 6 over-trigger noted as eval artifact, added to Things to Monitor.

### 6. Eval: /warmup ✓

9 test pairs. Key finding: full layered infrastructure is the differentiator — baseline handles individual concepts but doesn't build the complete system. Fixed over-trigger on unrelated requests. Adopted two baseline innovations: cross-file reinforcement loop and content quality diagnosis.

### 7. Eval: /foo (was /sharpen) ✓

8 test pairs. First skill where the eval confirmed the design — no adjustments needed. Strongest differentiators: evals 5-6 (recurring failures treated as process improvement, not just apologies). Prose→tooling escalation is unique to the skill. Caveat: proactive detection untestable in single-turn evals, added to Things to Monitor.

### 8. Plugin bundles ✓

Designed and implemented three bundles: session-kit (full), session-kit-core (/warmup, /fast-chat, /dictation), session-kit-refine (/notes, /stable-label, /foo). Symlinks from bundle skills/ directories to root skills/. Marketplace metadata bumped to 0.2.0.

### 9. Publish ✓

Published to GitHub marketplace.

### 10. README: How to Use section, skill reordering, drop bundles ✓

Added How to Use section with setup/ongoing for each skill. Added "Best for" lines to The Skills section. Reordered all sections to consistent order (warmup, fast-chat, dictation, notes, stable-label, foo). Removed bundle install options — skills are inert without explicit setup, so bundles add complexity without value.

### 11. Remove bundles from marketplace ✓

Removed session-kit-core and session-kit-refine from marketplace.json, deleted bundle directories, bumped plugin version to 0.5.0.

### 12. HELP.md and Quick Reference convention ✓

Added HELP.md files to all 6 skills (seeded from README How to Use section). Added Quick Reference blockquote to top of each SKILL.md with directive to read HELP.md for usage questions and escalation path to full SKILL.md for edge cases. Plugin version bumped to 0.6.0.

### 13. FOO_4, FOO_5, FOO_6 — foo-driven skill updates ✓

Applied three process observations from FEEDBACK_FOO.md:
- FOO_5: /fast-chat review prompt redesigned (R/O tail, silence-is-not-approval, drop S and A-E layout)
- FOO_4: /warmup escalation ladder gets concrete language-strengthening tactics
- FOO_6: /notes suggested section order reordered (stable reference first, decision log after)

### 14. Rename /sharpen → /foo ✓

Renamed skill from `/sharpen` to `/foo` (FOO = Feedback, Observation, Oversight). `/feedback` and `/feedback-foo` as aliases. Artifact `SHARPEN.md` → `FEEDBACK_FOO.md`, prefix `SPI_N` → `FOO_N`, directory `skills/sharpen/` → `skills/feedback-foo/`. Plugin version bumped to 0.8.0.

### 15. /session-kit:start skill + supporting infrastructure ✓

Added a unified bootstrap entry point and the supporting infrastructure the per-skill bootstraps lean on:

- **New `/session-kit:start` skill** (`skills/start/SKILL.md`, `HELP.md`) — minimal/standard/full tiers, single-approval flow for the plan (plus a `.claude/settings.json` sub-prompt when /warmup hits the propose path), re-runnable to pick up missing pieces. Sub-skills are activated via the Skill tool — /start never `Read`s sub-skill SKILL.md files as on-disk assets.
- **/notes template-driven bootstrap** — canonical NOTES.md scaffold lives inline in `skills/notes/SKILL.md` under § NOTES.md Template → § Template content (no external asset file, no permission-prompted read). Default prefix table, Quick Reference front-matter with TOC, `PREFIX_N: YYYY-MM-DD - Title` header format. New § Scaling: Hierarchical Prefixes for Large Projects.
- **/stable-label section labels vs IDs** — new § disambiguates bare-prefix section labels from IDs, bootstrap split into Branch A (table pre-seeded by /notes) and Branch B (no table), no-shorthand rule reinforced in the convention block
- **Commit style updated in CLAUDE.md** — switched from verb-first (`Add /foo: …`) to prefix-first (`feature: …`); commits before 2026-05-27 use the older style

Versioning, CHANGELOG, and a publish will happen as a follow-up before the next release. /warmup combined-canary changes were unstaged for a separate commit.

### 16. /warmup project scaffolding + combined canary ✓

Two additions to /warmup, version 0.1.2 → 0.2.0:

- **Project scaffolding bootstrap** — new § Project Scaffolding Files in Tactics + new step 2 in Bootstrap. Asymmetric rules per file:
  - `.gitignore` — skip-if-exists. Creates with `.DS_Store` only when the file is missing; never touches an existing file.
  - `.claude/settings.json` — **propose, never automatic.** /warmup proposes additions via a /fast-chat multi-select (A: `permissions.allow`, B: `includeCoAuthoredBy: false`, C: `env.CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, D: `enabledPlugins: session-kit@session-kit-marketplace`) when the file is missing, empty, or contains only `enabledPlugins` (the marketplace-install shape). For any other content, leaves it alone. User approves all, some, or none; writes are additive — never overwrite existing values.
- **Combined canary** — new recommended-default canary that folds acknowledgment + git status into one line. Existing acknowledgment/behavioral/content canaries preserved as alternatives. Bootstrap step 6 now defaults to the combined form.

Cascade: README.md and HELP.md updated; NOTES.md entries with defaults, rejected alternatives, and the propose-vs-skip rationale per file.

### 17. Bootstrap correctness fixes + publish v0.9.0 (folded) ✓

Three corrections to bootstrap behavior applied as commit `6c66bb1` (`fix: bootstrap correctness …`), then folded into the same v0.9.0 release as items 15-16:

- **/start** — sub-skills activated via the Skill tool, not `Read` as on-disk files
- **/notes** — NOTES.md template inlined into SKILL.md under § Template content; `skills/notes/assets/notes-template.md` and the `assets/` directory removed (self-contained skill)
- **/warmup** — `.claude/settings.json` blanket skip-if-exists → propose-multi-select when the file is missing, empty, or contains only `enabledPlugins` (the marketplace-install shape); `.gitignore` rule unchanged
- **README** — `/session-kit:start` → `/start` in marketing copy; "one approval" softened to surface the settings.json sub-prompt; example transcript updated

Publish commit force-pushes over origin's prior 0.9.0 commit (which had the un-corrected interim behavior; never tagged on origin). Distribution versions: `plugin.json` and `marketplace.json plugins[0].version` 0.8.0 → 0.9.0; `marketplace.json metadata.version` 0.4.0 → 0.5.0. Both `description` fields now lead with `/start`. Tag `v0.9.0` created locally; force-push by user.

### 18. /red-pen skill ✓

Incorporated `WRITING_DIRECTIVES.md` as a new always-on skill, `/red-pen` v0.1.0. SKILL.md (four modes, shared core, mode selection, cut pass, bootstrap block), HELP.md, README entries, CHANGELOG. Plugin/marketplace versions not bumped — distribution bump is human-directed.

### 19. Eval: /red-pen, iterations 1 to 3 ✓

Iteration 3 blind result: skill preferred 6 of 8, baseline 1, both fine 1; graders 84% vs 48%. Fixes applied as v0.2.1 (cost on its own line, bold bullet labels, lead-in for the before/after pair, tighter budget escape, new worked example). Remaining, optional: an iteration 4 to confirm v0.2.1; replace the non-discriminating assertions; reconcile the pr-description assertions with the user's preference.

Prerequisite done: `scripts/symptoms.py` gives the eval a mechanical before/after measure; `references/worked_example.md` is the reference pair.

Create `skills/red-pen-workspace/evals/evals.json` with skill-creator guidance, run with-skill vs baseline, apply findings. Inputs must be fresh generated drafts, not mature specs (see NOTES: premise test). Judge by preference on paired before/after paragraphs, reported by symptom counts, never by word count. Candidates: a fresh spec request for a product reader (does it open with a preamble, state each fact once, pace by stakes?), a `/red-pen <file>` editing pass on `test-projects/edit-target/grid_section.md`, a "too long" follow-up, a code change (does it narrate in comments?), a bootstrap on a project that already has a commit style. The open question the eval must answer: do the always-on rules prevent the symptoms at generation time, or only let the editing pass remove them afterward?

### 20. Port /multi-adversarial-review from vog_kit ✓

Claude copy ported as `skills/multi-adversarial-review` v0.1.0 (alias `mar` via description trigger). Vog-specifics generalized to examples, HELP.md, README, CHANGELOG. session-kit canonical; vog_kit README now points here. Follow-ups: Codex variant; a `copy` target for /red-pen (readers as lenses, Strong/fidelity contract); evals in degraded same-host mode.

### 21. `copy` target for /multi-adversarial-review ✓

Added as `references/copy-review.md` with hooks in SKILL.md and HELP.md; /red-pen points to it. /multi-adversarial-review v0.2.0, /red-pen v0.2.2. First real run: the README copy review (see NOTES).

### 22. Publish v0.10.0 ✓

Rebased onto the May changes (/start, OpenCode, /warmup scaffolding). Plugin 0.10.0, marketplace metadata 0.6.0; /red-pen and /multi-adversarial-review added to both manifests. Tagged v0.10.0.

### 23. /red-pen v0.3.0: sentence rules from ASD-STE100 ✓

Sentence and paragraph rules at about 80% strength, a lost-facts check in the cut pass, agents as readers, and new symptom counts. Iteration 4 measured fact retention: 45/46 for both v0.3.0 and v0.2.5, with shorter sentences and no meaning drift on the edit.

## Next Steps

### Description optimization

Run the skill-creator trigger optimization loop on each skill's description to improve triggering accuracy.

### /red-pen eval iteration 5 (optional)

Confirm v0.2.1+ fixes; replace the assertions that do not discriminate; align the pr-description assertions with the owner's preference.
