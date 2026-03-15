---
name: fast-chat
version: 0.1.0
description: "Structured interaction patterns for efficient human-AI communication. Codes (1A, 2B, 3ok) replace prose. Use when the user asks to 'fast-chat', 'set up options', 'set up fast chat', 'NL', 'NLR', '1b1', or wants structured decision-making. Also proactively adopt these patterns whenever you are presenting the user with choices, reviewing work for approval, or about to ask an open-ended question that could be lettered options instead — even if the user hasn't mentioned /fast-chat. These patterns are always-on communication defaults, not something that requires explicit invocation. Also trigger the bootstrap flow when setting up a new project's AGENTS.md and/or CLAUDE.md if no interaction conventions are defined yet."
user-invocable: true
---

# /fast-chat — Structured Interaction Patterns

> **Quick Reference:** See [HELP.md](HELP.md) for setup, usage, and examples.
> When the user asks how to use this skill, what it does, or asks for help,
> read and respond from HELP.md — you may not need to read the full SKILL.md.
> For detailed mechanics or edge cases, the full SKILL.md has the complete specification.

Replace prose-heavy back-and-forth with structured codes. Numbered questions, lettered options, single-character responses. The result: decisions that used to take a paragraph take three characters ("1A, 2B").

Originally developed for voice-input workflows where brevity is critical, but equally effective for typed interaction — the speed gain comes from reducing cognitive load, not just keystrokes.

**This is an always-on communication style, not just a tool you invoke.** Invoking `/fast-chat` runs the bootstrap (sets up conventions in AGENTS.md and/or CLAUDE.md). But the patterns themselves should be adopted immediately and used in every interaction where decisions are being made — no setup required.

---

## The Job

1. **Always-on**: adopt these patterns in every interaction — present options in NL style, parse batch answers, use the review prompt for approvals
2. **On explicit invocation**: detect whether conventions exist in AGENTS.md and/or CLAUDE.md. If not, bootstrap. If yes, show current config and ask what to adjust.

---

## The Standard Review Prompt

The single highest-leverage pattern. When presenting work for review, replace open-ended "anything else?" with structured options.

The prompt has two parts:

**Situational options** — the first N letters, adapted to the context. Could be two options, could be four — however many the situation calls for. The Add/Change/Remove set is a common default for reviewing artifacts, but other situations call for different choices. A naming decision might offer three candidate names. A plan review might offer "expand scope / narrow scope." Pick options that match what the user is actually deciding.

**Stable tail** — the last two options are always the same, regardless of how many situational options precede them:

```
[last - 1]. Recommendations — tell me what you'd suggest
[last].     Ok — approve as-is
```

"Recommendations" invites the agent to surface concerns proactively. "Ok" gives the user a fast exit. Together they ensure every review prompt supports both "I want your opinion" and "just approve it" without the user needing to invent a response.

**Example with 3 situational options** (artifact review):

```
A. Add something
B. Change something
C. Remove something
D. Recommendations — tell me what you'd suggest
E. Ok — approve as-is
```

**Example with 2 situational options** (direction choice):

```
A. Keep the current approach
B. Try the alternative
C. Recommendations — tell me what you'd suggest
D. Ok — approve as-is
```

Composable: "A, C" means "keep the current approach, and also tell me what you'd change."

This replaces the vague "what do you think?" or "any feedback?" with a menu that's faster to respond to. Use it after presenting any artifact, plan, or decision for approval — it applies everywhere.

---

## The Patterns

/fast-chat defines patterns in two groups: mechanics (how to format and parse) and principles (when and why to use them).

### Mechanics

#### 1. Numbers-Letters Options (NL / NLR)

Numbered questions with lettered options. The core pattern.

```
1. What kind of persistence?
   A. In-memory only
   B. Local file storage (SQLite, JSON)
   C. Remote database
   D. Other — please specify

2. Project ID?
   A. LOGA
   B. LOGZ
   C. Something else
```

- **NL** — shorthand meaning "reformat the most recent query in numbers-letters style"
- **NLR** — numbers-letters with recommendations. Present the options and mark which you'd pick and why. Two common formats (not exhaustive — use whatever format communicates the recommendation clearly):

  **Inline marker** — tag the recommended option directly:
  ```
  1. What kind of persistence?
     A. In-memory only
     B. Local file storage (SQLite, JSON) ← recommended
     C. Remote database
     D. Other — please specify
  ```

  **Rationale paragraph** — present options first, then a paragraph at the end with your recommendation and reasoning:
  ```
  1. What kind of persistence?
     A. In-memory only
     B. Local file storage (SQLite, JSON)
     C. Remote database
     D. Other — please specify

  Recommendation: B. This is a single-user CLI tool with modest data —
  SQLite gives you durability without infrastructure overhead. C is
  overkill until there's a multi-user requirement.
  ```

  Inline markers work well when the rationale is obvious, rationale paragraphs when the "why" matters. Other formats may fit other situations — the goal is clarity, not rigid adherence to these two.

  **NLR is different from the review prompt's "Recommendations" option.** NLR is the agent proactively marking its pick when presenting options (agent → user: "I recommend B"). The review prompt's Recommendations option is the user asking the agent to surface concerns after seeing completed work (user → agent: "tell me what you'd suggest"). Different direction of flow, different purpose.

**Formatting rule:** always wrap NL options in a **fenced code block** (triple backticks). Indent lettered options by 3 spaces from the number. Without the code block, markdown rendering collapses the indentation and the hierarchy is lost. This is not optional — without it, the numbered-lettered hierarchy is visually flat and hard to scan.

#### 2. Batch Answer Parsing

The user responds with codes: `1A, 2C, 3ok`. Parse and apply all answers at once.

Rules:
- Re-present the list with only **unanswered items remaining**
- **No answer = still open** — never assume approval for unanswered items
- "ok" on any item means approve as-is
- Partial batches are fine — the user can answer some now and some later

#### 3. One-by-One Mode (1b1)

The user says **"1b1"** or **"11"** — discuss each item sequentially instead of batching. Present one item, wait for the response, then present the next. Useful for items that need discussion before deciding.

#### 4. Single Decision = Letters Only

When there's only one question, drop the number and just use letters:

```
A. Duplicate the full section
   - Survives even if the file isn't present
   - More robust after compaction

B. Keep the reference
   - No drift risk between two copies
   - Lighter file
```

Numbers are only needed to batch multiple decision points. A single question with numbered prefix adds clutter.

#### 5. "Ok" as Universal Approval

"ok" means approve and move on. No elaboration needed. Works as a standalone response or within a batch (`3ok`).

### Principles

#### 6. Always Suggest Options, Never Ask Open-Ended

Don't make the user invent from scratch. When you need a decision, suggest 2-3 concrete options with an "Other" escape hatch. Open-ended questions ("what should we name this?") force the user to do generative work; options ("A. LogStream, B. EventPipe, C. Something else") let them do evaluative work, which is faster.

#### 7. Show Work, Then Recommend

Present content first for context, then proactively surface concerns or alternatives before asking for approval. The user sees the full picture before deciding.

Pattern: content → observations/concerns → recommendation → structured approval prompt.

#### 8. When Ambiguous, Ask

One clarification round-trip costs less than a wrong action. When the user's intent is unclear, present your best interpretations as lettered options rather than guessing.

---

## Bootstrap

When invoked on a project for the first time:

1. **Audit AGENTS.md and/or CLAUDE.md** — check for existing interaction conventions. Some projects already have informal versions of these patterns.

2. **Add interaction conventions section** — write the fast-chat conventions to AGENTS.md and/or CLAUDE.md. The section should be concise — a reference card, not a tutorial. Include:
   - NL/NLR/1b1 shorthands and what they mean
   - Batch answer format (`1A, 2C, 3ok`)
   - The "no answer = still open" rule
   - The standard review prompt
   - The "always suggest options" principle
   - Mark with `<!-- managed by /fast-chat -->`

3. **Inform the user** — explain the conventions briefly. Mention that NL, NLR, and 1b1 are voice-friendly shorthands they can use anytime.

Example AGENTS.md and/or CLAUDE.md section:

```
## Interaction Conventions
<!-- managed by /fast-chat -->

Use **numbers-letters style** when presenting choices — numbered questions, lettered
options, wrapped in fenced code blocks. Indent options 3 spaces from the number.

Shorthands:
- **NL** — reformat the most recent query in numbers-letters style
- **NLR** — numbers-letters with your recommendations
- **1b1** or **11** — discuss items one by one instead of batching

Batch answers: "1A, 2C, 3ok" — re-present with only unanswered items.
No answer = still open. Never assume approval.

When reviewing, use the standard review prompt: situational options adapted to
context, followed by Recommendations and Ok as the stable tail.
Always suggest concrete options — never ask open-ended questions when options are possible.
```

---

## Ongoing Operations

### When invoked on an existing project

When /fast-chat is invoked and conventions are already set up:

1. Show the current interaction conventions
2. Ask what the user wants to adjust — add shorthands, modify the review prompt, tweak formatting rules
3. Make the changes, preserving breadcrumbs

### Adapting to voice input

Voice-to-text users benefit most from fast-chat because:
- Single-character codes are easy to dictate ("one A, two B, three ok")
- Structured options eliminate the need to dictate long explanations
- NL/NLR/1b1 are pronounceable shorthands

If the project also uses `/dictation`, fast-chat shorthands (NL, NLR, 1b1) should be added to the dictation correction table so voice engines don't mangle them.

---

## What Does NOT Go in /fast-chat

- **Domain-specific option content** — /fast-chat defines the interaction format, not what options to present for any specific domain
- **Decision tracking** — /fast-chat structures how decisions are made; /notes captures what was decided
- **Task management** — structured options help make decisions, but tracking work items is a different concern
- **Dictation corrections** — /fast-chat defines the shorthands; /dictation maintains the correction table. They're complementary but separate

---

## How It Fits

```
Always-on behavior         → NL formatting, batch parsing, review prompts
                               (adopted immediately, no setup needed)

AGENTS.md and/or CLAUDE.md  → interaction conventions (persisted rules)
                               (bootstrapped on invocation for durability)

Shorthands (NL, NLR, 1b1)  → voice-friendly commands to switch modes
                               (user says "NLR", agent reformats)

Standard review prompt      → structured approval for any review cycle
                               (situational options + Recommend / Ok tail)
```

/fast-chat is the communication layer that makes every other skill's interactions faster. Without it, each decision is an open-ended conversation. With it, decisions are codes — precise, parseable, and fast enough for voice input.
