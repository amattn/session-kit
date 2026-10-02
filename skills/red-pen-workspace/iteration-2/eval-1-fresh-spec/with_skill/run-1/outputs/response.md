Written to docs/rate_limiting.md.

Three items need an answer before it's buildable, each with my lean in the doc: the actual limit (I have no number except that 2k rps was too much; propose measuring from LB logs first), whether the mobile app is exempt (lean yes, otherwise one shared key throttles ~40k users as one client), and whether Redis being down allows or rejects (lean allow).

One thing to flag: docs/design.md proposes a per-IP in-process counter for export, which contradicts the Redis and per-API-key decisions in NOTES.md. The plan supersedes it; design.md itself is untouched.
