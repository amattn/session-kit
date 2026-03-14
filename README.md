# session-kit

A suite of Claude Code skill plugins for making AI-assisted development sessions reliable and productive across time.

Extracted from patterns discovered during 500+ sessions of AI-assisted development. Each skill addresses a specific friction point that compounds over time — lost context, slow decision-making, garbled input, fragile cross-references.

## Skills

| Skill | What it does |
|-------|-------------|
| `/notes` | Institutional memory. Captures decisions, rationale, and conventions in NOTES.md so future sessions don't re-litigate settled questions. |
| `/warmup` | Session bootstrap and compaction recovery. Ensures skills, disciplines, and key files load reliably and survive context compaction. |
| `/stable-label` | Greppable stable references. Gives every referenceable thing an append-only ID (`REQ_3`, `DEC_14`) that never renumbers and always resolves to exactly one definition. |
| `/fast-chat` | Structured interaction patterns. Numbered questions, lettered options, batch answer codes (`1A, 2B, 3 let's discuss pros/cons`). Always-on communication style that makes decisions faster. |
| `/dictation` | Project-specific correction table. Originally designed for voice-to-text errors, but also useful for recurring typos and emergent shorthand — any systematic input pattern where the user means something other than what they literally typed. |
| `/sharpen` | Process improvement — pattern detection, observation tracking, and discipline creation. Proactively notices recurring patterns, tracks process observations with a resolution lifecycle, and helps formalize workflows as named disciplines. |

## Install

### Option 1: Claude Code Marketplace

```bash
/plugin marketplace add amattn/session-kit
/plugin install session-kit@session-kit-marketplace
```

### Option 2: Global Installation

Copy the skills into your Claude Code skills directory so they're available across all projects:

```bash
cp -r skills/* ~/.claude/skills/
```

### Option 3: Project-Level Installation

Copy the skills into your project for per-project use:

```bash
mkdir -p .claude/skills
cp -r /path/to/session-kit/skills/* .claude/skills/
```

## The Skills

### `/notes` — Institutional Memory

The most common failure mode in multi-session AI work: decisions get re-litigated because nobody remembers why they were made. `/notes` maintains a living `NOTES.md` that captures decisions, rationale, rejected alternatives, and conventions. Every session starts with an accurate picture of what's been decided and why.

Why it matters: without institutional memory, session 12 reopens questions that session 3 settled. The rationale is gone, so the same arguments play out again. `/notes` makes this nearly impossible — the reasoning is written down, in the user's own words, before the conversation moves on.

What it adds over baseline Claude: the CLAUDE.md discipline block is the killer feature — it makes note-taking behavior persist across sessions, not just the current one. The skill also enforces consistent structure (same sections every project) and preserves user quotes verbatim where baseline Claude tends to paraphrase.

### `/warmup` — Session Bootstrap & Compaction Recovery

AI agents don't reliably read project files at session start, and context compaction mid-session can silently drop critical instructions. `/warmup` is the reliability layer — it uses every available tactic (auto-memory, Required Reading sections, discipline blocks, loading canaries) to ensure that what matters gets loaded and stays loaded.

Why it matters: every other skill in session-kit depends on the agent actually reading and following project directives. `/warmup` is what makes that reliable instead of aspirational.

What it adds over baseline Claude: the baseline can set up individual pieces (compaction recovery, required reading) but doesn't build the complete layered system — Required Reading + canaries + post-compaction rule + breadcrumbs + auto-memory guidance + cross-platform AGENTS.md — as integrated infrastructure. The skill also provides a systematic diagnostic checklist and escalation ladder for when rules aren't being followed reliably.

### `/stable-label` — Greppable Stable References

Gives every referenceable thing an append-only ID using the `XXX_N` convention (`REQ_3`, `DEC_14`). IDs never renumber, never get reused, and always resolve to exactly one definition. `grep REQ_3` returns the definition and every reference across the entire project.

Why it matters: without stable IDs, cross-references are fragile text that breaks when things get renamed. With them, any ID is a permanent, greppable anchor — in docs, in code comments, in docstrings, anywhere text lives. Both humans and agents can trace a requirement from spec to implementation in seconds.

What it adds over baseline Claude: convention enforcement is the biggest win — without the skill, Claude invents ad-hoc formats (kebab-case, dashes, zero-padding) that vary per session. The skill ensures consistent `XXX_N` format every time. Lifecycle operations are the second major differentiator: splits get provenance notes, merges keep tombstone redirects so every ID stays greppable, promotions get bidirectional cross-references, and crosscutting concerns get domain-specific faceted IDs instead of just prose. The baseline handles simple operations fine but loses ID traceability during lifecycle changes.

### `/fast-chat` — Structured Interaction Patterns

Replaces prose-heavy back-and-forth with structured codes. Numbered questions with lettered options, batch answer codes (`1A, 2B, 3ok`), and a standard review prompt with situational options plus a stable Recommendations/Ok tail. This is an always-on communication style, not just a tool you invoke.

Why it matters: every decision point in AI-assisted work is a potential bottleneck. Open-ended questions ("what do you think?") force the user to do generative work. Structured options let them do evaluative work — picking from a list instead of inventing from scratch. The speed gain compounds across hundreds of decisions per session and hundreds of sessions per project.

What it adds over baseline Claude: behavioral activation. Claude already *knows* these interaction patterns, but doesn't consistently *use* them — even when conventions are written in CLAUDE.md. The skill provides the activation energy to apply structured options to every decision point, use the review prompt for approvals, and avoid open-ended questions. The patterns themselves aren't novel; the consistent application is.

### `/dictation` — Correction Table

Maintains a project-specific table for voice-to-text errors, recurring typos, and emergent shorthand. Originally designed for dictation (voice engines predictably mangle project jargon), but the table is useful for any systematic input pattern where the user means something other than what they literally typed.

Why it matters: each uncorrected error costs a correction cycle — the user says it, the agent misunderstands, the user corrects, the agent apologizes. A correction table eliminates this for known patterns, and a learning loop captures new ones as they appear.

What it adds over baseline Claude: the bootstrap puts the correction table in CLAUDE.md (loaded every session) rather than an ad-hoc file. When input is garbled beyond the table, the skill presents structured disambiguation options instead of guessing. And the "What Does NOT Go" boundaries prevent table bloat — one-off typos and standard abbreviations (k8s, img) stay out.

### `/sharpen` — Process Improvement

The process improvement skill — combines pattern detection, observation tracking, and discipline creation into one place. Proactively notices recurring patterns ("I've seen this twice, should we write it down?"), tracks process observations with a resolution lifecycle (open → resolved), and helps formalize important workflows as named disciplines.

Why it matters: process improvements come from two directions — the agent notices patterns, and the user reports friction. Both need somewhere to go. Without `/sharpen`, observations get lost in conversation and patterns go unnoticed. With it, informal habits become named disciplines, friction becomes tracked observations, and the process gets sharper over time.

What it adds over baseline Claude: when told about a recurring failure, baseline Claude apologizes and fixes the immediate problem. The skill treats it as a process improvement opportunity — creates a tracked observation, strengthens the relevant discipline, and flags escalation to tooling if prose keeps failing. The methodology (routing, discipline creation, prose→tooling escalation) is confirmed by evals. The proactive detection — the always-on capability where the agent notices patterns without being told — is the highest-value feature and requires real-world usage to fully validate.

## How They Fit Together

```
/warmup          → ensures everything loads reliably
                    (the foundation — without it, nothing else is guaranteed)

/notes           → captures what was decided and why
                    (institutional memory across sessions)

/stable-label    → makes cross-references greppable and permanent
                    (machine-verifiable navigation)

/fast-chat       → makes every interaction faster
                    (structured codes replace prose)

/dictation       → removes input friction
                    (correction table for voice, typos, shorthand)

/sharpen         → detects patterns, tracks observations, creates disciplines
                    (process gets sharper over time)
```

The skills are independent — install any subset. But they're designed to complement each other: `/warmup` ensures `/notes` loads every session, `/stable-label` gives `/notes` entries greppable IDs, `/fast-chat` speeds up the decisions `/notes` captures, and `/dictation` keeps voice input from garbling the whole conversation.

## Origin

Developed and battle-tested during [plet-skills](https://github.com/amattn/plet-skills) development (8+ parts, hundreds of sessions). Extracted as a standalone suite for use in any Claude Code project.

`/fast-chat` was strongly inspired by [snarktank's Ralph skills](https://github.com/snarktank/ralph).

## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). You're free to use, share, and adapt these skills — including in commercial projects — as long as you provide attribution and share any adaptations under the same license. See [LICENSE](LICENSE) for the full text.
