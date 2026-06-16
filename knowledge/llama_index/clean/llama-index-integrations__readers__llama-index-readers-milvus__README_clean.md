---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-milvus/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-milvus/README.md
---
# LlamaIndex Readers Integration: Milvus

## Overview

Milvus Reader is designed to load data from a Milvus vector store, which provides search functionality based on query vectors. It retrieves documents from the specified Milvus collection using the provided connection parameters.

### Installation

You can install Milvus Reader via pip:

```bash
pip install llama-index-readers-milvus
```

### Usage

```python
from llama_index.readers.milvus import MilvusReader

# Initialize MilvusReader
reader = MilvusReader(
    host="",  # Milvus host address (default: "localhost")
    port=19530,  # Milvus port (default: 19530)
    user="",  # Milvus user (default: "")
    password="",  # Milvus password (default: "")
    use_secure=False,  # Use secure connection (default: False)
)

# Load data from Milvus
documents = reader.load_data(
    query_vector=[0.1, 0.2, 0.3],  # Query vector
    collection_name="",  # Name of the Milvus collection
    limit=10,  # Number of results to return
    search_params=None,  # Search parameters (optional)
)
```

Implementation for Milvus reader can be found here

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
