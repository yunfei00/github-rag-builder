---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-quip/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-quip/README.md
---
# LlamaIndex Readers Integration: Quip

## Overview

The Quip Reader enables loading data from Quip documents. It constructs queries to retrieve thread content based on thread IDs.

### Installation

You can install the Quip Reader via pip:

```bash
pip install llama-index-readers-quip
```

### Usage

```python
from llama_index.readers.quip import QuipReader

# Initialize QuipReader
reader = QuipReader(access_token="")

# Load data from Quip
documents = reader.load_data(thread_ids=["", ""])
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
