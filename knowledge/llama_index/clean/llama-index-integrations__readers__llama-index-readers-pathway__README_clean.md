---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-pathway/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-pathway/README.md
---
# LlamaIndex Readers Integration: Pathway

## Overview

Pathway Reader is a utility class for retrieving documents from the Pathway data indexing pipeline. It queries the Pathway vector store to get the closest neighbors of a given text query.

### Installation

You can install Pathway Reader via pip:

```bash
pip install llama-index-readers-pathway
```

### Usage

```python
from llama_index.readers.pathway import PathwayReader

# Initialize PathwayReader with the URI and port of the Pathway server
reader = PathwayReader(host="", port="")

# Load data from Pathway
documents = reader.load_data(
    query_text="",  # The text to get the closest neighbors of
    k=4,  # Number of results to return
    metadata_filter="",  # Filter to be applied
)
```

This loader is designed to be used as a way to load data into
LlamaIndex.
