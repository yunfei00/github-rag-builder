---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-weaviate/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-weaviate/README.md
---
# LlamaIndex Readers Integration: Weaviate

## Overview

The Weaviate Reader retrieves documents from Weaviate through vector lookup. It allows you to specify a class name and properties to retrieve from documents, or to provide a custom GraphQL query. You can choose to receive separate Document objects per document or concatenate retrieved documents into one Document.

### Installation

You can install the Weaviate Reader via pip:

```bash
pip install llama-index-readers-weaviate
```

### Usage

```python
from llama_index.readers.weaviate import WeaviateReader

# Initialize WeaviateReader with host and optional authentication
reader = WeaviateReader(
    host="", auth_client_secret=""
)

# Load data from Weaviate
documents = reader.load_data(
    class_name="", properties=["property 1", "property 2"]
)
```

You can follow this tutorial to learn more on how to use Weaviate Reader

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
