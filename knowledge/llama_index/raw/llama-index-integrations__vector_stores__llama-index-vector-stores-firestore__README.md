---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/vector_stores/llama-index-vector-stores-firestore/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/vector_stores/llama-index-vector-stores-firestore/README.md
---

# LlamaIndex Vector_Store Integration: Firestore

<a href="https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/vector_stores/FirestoreVectorStore.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

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

Check out the [notebook](https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/vector_stores/FirestoreVectorStore.ipynb) for detailed usage.
