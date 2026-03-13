# NOTES.md — session-kit

## Project Context

session-kit is a suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time. Extracted from patterns discovered during 50+ sessions of plet-skills development. The `/notes` skill is the first; 7 more are planned from the EXTRACTABLE.md catalog.

**Origin:** Extracted from patterns discovered during plet-skills development (`../plet-skills/`).

---

## Key Design Decisions

### Suite scope and skill roster (2026-03-13)

All 7 extractable skills from plet-skills EXTRACTABLE.md will be included in session-kit, plus the existing `/notes` skill (8 total). Scaffolding first, then skills added incrementally.

### Skill naming philosophy: nouns for systems, verbs for actions (2026-03-13)

Most skills in this suite are noun-shaped — they manage a system or artifact, not perform a one-shot action. `/notes` means "engage the notes system," not "take a note." Verb-form names (like `/mark`) undersell system-oriented skills by implying a one-shot action.

### Suite name: session-kit (2026-03-13)

Kept the original name. The suite name doesn't need to carry the value prop — the individual skill names already do that (`/fast-chat`, `/stable-label`, `/sharpen`). The suite name just says "here's a collection of session tools."

- **Rejected:** `/steady-session` — follows the [value]-[domain] pattern but feels ostentatious, "too much bragging." Promises a result rather than describing what the tool does.
- **Rejected:** `/session-craft` — aspirational but unnecessary weight
- **Chosen:** `session-kit` — neutral, modest, lets the skills do the branding

**Key insight:** Value-prop naming works for individual skills but not for the suite. Suite names should be modest containers; skill names should sell.

### /fast-chat naming (2026-03-13)

Renamed from `/chatux` (EX_1). The core value is speed — structured codes (1A, 2B, 3 with caveats) replace prose paragraphs, making communication dramatically more efficient.

- **Rejected:** `/chatux` — "ux" is jargon, doesn't convey the speed benefit
- **Rejected:** `/options` — names the mechanism (structured options) but misses the value prop
- **Rejected:** `/ask` — too vague
- **Rejected:** `/shorthand` — accurate mechanism name but doesn't convey speed
- **Chosen:** `/fast-chat` — mixes the value prop ("fast") with the domain ("chat"). Says exactly what it delivers.

**Key insight:** Skill names should mix the value proposition into the name, not just describe the mechanism. `/options` describes what you see; `/fast-chat` describes what you get.

### /sharpen naming (2026-03-13)

Renamed from `/feedback` (EX_2). The skill tracks meta-observations about process and tooling, with resolution lifecycle and promotion paths. The value prop is process improvement, not just collecting feedback.

- **Rejected:** `/feedback` — implies feedback TO someone; these are self-observations about process. Also confusable with product feedback.
- **Rejected:** `/observe` — describes the mechanism, not the value
- **Rejected:** `/process-sharpen` — descriptive but artifact name (`PROCESS-SHARPEN.md`) reads like a command, not a document
- **Rejected:** `/process-tuning` — reads naturally but redundant within session-kit (every skill is about process)
- **Chosen:** `/sharpen` → `SHARPEN.md` — conveys value prop (your process gets sharper), bold artifact name, suite context provides the "process" framing

**Caveat:** "sharpen" isn't an obvious destination for users who think in terms of "feedback" or "meta-feedback." The skill definition will need strong trigger words covering those synonyms. If SHARPEN.md sees low adoption, may need more user-facing guidance to connect the concept. Monitor this.

### /stable-label naming (2026-03-13)

Renamed from `/label` (EX_7). The skill is more than labels — it's a system for stable, greppable cross-references that never renumber and always resolve to exactly one definition. The labeling is the mechanism, but the value is the reference system.

- **Rejected:** `/label` — accurate for the mechanism but misses the "stable references" value
- **Rejected:** `/tag` — implies categorization (like git tags), leans verb
- **Rejected:** `/id` — too specific to the artifact format, not the system
- **Rejected:** `/ref` — accurate but doesn't convey the stability guarantee
- **Rejected:** `/ref_ids` — too specific, underscore in command name unusual
- **Chosen:** `/stable-label` — self-documenting ("the labels are stable"), memorable rhyme is a feature not a bug. User: "i love that b rhymes, makes it memorable"

---

## Invariants & Critical Requirements

*(None yet)*

---

## Important Concepts & Insights

### From the user

- "should a skill be a noun or verb?" — led to the nouns-for-systems principle
- "label is more than the labels. it's stable references." — drove the /stable-label rename
- "i love that b rhymes, makes it memorable but maybe too cute?" → decided it's a feature, not a bug
- "i'm not worried about long. the claude code ui is awesome at autocomplete" — length of slash commands is not a concern; clarity and descriptiveness win

---

## Taxonomy / Conventions

### Skill roster (in progress — names under review)

| # | Current name | Status | Source |
|---|-------------|--------|--------|
| 1 | /notes | Confirmed | Existing |
| 2 | /fast-chat | Confirmed | EX_1 |
| 3 | /sharpen | Confirmed | EX_2 |
| 4 | /dictation | Confirmed | EX_3 |
| 5 | /warmup | Confirmed | EX_5 |
| 6 | /patterns | Confirmed | EX_4 |
| 7 | /discipline | Confirmed | EX_6 |
| 8 | /stable-label | Confirmed | EX_7 |

---

## Open Questions

- ~~Suite name~~ → resolved: session-kit
- ~~Skill 2 (/chatux) naming~~ → resolved: /fast-chat
- ~~Skill 3 (/feedback) naming~~ → resolved: /sharpen (monitor adoption — name may not be intuitive for "feedback" mental model)

---

## Things to Monitor

*(None yet)*

---

## Artifact Approval Status

*(None yet)*
