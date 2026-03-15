# /dictation — Quick Reference

**Setup:** Run `/dictation` in your project. It scans project jargon, proposes a correction table (focused on terms voice engines are likely to mangle), and writes the table to CLAUDE.md with a `<!-- managed by /dictation -->` breadcrumb.

**Ongoing:** Always-on — known corrections are applied silently. When input is garbled beyond the table, the agent presents disambiguation options instead of guessing. Your side:
- When the agent misinterprets a recurring term, say something like "add 'pleat' means 'plet' to the correction table" — or just correct it and the agent will offer to add it
- One-off typos don't need table entries; the table is for systematic, recurring patterns

**Example:**
```
You: push the jason config to the Maine branch and update the cloud API key
Agent: (silently corrects to "JSON config", "main branch", and "Claude API key",
        proceeds with the task)

You: we need to fix the pleet workflow
Agent: I'm not sure what "pleet" refers to. Did you mean:
       A. plet (the dev orchestrator)
       B. fleet (deployment fleet)
       C. Something else

You: A
Agent: Got it. Want me to add "pleet → plet" to the correction table?
```
