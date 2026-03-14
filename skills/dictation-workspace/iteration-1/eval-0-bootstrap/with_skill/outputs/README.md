# KubeFlux

A Kubernetes-native event streaming platform built with gRPC and Protocol Buffers.

## Architecture

KubeFlux uses a custom CRD (FluxStream) to define event pipelines. Events flow through Envoy sidecars, get serialized via Protobuf, and land in either ClickHouse (analytics) or ScyllaDB (hot storage).

## Key Components

- **fluxctl** — CLI tool for managing FluxStream resources
- **flux-operator** — Kubernetes operator that reconciles FluxStream CRDs
- **flux-ingest** — gRPC service for event ingestion
- **flux-query** — GraphQL API for querying stored events

## Development

Requires: Go 1.22+, kubectl, Helm 3, Tilt for local dev.

```bash
tilt up          # start local cluster
fluxctl apply    # deploy FluxStream resources
make proto       # regenerate Protobuf stubs
```
