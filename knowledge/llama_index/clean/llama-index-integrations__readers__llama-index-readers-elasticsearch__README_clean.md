---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-elasticsearch/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-elasticsearch/README.md
---
# LlamaIndex Readers Integration: Elasticsearch

## Overview

Elasticsearch (or Opensearch) Reader over REST API is a tool designed to read documents from an Elasticsearch or Opensearch index using the basic search API. These documents can then be utilized in downstream LlamaIndex data structures.

### Installation

You can install Elasticsearch (or Opensearch) Reader via pip:

```bash
pip install llama-index-readers-elasticsearch
```

## Usage

```python
from llama_index.core.schema import Document
from llama_index.readers.elasticsearch import ElasticsearchReader

# Initialize ElasticsearchReader
reader = ElasticsearchReader(
    endpoint="",
    index="",
    httpx_client_args={
        "timeout": 10
    },  # Optional additional arguments for the httpx.Client
)

# Load data from Elasticsearch
documents = reader.load_data(
    field="",  # Field in the document to retrieve text from
    query={"query": {"match_all": {}}},  # Elasticsearch JSON query DSL object
    embedding_field="",  # Field for embeddings (optional)
)
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
