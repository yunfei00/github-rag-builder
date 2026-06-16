---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-qdrant/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-qdrant/README.md
---
# LlamaIndex Readers Integration: Qdrant

## Overview

The Qdrant Reader allows you to retrieve documents from existing Qdrant collections. Qdrant is a similarity search engine that helps you efficiently search and retrieve similar items from large datasets based on vector embeddings.

For more detailed information about Qdrant, visit Qdrant

### Installation

You can install the Qdrant Reader via pip:

```bash
pip install llama-index-readers-qdrant
```

### Usage

```python
from llama_index.readers.qdrant import QdrantReader

# Initialize QdrantReader
reader = QdrantReader(
    location="",
    url="",
    port="",
    grpc_port="",
    prefer_grpc="",
    https="",
    api_key="",
    prefix="",
    timeout="",
    host="",
)

# Load data from Qdrant
documents = reader.load_data(
    collection_name="",
    query_vector=[0.1, 0.2, 0.3],
    should_search_mapping={"text_field": "text"},
    must_search_mapping={"text_field": "text"},
    must_not_search_mapping={"text_field": "text"},
    rang_search_mapping={"text_field": {"gte": 0.1, "lte": 0.2}},
    limit=10,
)
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
