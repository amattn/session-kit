# CLAUDE.md

## Project

inventory-api — A REST API for managing inventory.

## Quick Start

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

## Session Warmup

At the start of every session, read the following files to establish context:

1. **This file (`CLAUDE.md`)** — project overview, conventions, and session instructions.
2. **`README.md`** — project description and setup instructions.

These files are small and should always be loaded in full. They provide the minimum context needed to work productively on this project.

## Compaction Resilience

If context compaction occurs mid-session, re-read this file (`CLAUDE.md`) to restore essential project knowledge. The key facts to preserve across compaction:

- This is a Python REST API project using **uvicorn** and (likely) **FastAPI**.
- Dependencies are managed via `requirements.txt`.
- The app entrypoint is `main:app`.

## Conventions

- Follow existing code style and patterns found in the codebase.
- When making changes, check for related tests and update them accordingly.
