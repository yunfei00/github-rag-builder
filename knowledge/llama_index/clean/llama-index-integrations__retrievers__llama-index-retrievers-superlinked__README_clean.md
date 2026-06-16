---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/retrievers/llama-index-retrievers-superlinked/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/retrievers/llama-index-retrievers-superlinked/README.md
---
# Llamaindex Superlinked Retriever

A LlamaIndex retriever integration for Superlinked, mirroring the structure of official LlamaIndex retriever packages.

Superlinked is a Python framework that let's you build full stack scalable AI search and recommendation apps by creating metadata aware embeddings and getting better use of your vector dbs. Superlinked uses an approach of mixture of encoders, where specalised encoders are used for different data types leading to more accurate retrieval.

## Installation

Option A (standalone dev):

```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip
pip install -e .
pip install pytest
```

Option B (monorepo): Add this directory under `llama-index-integrations/retrievers` and install with the monorepo tooling.

Note: Examples require Python 3.10–3.12 (Superlinked does not support Python 3.9).

## References and resources

- Superlinked framework repository: superlinked/superlinked
- Steam Games example article: read the article
- Open in Colab: Steam Games example notebook

## Usage

```python
from llama_index.retrievers.superlinked import SuperlinkedRetriever
from llama_index.core import QueryBundle

retriever = SuperlinkedRetriever(
    sl_client=app,  # Superlinked App
    sl_query=query_descriptor,  # Superlinked QueryDescriptor
    page_content_field="text",
    query_text_param="query_text",
    metadata_fields=None,
    top_k=4,
)

nodes = retriever.retrieve("What is a landmark in Paris?")
```

## Development

- Follows LlamaIndex contribution guidelines.
- Run tests: `pytest -q`.

## Testing without Superlinked

Tests use mocks for the `superlinked` imports so they can run without the dependency installed.

## Example

An end-to-end example is provided in `examples/steam_games_example.py`.
