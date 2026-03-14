# NOTES.md — inventory-api

> **Reminder:** This file is institutional memory. Every decision made during a session MUST be recorded here immediately. After compaction or context recovery, re-read this file in full — it is your only source of truth for past decisions and rationale. See CLAUDE.md "NOTES.md Discipline" for the full protocol.

## Project Context

REST API for managing inventory.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.
