# NOTES.md — inventory-api

## Project Context

REST API for managing inventory.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

## Session Continuity

If you are reading this file mid-session or after context compaction, also re-read `CLAUDE.md` to restore the full set of project conventions, interaction rules, and warmup instructions.
