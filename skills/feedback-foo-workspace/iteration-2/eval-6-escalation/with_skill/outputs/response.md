# Response — FOO_2 Escalation

## What I did

FOO_2 ("review cycles take too many round-trips") was resolved in session 5 with interaction conventions added to CLAUDE.md, but the fix didn't hold — the pattern recurred in sessions 7 and 8. This is the escalation signal /foo watches for: a resolved entry that keeps coming back means the fix wasn't strong enough.

### Actions taken

1. **Escalated the fix from directive to discipline.** The original fix was a paragraph of interaction conventions — prose that agents re-interpreted each session and drifted away from. Replaced it with a **Review Interaction Discipline**: numbered, imperative rules that are concrete enough to verify compliance.

2. **Updated FEEDBACK_FOO.md** — added `[escalated]` status to FOO_2 with a pointer to the new discipline in CLAUDE.md. The entry stays Open until we confirm the discipline holds in real sessions.

3. **Updated NOTES.md** — captured the escalation decision and rationale: why the directive failed, why a discipline is the right next step, and what the further escalation path would be (tooling) if the discipline also doesn't stick.

4. **Updated CLAUDE.md** — added the "Review Interaction Discipline" block with four enforceable rules replacing the softer convention.

## What I would say to the user

"FOO_2 keeps recurring because the original fix was too soft — a paragraph of conventions that agents re-interpret and drift from each session. I've escalated it to a named discipline in CLAUDE.md with four concrete, numbered rules: gather all feedback before responding, present it as a structured list, end with a clear verdict instead of 'anything else?', and don't reopen the review loop on clarifying questions.

The FEEDBACK_FOO.md entry is marked `[escalated]` and stays Open until we confirm the discipline holds across a couple of sessions. If it still doesn't stick after that, the next step would be tooling — a review prompt template that makes the structured format automatic rather than relying on prose instructions."
