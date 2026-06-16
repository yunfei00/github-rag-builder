---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-guru/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-guru/README.md
---
# Guru Loader

```bash
pip install llama-index-readers-guru
```

This loader loads documents from Guru. The user specifies a username and api key to initialize the GuruReader.

Note this is not your password. You need to create a new api key in the admin tab of the portal.

## Usage

Here's an example usage of the GuruReader.

```python
from llama_index.readers.guru import GuruReader

reader = GuruReader(username="", api_key="")

# Load all documents in a collection
documents = reader.load_data(
    collection_ids=["", ""]
)

# Load specific cards by card id
documents = reader.load_data(card_ids=["", ""])
```

This loader is designed to be used as a way to load data into LlamaIndex.
