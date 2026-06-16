---
source: chroma
owner: chroma-core
repo: chroma
path: chromadb/telemetry/README.md
url: https://github.com/chroma-core/chroma/blob/main/chromadb/telemetry/README.md
---
# Telemetry

This directory holds all the telemetry for Chroma.

- `product/` contains anonymized product telemetry which we, Chroma, collect so we can
  understand usage patterns. For more information, see https://docs.trychroma.com/telemetry.
- `opentelemetry/` contains all of the config for Chroma's OpenTelemetry
  setup. These metrics are *not* sent back to Chroma -- anyone operating a Chroma instance
  can use the OpenTelemetry metrics and traces to understand how their instance of Chroma
  is behaving.
