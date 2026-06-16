---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-mbox/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-mbox/README.md
---
# LlamaIndex Readers Integration: Mbox

## Overview

Mbox Reader is a simple reader for mbox (mailbox) files, commonly used for storing email messages. It reads a set of emails saved in the mbox format and extracts them into documents.

### Installation

You can install Mbox Reader via pip:

```bash
pip install llama-index-readers-mbox
```

### Usage

```python
from llama_index.readers.mbox import MboxReader

# Initialize MboxReader
reader = MboxReader()

# Load data from mbox files in the input directory
documents = reader.load_data(input_dir="")
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
