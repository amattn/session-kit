# SPI_2: Review cycles — why the fix didn't stick, and what to do next

## Diagnosis

SPI_2 was resolved in session 5 by adding interaction conventions to CLAUDE.md, but it recurred in sessions 7 and 8. That pattern — fix documented, behavior unchanged — usually means one of three things:

1. **The instruction is too vague.** "Interaction conventions" may describe the goal without specifying the exact behavior change. If the instruction says something like "use structured options," the agent has room to interpret that loosely and fall back to the "anything else?" habit.

2. **The instruction is in the wrong place.** CLAUDE.md rules work best when they're close to the point of action. If the convention is buried in a general section, it may not activate when the agent is mid-review and deciding how to present options.

3. **The instruction lacks a concrete format.** Without a template or example, each session re-invents what "structured options" looks like, and some sessions drift back to the open-ended pattern.

## Recommended next steps

**A. Strengthen the CLAUDE.md instruction.** Replace the current interaction convention with something specific and testable. For example:

> When presenting review feedback or choices, use a numbered list of concrete options. Do not ask open-ended "anything else?" — instead, present all identified items in a single structured pass.

**B. Add a checkpoint format.** Give the agent a template to follow:

> After completing a task, present a summary in this format:
> - What was done (1-2 lines)
> - Remaining items (numbered list, or "none")
> - Recommended next step
>
> Do not prompt with "anything else?" or equivalent open-ended questions.

**C. Track whether the strengthened fix holds.** Keep SPI_2 open with a note that the escalation strategy is "stronger instruction + concrete template." If it recurs again after this, the next escalation would be to add it as a hard constraint (e.g., a lint-like check or a pre-response checklist the agent must follow).

## Why this is an escalation, not just a re-fix

The first fix ("add interaction conventions") addressed the *what*. This fix addresses the *how* — giving a concrete template rather than a general directive. If a pattern survives one round of documentation, the next round needs to be more specific and more structural, not just a rewording of the same idea.
