---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-json/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-json/README.md
---
# LlamaIndex Readers Integration: Json

## Overview

JSON Reader reads JSON documents with options to help extract relationships between nodes. It provides functionalities to control the depth of JSON traversal, collapse long JSON fragments, and clean JSON structures.

### Installation

You can install JSON Reader via pip:

```bash
pip install llama-index-readers-json
```

## Usage

```python
from llama_index.readers.json import JSONReader

# Initialize JSONReader
reader = JSONReader(
    # The number of levels to go back in the JSON tree. Set to 0 to traverse all levels. Default is None.
    levels_back="",
    # The maximum number of characters a JSON fragment would be collapsed in the output. Default is None.
    collapse_length="",
    # If True, ensures that the output is ASCII-encoded. Default is False.
    ensure_ascii="",
    # If True, indicates that the file is in JSONL (JSON Lines) format. Default is False.
    is_jsonl="",
    # If True, removes lines containing only formatting from the output. Default is True.
    clean_json="",
)

# Load data from JSON file
documents = reader.load_data(input_file="", extra_info={})
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
