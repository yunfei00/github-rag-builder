---
source: chroma
owner: chroma-core
repo: chroma
path: examples/observability/README.md
url: https://github.com/chroma-core/chroma/blob/main/examples/observability/README.md
---
# Observability

## Local Observability Stack

To run the Chroma with local observability stack (OpenTelemetry + Zipkin),
run the following command from the root of the repository:

```bash
docker compose -f examples/observability/docker-compose.local-observability.yml up --build -d
```
