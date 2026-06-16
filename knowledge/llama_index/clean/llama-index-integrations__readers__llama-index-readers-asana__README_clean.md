---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-asana/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-asana/README.md
---
# Asana Loader

```bash
pip install llama-index-readers-asana
```

This loader loads documents from Asana. The user specifies an API token to initialize the AsanaReader. They then specify a `workspace_id` OR a `project_id` to load in the corresponding Document objects.

## Usage

Here's an example usage of the AsanaReader.

```python
import os

from llama_index.readers.asana import AsanaReader

reader = AsanaReader("")

# Option 1
documents = reader.load_data(workspace_id="")

# Option 2
documents = reader.load_data(project_id="")
```

This loader is designed to be used as a way to load data into LlamaIndex.
