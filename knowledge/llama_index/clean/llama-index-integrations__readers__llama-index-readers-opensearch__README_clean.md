---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-opensearch/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-opensearch/README.md
---
# Opensearch Loader

```bash
pip install llama-index-readers-opensearch
```

The Opensearch Loader returns a set of texts corresponding to documents retrieved from an Opensearch index.
The user initializes the loader with an Opensearch index. They then pass in a field, and optionally a JSON query DSL object to fetch the fields they want.

## Usage

Here's an example usage of the OpensearchReader to load 100 documents.

```python
from llama_index.readers.opensearch import OpensearchReader

reader = OpensearchReader(
    host="localhost",
    port=9200,
    index="",
    basic_auth=("", ""),
)

query = {"size": 100, "query": {"match_all": {}}}
documents = reader.load_data(
    "", query=query, embedding_field="field_name"
)
```

This loader is designed to be used as a way to load data into LlamaIndex.
