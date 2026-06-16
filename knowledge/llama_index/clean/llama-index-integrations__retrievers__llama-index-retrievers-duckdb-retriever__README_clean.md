---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/retrievers/llama-index-retrievers-duckdb-retriever/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/retrievers/llama-index-retrievers-duckdb-retriever/README.md
---
# LlamaIndex Retrievers Integration: DuckDBRetriever

`pip install llama-index-retrievers-duckdb-retriever.`

## What is this?

This is a BM25 Retriever for DuckDB that can be used with LlamaIndex to enable full-text search.

## How to use

This was created with reference to DuckDB Full-Text Search Extension, so it's mostly the same.

Please refer to that.

However, while `DuckDBVectorStore` is an VectorStore, `DuckDBRetriever` is a Retriever.

DuckDBRetriever Example:

```python
from llama_index.retrievers.duckdb_retriever import DuckDBRetriever

retriever = DuckDBRetriever(database_name="vector.db", persist_dir="duckdb")
nodes = retriever.retrieve("retrieve_query")
```
