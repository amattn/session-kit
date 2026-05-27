# NOTES.md — {{PROJECT_NAME}}

Living institutional memory for {{PROJECT_NAME}}. Captures the **why** behind decisions, rejected alternatives, user insights, and conventions. See AGENTS.md (or CLAUDE.md) § NOTES.md Discipline for update rules.

---

## Quick Reference

**Stable label IDs** use `XXX_N` format (e.g., `DEC_1`, `OPN_3`). **Append-only** — never renumber, never reuse. Bare prefixes appearing in section headers like `(TAX)` are **section labels**, not IDs.

**Entry header format:** `### PREFIX_N: YYYY-MM-DD - Title`

Examples:
- `### DEC_1: 2026-05-27 - Adopt Postgres for the event store`
- `- **OPN_3: 2026-05-27 - What auth scheme?**` (bullet form for list-shaped sections)

The colon marks the end of structured metadata (ID, date). Everything after the date's ` - ` is free-form title — titles can contain dashes freely.

**Full prefix table:** § Taxonomy / Conventions below.
**Full convention rules:** AGENTS.md § Stable Label Convention.
**Skill suite:** [session-kit](https://github.com/amattn/session-kit) — `/notes` defines this template; `/stable-label` defines the ID convention.

### Sections

- [Project Context](#project-context)
- [Invariants & Critical Requirements (ICR)](#invariants--critical-requirements-icr)
- [Important Concepts & Insights (INS)](#important-concepts--insights-ins)
- [Taxonomy / Conventions (TAX)](#taxonomy--conventions-tax)
- [Key Design Decisions (DEC)](#key-design-decisions-dec)
- [Open Questions (OPN)](#open-questions-opn)
- [Things to Monitor (MON)](#things-to-monitor-mon)
- [Artifact Approval Status](#artifact-approval-status)

_As you add H3 entries (`DEC_1`, `INS_2`, etc.), add them under their parent section here. A stale TOC is worse than no TOC._

---

## Project Context

**{{PROJECT_NAME}}** — {{PROJECT_DESCRIPTION}}.

Bootstrap: {{DATE}}.

_(Replace this paragraph with: what is this project, where did it come from, one-liner on how it works. List anything explicitly TBD so future sessions don't make assumptions.)_

---

## Invariants & Critical Requirements (ICR)

_Load-bearing rules that must not be violated. Each stated as a checkable rule, justified, and scoped. Small but high-impact. Assigned `ICR_N` IDs. The `(ICR)` in this heading is a section label, not an ID — see § Stable Label Convention above._

_Example format — replace with real entries:_

- **ICR_1: YYYY-MM-DD - All times stored in UTC.** Why: avoid timezone bugs across users and servers. Scope: every persisted timestamp.

---

## Important Concepts & Insights (INS)

### From the user

_Direct quotes from the user about principles, values, or preferences — verbatim. Quotes resist drift across sessions and preserve the user's voice._

### Emergent

_Insights crystallized during design conversation. Paraphrase freely. Assigned `INS_N` IDs._

_Example format — replace with real entries:_

### INS_1: YYYY-MM-DD - Insight title

Body explaining the insight and why it matters.

---

## Taxonomy / Conventions (TAX)

### Stable Label Prefixes

| Prefix | Artifact type                          | Source section                       |
|--------|----------------------------------------|--------------------------------------|
| DEC    | Design decisions                       | Key Design Decisions                 |
| ICR    | Invariants & critical requirements     | Invariants & Critical Requirements   |
| INS    | Insights & principles                  | Important Concepts & Insights        |
| OPN    | Open questions                         | Open Questions                       |
| MON    | Things to monitor                      | Things to Monitor                    |
| TAX    | Taxonomy groups (enumerations)         | Taxonomy / Conventions               |
| FOO    | Feedback / observations / oversight    | FEEDBACK_FOO.md (when /foo runs)     |

**TAX semantics:** each `TAX_N` is a complete **enumeration unit** (e.g., "8 phases", "3 bug types", "5 feature types"). Members are referenced by name in prose by default. Promote to sub-IDs (`TAX_N_M` or `TAX_N_NAME`) only if a specific taxonomy starts being cross-referenced enough to warrant it.

**Convention rules:** see AGENTS.md § Stable Label Convention. Append-only; never renumber, never reuse; always use the full registered prefix.

_(Customize the table for this project: rename prefixes, drop unused ones, add project-specific ones. Append-only once IDs exist in the wild.)_

---

## Key Design Decisions (DEC)

_What was decided, why, rejected alternatives, status. Typically the largest and most active section. Assigned `DEC_N` IDs. Capture rejected alternatives — the "why not" is as valuable as the "why."_

_Example format — replace with real entries:_

### DEC_1: YYYY-MM-DD - Adopt Postgres for the event store

Chose Postgres for ACID guarantees on the event log.

**Why:** event ordering correctness is load-bearing; we will reconstruct state from this log.

**Rejected alternatives:**
- **DynamoDB** — cheaper at scale but eventual consistency makes ordering reasoning harder
- **SQLite** — simpler ops but no concurrent writers

---

## Open Questions (OPN)

_Unresolved topics, things to investigate, items awaiting user input. Assigned `OPN_N` IDs._

_Example format — replace with real entries:_

- **OPN_1: YYYY-MM-DD - What auth scheme?** JWT vs session cookies vs OAuth-only. Needs a security review before deciding.

---

## Things to Monitor (MON)

_Watchlist items: drift risks, size concerns, potential problems. Assigned `MON_N` IDs._

_Example format — replace with real entries:_

- **MON_1: YYYY-MM-DD - NOTES.md size.** Currently small; revisit if it exceeds ~500 lines or starts crowding context.

---

## Artifact Approval Status

_Section-by-section tracking of what's been reviewed and approved. Most useful when there's no separate plan file._
