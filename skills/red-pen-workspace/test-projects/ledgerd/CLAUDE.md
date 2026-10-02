# CLAUDE.md

## Required Reading

Load these files at the start of every session:

- `NOTES.md` — institutional memory (decisions, rationale)

## Project

ledgerd — a Python (FastAPI) HTTP API that serves account balances and transaction history to a mobile app and to partner integrations. Postgres for storage, Redis for caching. Deployed as three replicas behind a load balancer.

## Key Files

- `src/api/` — route handlers
- `src/webhook_client.py` — outbound webhook delivery to partners
- `docs/` — design notes
