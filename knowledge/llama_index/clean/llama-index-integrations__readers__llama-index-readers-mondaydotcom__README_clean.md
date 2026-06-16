---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-mondaydotcom/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-mondaydotcom/README.md
---
# Monday Loader

```bash
pip install llama-index-readers-mondaydotcom
```

This loader loads data from monday.com. The user specifies an API token to initialize the MondayReader. They then specify a monday.com board id to load in the corresponding Document objects.

## Usage

Here's an example usage of the MondayReader.

```python
from llama_index.readers.mondaydotcom import MondayReader

reader = MondayReader("")
documents = reader.load_data("")
```

Check out monday.com API docs - here

This loader is designed to be used as a way to load data into LlamaIndex. See here for examples.
