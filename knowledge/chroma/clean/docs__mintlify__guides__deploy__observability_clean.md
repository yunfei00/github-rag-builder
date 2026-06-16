---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/guides/deploy/observability.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/guides/deploy/observability.mdx
---
---
title: Observability
description: Monitor and trace your Chroma deployment with OpenTelemetry.
---

import { Callout } from '/snippets/callout.mdx';

## Backend Observability

Chroma is instrumented with OpenTelemetry hooks for observability.

"Telemetry" refers to anonymous product usage statistics we collect. "Observability" refers to metrics, logging, and tracing which can be used by anyone operating a Chroma deployment. Observability features listed on this page are **never** sent back to Chroma; they are for end-users to better understand how their Chroma deployment is behaving.

### Available Observability

Chroma currently only exports OpenTelemetry traces. Traces allow a Chroma operator to understand how requests flow through the system and quickly identify bottlenecks.

### Configuration

Tracing is configured with three environment variables:

- `CHROMA_OPEN_TELEMETRY__ENDPOINT`: where to send observability data. Example: `api.honeycomb.com`.
- `CHROMA_OPEN_TELEMETRY__SERVICE_NAME`: Service name for OTel traces. Default: `chromadb`.
- `OTEL_EXPORTER_OTLP_HEADERS`: Headers to use when sending observability data. Often used to send API and app keys. For example `{"x-honeycomb-team": "abc"}`.

We also have dedicated observability guides for various deployments:

- Docker
- AWS
- GCP
- Azure

## Client (SDK) Observability

Several observability platforms offer built-in integrations for Chroma, allowing you to monitor your application's interactions with the Chroma server:

- OpenLLMetry Integration.
- OpenLIT Integration.
