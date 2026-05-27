# PLAN.md — session-kit

## Current Status

All 6 skills implemented and eval'd. Findings applied to 5 of 6 (/foo, formerly /sharpen, needed none).

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

## Next Steps

### Next publish (folded with today's follow-ups)

The most recent publish was reverted locally so today's follow-ups (Skill-tool delegation in /start, inline /notes template, /warmup settings propose-flow, README /start normalization) can ship as part of the *same* release as the initial skill-version work rather than as separate patch versions. Origin still has the prior published commit and tag — the new publish will force-push.

Tasks for the publish commit:

- **Bump distribution versions** — `plugin.json` and `marketplace.json plugins[0].version` from 0.8.0 to the new release version; `marketplace.json metadata.version` from 0.4.0 to its new release version (decide at publish time)
- **Plugin / marketplace `description` field** — use `/start` (matches the README normalization), not `/session-kit:start`. Both `description` fields list the suite's slash commands; the leading entry becomes `/start` instead of `/session-kit:start`.
- **Restore CHANGELOG entry** for the new release version, with three subsections describing the folded behavior:
  - `/start` v0.1.0 — add bullet "Sub-skills activated via the Skill tool, not `Read` as files"
  - `/notes` v0.2.0 — replace "New asset: `skills/notes/assets/notes-template.md`" with "Inline NOTES.md template in `SKILL.md` under § NOTES.md Template → § Template content (self-contained, no external asset)"
  - `/warmup` v0.2.0 — replace the scaffolding bullet with the asymmetric rule: `.gitignore` skip-if-exists unchanged; `.claude/settings.json` propose-multi-select when missing/empty/marketplace-only; settings changes never automatic
  - Add a **README** subsection: "`/session-kit:start` → `/start` everywhere in marketing copy; 'one approval' softened to surface the `.claude/settings.json` multi-select; example transcript updated to show the sub-prompt"
- **Tag and force-push** — tag the new release version (force-update over the existing tag) and force-push `main` + tag

### Description optimization

Run the skill-creator trigger optimization loop on each skill's description to improve triggering accuracy.
