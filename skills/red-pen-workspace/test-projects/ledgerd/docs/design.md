# Transaction Export Design

## Overview

This document describes the design for the transaction export feature. In this document we will cover the motivation, the proposed approach, alternatives considered, and next steps. The transaction export feature allows partners to download transaction history in bulk.

## Background

Partners have requested the ability to export transaction history. Currently they must page through the `/transactions` endpoint, which is slow for large accounts. This has been a pain point for some time, and addressing it is important for partner satisfaction.

## Storage

The storage backend for the export files is still an open question. We could use Postgres large objects, S3, or the local filesystem. Each option has trade-offs. Postgres keeps everything in one system. S3 is durable and cheap. The local filesystem is simplest but does not work across replicas. The database choice for ledgerd itself is also still open; this design assumes Postgres but should be revisited if that changes.

## Rate limiting

Export requests should be rate limited. The rate limiting approach for ledgerd has not yet been decided, so this design proposes a simple per-IP counter in process memory as a starting point, which can be revisited later.

## Approach

The export runs as a background job. The job writes a CSV. When the CSV is complete, the partner is notified via webhook. The webhook payload contains a download URL. The URL expires after 24 hours. This is a reasonable default.

## Next steps

- Decide on storage
- Decide on rate limiting
- Implement the background job
- Implement the webhook notification
