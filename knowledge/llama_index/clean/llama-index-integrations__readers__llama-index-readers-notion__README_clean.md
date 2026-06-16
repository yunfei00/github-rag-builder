---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-notion/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-notion/README.md
---
# LlamaIndex Readers Integration: Notion

## Overview

Notion Page Reader enables loading data from Notion pages. It constructs queries to retrieve pages based on page IDs or from a specified Notion database.

### Installation

You can install Notion Reader via pip:

```bash
pip install llama-index-readers-notion
```

### Usage

```python
from llama_index.readers.notion import NotionPageReader

# Initialize NotionPageReader
reader = NotionPageReader(integration_token="")

# Load data from Notion
documents = reader.load_data(
    page_ids=["", ""],  # List of page IDs to load
    database_id="",  # Database ID from which to load page IDs
)
```

Implementation for Notion reader can be found here

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
