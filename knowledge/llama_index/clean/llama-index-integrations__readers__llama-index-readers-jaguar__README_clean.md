---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-jaguar/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-jaguar/README.md
---
# LlamaIndex Readers Integration: Jaguar

## Overview

Jaguar Reader retrieves documents from an existing persisted Jaguar store. These documents can then be used in a downstream LlamaIndex data structure.

### Installation

You can install Jaguar Reader via pip:

```bash
pip install llama-index-readers-jaguar
```

To use Jaguar Reader, you must have an API key. Here are the installation instructions

## Usage

```python
from llama_index.readers.jaguar import JaguarReader

# Initialize JaguarReader
reader = JaguarReader(
    pod="",
    store="",
    vector_index="",
    vector_type="",
    vector_dimension="",
    url="",
)

# Login to Jaguar server
reader.login(jaguar_api_key="")

# Load data from Jaguar
documents = reader.load_data(
    embedding="",
    k=10,
    metadata_fields=["", ""],
    where="",
)

# Logout from Jaguar server
reader.logout()
```

This loader is designed to be used as a way to load data into
LlamaIndex.
