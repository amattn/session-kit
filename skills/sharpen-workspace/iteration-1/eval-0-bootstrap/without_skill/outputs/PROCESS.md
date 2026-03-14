# PROCESS.md — inventory-api

Process improvement tracking. Captures observations, tracks them through a lifecycle, and formalizes confirmed patterns into enforceable disciplines.

## How This Works

### Lifecycle

Every process observation moves through these stages:

1. **Observed** — Something noticed during work (a friction point, a recurring mistake, a pattern that helped). Captured immediately with minimal ceremony.
2. **Validated** — The observation has recurred or been confirmed by evidence. Not a fluke.
3. **Discipline** — A validated pattern formalized into an enforceable rule. Added to CLAUDE.md so it applies to all future work.
4. **Retired** — A discipline that no longer applies (context changed, better approach found). Kept here for rationale.

### Recording an Observation

Add an entry under "Observations" with:
- **Date** observed
- **Status**: `observed` | `validated` | `discipline` | `retired`
- **Description**: What happened, concretely
- **Evidence**: Specific instances (commit, file, conversation) — add more as the pattern recurs
- **Tally**: Number of times observed (increment on recurrence)

### Promoting to Discipline

When an observation reaches `validated` and the team agrees it should be enforced:
1. Write the discipline rule in the "Active Disciplines" section below
2. Add the rule to `CLAUDE.md` so it is enforced automatically
3. Update the observation's status to `discipline`
4. Record the promotion date and the CLAUDE.md section where it lives

---

## Active Disciplines

_None yet. Disciplines will be added here as observations are validated and formalized._

<!-- Template:
### DIS-NNN: [Short Name]
- **Promoted**: YYYY-MM-DD
- **From observation**: OBS-NNN
- **Rule**: [The enforceable rule, stated clearly]
- **CLAUDE.md section**: [Where the rule lives in CLAUDE.md]
- **Rationale**: [Why this matters — link back to evidence]
-->

---

## Observations

_Add new observations at the top._

<!-- Template:
### OBS-NNN: [Short Description]
- **Date**: YYYY-MM-DD
- **Status**: observed
- **Tally**: 1
- **Description**: [What happened]
- **Evidence**:
  - [Specific instance 1]
- **Notes**: [Any additional context]
-->

---

## Retired Disciplines

_Disciplines that no longer apply. Kept for historical rationale._

<!-- Template:
### DIS-NNN: [Short Name] (retired)
- **Retired**: YYYY-MM-DD
- **Reason**: [Why it was retired]
- **Original rule**: [What the rule was]
-->
