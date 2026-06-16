---
source: dify
owner: langgenius
repo: dify
path: api/providers/README.md
url: https://github.com/langgenius/dify/blob/main/api/providers/README.md
---
# Providers

This directory holds **optional workspace packages** that plug into Dify’s API core. Providers are responsible for implementing the interfaces and registering themselves to the API core. Provider mechanism allows building the software with selected set of providers so as to enhance the security and flexibility of distributions.

## Developing Providers

- VDB Providers

## Tests

Provider tests often live next to the package, e.g. `providers///tests/unit_tests/`. Shared fixtures may live under `providers/` (e.g. `conftest.py`).

## Excluding Providers

In order to build with selected providers, use `--no-group vdb-all` and `--no-group trace-all` to disable default ones, then use `--group vdb-` and `--group trace-` to enable specific providers.
