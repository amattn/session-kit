# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

### Interaction Style — Structured Options
Open-ended "anything else?" prompts were causing too many round-trips in review cycles. Added a convention to CLAUDE.md to use numbered options instead. This was previously attempted but didn't stick, so the instruction has been reinforced with clearer wording.
