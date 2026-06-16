---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-mongodb/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-mongodb/README.md
---
# LlamaIndex Readers Integration: Mongo

## Overview

Simple Mongo Reader allows loading data from a MongoDB database. It concatenates specified fields from each document into a single document used by LlamaIndex.

### Installation

You can install MongoDB Reader via pip:

```bash
pip install llama-index-readers-mongodb
```

### Usage

```python
from llama_index.readers.mongodb import SimpleMongoReader

# Initialize SimpleMongoReader
reader = SimpleMongoReader(
    host="",  # Mongo host address
    port=27017,  # Mongo port (default: 27017)
    uri="",  # Provide the URI if not using host and port
)

# Lazy load data from MongoDB
documents = reader.lazy_load_data(
    db_name="",  # Name of the database
    collection_name="",  # Name of the collection
    field_names=[
        "text"
    ],  # Names of the fields to concatenate (default: ["text"])
    separator="",  # Separator between fields (default: "")
    query_dict=None,  # Query to filter documents (default: None)
    max_docs=0,  # Maximum number of documents to load (default: 0)
    metadata_names=None,  # Names of the fields to add to metadata attribute (default: None)
)
```

Implementation for MongoDB reader can be found here

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
