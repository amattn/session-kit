# NOTES.md — inventory-api

## Project Context

REST API for managing inventory. Python/FastAPI/PostgreSQL.

## Key Design Decisions

### Database — PostgreSQL
Chose over SQLite for concurrent write support.

## Process

### SPI_2 escalated — prose convention replaced with discipline
The interaction conventions added in session 5 didn't prevent the "anything else?" pattern from recurring (sessions 7, 8). Escalated per /sharpen guidance: replaced vague prose with a numbered Interaction Discipline in CLAUDE.md. The discipline names specific anti-patterns and enforceable rules. If it still drifts, next escalation is a validation script.
