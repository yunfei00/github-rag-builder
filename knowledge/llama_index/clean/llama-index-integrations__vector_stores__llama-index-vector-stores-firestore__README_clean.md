---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/vector_stores/llama-index-vector-stores-firestore/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/vector_stores/llama-index-vector-stores-firestore/README.md
---
# LlamaIndex Vector_Store Integration: Firestore

A LlamaIndex vector store using Cloud Firestore as the backend.

## Usage

Pre-requisite:

```bash
pip install llama-index-vector-stores-firestore
```

Minimal example:

```python
from llama_index_vector_stores_firestore import FirestoreVectorStore

store = FirestoreVectorStore(
    collection_name=COLLECTION_NAME,
)
```

## More examples and references

Check out the notebook for detailed usage.
