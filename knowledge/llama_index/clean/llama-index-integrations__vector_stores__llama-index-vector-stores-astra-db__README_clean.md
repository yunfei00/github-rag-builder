---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/vector_stores/llama-index-vector-stores-astra-db/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/vector_stores/llama-index-vector-stores-astra-db/README.md
---
# Astra DB Vector Store

A LlamaIndex vector store using Astra DB as the backend.

## Usage

Pre-requisite:

```bash
pip install llama-index-vector-stores-astra-db
```

A minimal example:

```python
from llama_index.vector_stores.astra_db import AstraDBVectorStore

vector_store = AstraDBVectorStore(
    token="AstraCS:xY3b...",  # Your Astra DB token
    api_endpoint="https://012...abc-us-east1.apps.astra.datastax.com",  # Your Astra DB API endpoint
    collection_name="astra_v_table",  # Table name of your choice
    embedding_dimension=1536,  # Embedding dimension of the embeddings model used
)
```

## More examples and references

A more detailed usage guide can be found
at this demo notebook
in the LlamaIndex docs.

> **Note**: Please see the AstraDB documentation here.
