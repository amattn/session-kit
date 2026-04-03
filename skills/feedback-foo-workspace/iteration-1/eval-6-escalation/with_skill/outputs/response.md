SPI_2 keeps recurring because the original fix was too vague — "interaction conventions" is guidance that agents reinterpret each session and drift away from. This is the classic prose-didn't-stick escalation pattern.

Here's what I did:

1. **Replaced the vague convention with a structured Interaction Discipline in CLAUDE.md.** Four numbered, enforceable rules that name specific anti-patterns (no "anything else?", no splitting answers into multiple rounds, present numbered options instead of open-ended questions). Numbered rules with concrete anti-patterns are harder to drift from than general guidance.

2. **Updated SPI_2 in SHARPEN.md** to reflect the escalation — it's still in Open because we need to verify the discipline actually sticks in real sessions. The entry now documents the full history: resolved, reopened, escalated.

3. **Logged the decision in NOTES.md** so the rationale survives across sessions.

If the discipline still gets violated after a couple sessions, the next escalation step is a validation script that flags open-ended "anything else?" patterns in agent output — making compliance automatic rather than relying on prose interpretation.
