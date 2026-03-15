---
name: dictation
version: 0.1.1
description: "Project-specific correction table for voice input errors, recurring typos, and emergent shorthand. Use when the user asks to 'dictation', 'voice correction', 'add misspelling', 'fix dictation', 'add shorthand', or when input garbles project-specific terms. Also proactively trigger when you notice the user correcting a misinterpretation that looks like a recurring pattern — offer to add it to the correction table. Also trigger the bootstrap flow when a project has jargon-heavy terms (framework names, internal tools, abbreviations) but no correction table yet."
user-invocable: true
---

# /dictation — Voice Input Correction

> **Quick Reference:** See [HELP.md](HELP.md) for setup, usage, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.
> For detailed mechanics or edge cases, the full SKILL.md has the complete specification.

Maintain a project-specific correction table. Originally designed for voice-to-text errors — voice engines mangle project jargon predictably ("jason" for JSON, "cloud" for Claude, "Maine" for main). But the table is useful beyond dictation: recurring typos, emergent shorthand (like "1b1" for one-by-one), and any recurring input pattern where the user means something other than what they literally typed. A correction table turns these from recurring friction into transparent fixes.

---

## The Job

1. **Always-on**: when a user message contains known misspellings from the correction table, apply corrections and proceed. Most corrections can be silent — no need to announce every "jason → JSON." But when a correction changes the meaning of the message in a way that affects the action taken (e.g., "Maine" → "main" when the user might actually mean the US state), briefly confirm before acting.
2. **On explicit invocation**: detect whether a correction table exists in AGENTS.md and/or CLAUDE.md. If not, bootstrap. If yes, show current table and ask what to adjust.

---

## The Correction Table

A simple two-column table in AGENTS.md and/or CLAUDE.md:

```
## Common Misspellings (voice input)
<!-- managed by /dictation -->

| Heard/Typed | Means |
|-------------|-------|
| cloud       | Claude |
| jason       | JSON |
| Maine       | main (git branch) |
```

Guidelines:
- **One row per correction** — keep entries atomic
- **Multi-word entries are fine** — voice engines often split or garble compound terms: "re-base of emerge → rebase over merge," "sub plet → subplet"
- **Include context when ambiguous** — "Maine" could mean the US state in some projects; the parenthetical "(git branch)" disambiguates
- **Group by frequency** — put the most common corrections near the top so they're found quickly during audits

---

## Bootstrap

When invoked on a project for the first time:

1. **Scan the project** — read README, AGENTS.md and/or CLAUDE.md, NOTES.md, and key source files. Identify jargon that voice engines are likely to mangle: framework names, internal tool names, abbreviations, unconventional spellings.

2. **Seed the table** — propose an initial correction table based on the scan. Focus on terms that voice engines are likely to mangle *and* that the agent can't easily infer from context. Common tech terms like JSON or API are usually recoverable without a table — the real value is in:
   - Project-specific names: the project name itself, key module names, internal tool names
   - Domain jargon: terms unique to the project's problem space
   - Unconventional spellings: names that don't follow English phonetics
   - Compound terms that voice splits: "subagent" heard as "sub agent," "rebase over merge" heard as "re-base of emerge"

3. **Present for review** — show the proposed table. The user adds, removes, or corrects entries.

4. **Write to AGENTS.md and/or CLAUDE.md** — add the correction table with the `<!-- managed by /dictation -->` breadcrumb.

5. **Add /fast-chat shorthands** — if the project uses /fast-chat, add NL, NLR, 1b1 to the correction table so voice engines don't mangle them.

---

## Ongoing Operations

### When garbled beyond the table

When a message doesn't parse cleanly — especially when multiple words seem wrong in a way that doesn't match any single intent — ask for clarification rather than guessing. Present your best interpretations as lettered options so the user can pick quickly. The cost of asking is one round-trip. The cost of guessing wrong is a wasted action and a correction cycle.

### Learning new corrections

When the user corrects a misinterpretation that looks like a recurring pattern (voice error, habitual typo, or shorthand), offer to add it to the correction table. Keep the offer lightweight — "Want me to add 'pleat → plet' to the correction table?" One sentence, not a ceremony.

### Editing the table

When invoked on a project that already has a correction table:

1. Show the current table
2. Ask what the user wants to add, change, or remove
3. Make the changes, preserving the breadcrumb

---

## What Does NOT Go in /dictation

- **One-off typos** — /dictation captures *systematic, recurring* patterns (voice errors, habitual typos, emergent shorthand). One-off typos don't need a table entry.
- **Abbreviation expansion** — if "k8s" means "Kubernetes" in the project, that's a convention, not a voice correction. It might go in AGENTS.md and/or CLAUDE.md, but not in the dictation table.
- **The shorthands themselves** — /fast-chat defines NL, NLR, 1b1. /dictation just adds them to the correction table so voice engines don't mangle them.

---

## How It Fits

```
AGENTS.md and/or CLAUDE.md  → correction table (the reference)
                               (every session knows the corrections)

Always-on behavior          → silently apply known corrections
                               (no announcement, just understanding)

Disambiguation              → ask when garbled beyond the table
                               (lettered options, one round-trip)

Learning                    → offer to add new corrections
                               (lightweight, one sentence)
```

/dictation removes a class of friction that compounds over time. Each uncorrected voice error costs a correction cycle — the user says it, the agent misunderstands, the user corrects, the agent apologizes. A correction table eliminates the cycle for known terms, and the learning loop shrinks the set of unknown terms over time.
