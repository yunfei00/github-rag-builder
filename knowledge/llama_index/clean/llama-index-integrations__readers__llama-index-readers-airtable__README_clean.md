---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-airtable/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-airtable/README.md
---
# Airtable Loader

```bash
pip install llama-index-readers-airtable
```

This loader loads documents from Airtable. The user specifies an API token to initialize the AirtableReader. They then specify a `table_id` and a `base_id` to load in the corresponding Document objects.

## Usage

Here's an example usage of the AirtableReader.

```python
import os

from llama_index.readers.airtable import AirtableReader

reader = AirtableReader("")
documents = reader.load_data(table_id="", base_id="")
```

This loader is designed to be used as a way to load data into LlamaIndex.
