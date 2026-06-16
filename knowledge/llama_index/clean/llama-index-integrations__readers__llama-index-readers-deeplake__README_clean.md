---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-deeplake/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-deeplake/README.md
---
# LlamaIndex Readers Integration: Deeplake

## Overview

DeepLake Reader is a tool designed to retrieve documents from existing DeepLake datasets efficiently.

### Installation

You can install DeepLake Reader via pip:

```bash
pip install llama-index-readers-deeplake
```

To use Deeplake Reader, you must have an API key. Here are the installation instructions

## Usage

```python
from llama_index.core.schema import Document
from llama_index.readers.deeplake import DeepLakeReader

# Initialize DeepLakeReader with the token
reader = DeepLakeReader(token="")

# Load data from DeepLake
documents = reader.load_data(
    query_vector=[0.1, 0.2, 0.3],  # Query vector
    dataset_path="",  # Path to the DeepLake dataset
    limit=4,  # Number of results to return
    distance_metric="l2",  # Distance metric
)
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
