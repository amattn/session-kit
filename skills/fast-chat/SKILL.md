---
name: fast-chat
version: 0.2.0
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

The single highest-leverage pattern. When presenting work for review, replace open-ended "anything else?" with a structured prompt.

### Core rule: silence is not approval

**The review stays open until the user explicitly approves with O.** After executing any instruction (add, change, remove), re-present the item for further input. Do not treat the first instruction as implicit approval of everything else. The user may have more changes — wait for O.

This is the most important rule for review prompts. Without it, the agent races ahead after one instruction and the user loses control of the review.

Use the review prompt when presenting work for approval — artifacts, plans, decisions. Do not attach it to informational answers or explanations.

### The stable tail

Every review prompt ends with these two codes:

```
R. Show me recommendations
O. Ok, approve
```

**R** asks the agent to surface concerns or suggestions. In a review context, R always produces NL-formatted options (lettered choices), not prose paragraphs. The user wants to pick, not read.

**O** approves the current item and moves on. When a simple recommendation is displayed (e.g., "add GUI tools to the list"), O implicitly accepts it — no extra code needed. For non-trivial recommendations, the user engages with them directly (prose or picking from NL options) before saying O.

### Free-form input needs no prefix

The user just says what they want: "add X", "fix the wording on Y", "remove Z." No letter code required for instructions — prose is the default, not an option to select.

### How it works in practice

**Simple section review:**
```
Agent: [presents section]

   R. Show me recommendations
   O. Ok, approve

User: fix the typo in line 3
Agent: [fixes typo, re-presents section]

   R. Show me recommendations
   O. Ok, approve

User: O
```

**With recommendations (R produces NL-formatted options):**
```
Agent: [presents section]

   R. Show me recommendations
   O. Ok, approve

User: R
Agent: 1. Error handling for the timeout case
          A. Add try/catch with retry
          B. Add try/catch, fail fast
          C. Skip for now

       2. Variable naming
          A. Rename `data` to `response_payload`
          B. Keep as-is

       3. Retry logic
          A. Refactor to use exponential backoff
          B. Keep as-is

   R. Show me recommendations
   O. Ok, approve

User: 1A, 2B, 3 note for later review
Agent: [applies retry try/catch, keeps naming, notes retry logic for later, re-presents]
```

**Direction choice (situational options + tail):**
```
A. Keep the current approach
B. Try the alternative

R. Show me recommendations
O. Ok, approve
```

Situational options appear when the review involves a specific decision — the agent adapts the options to the context. The tail is always the same.

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

  **NLR is different from the review prompt's R code.** NLR is the agent proactively marking its pick when presenting options (agent → user: "I recommend B"). The review prompt's R is the user asking the agent to surface concerns after seeing completed work (user → agent: "give me recommendations"). Different direction of flow, different purpose.

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

When reviewing work, use the standard review prompt: present the item, then
the R/O stable tail (R. Show me recommendations, O. Ok, approve). Silence is not
approval — re-present after every change until the user says O.
R always produces NL-formatted options in review context.
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
                               (R/O tail, silence is not approval)
```

/fast-chat is the communication layer that makes every other skill's interactions faster. Without it, each decision is an open-ended conversation. With it, decisions are codes — precise, parseable, and fast enough for voice input.
