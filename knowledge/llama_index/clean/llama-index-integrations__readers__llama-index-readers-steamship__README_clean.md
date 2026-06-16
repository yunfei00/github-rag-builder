---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-steamship/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-steamship/README.md
---
# LlamaIndex Readers Integration: SteamshipFile

## Overview

The SteamshipFile Reader allows you to load documents from persistent Steamship Files. Steamship is a platform for storing and managing files with advanced tagging capabilities.

For more detailed information about the SteamshipFile Reader, visit SteamShip.

### Installation

You can install the SteamshipFile Reader via pip:

```bash
pip install llama-index-readers-steamship
```

This reader requires steamship API key, which can be acquired from SteamShip.

### Usage

```python
from llama_index.readers.steamship import SteamshipFileReader

# Initialize SteamshipFileReader
reader = SteamshipFileReader(api_key="")

# Load data from persistent Steamship Files
documents = reader.load_data(
    workspace="",
    query="",
    file_handles=["smooth-valley-9kbdr"],
    collapse_blocks=True,
    join_str="\n\n",
)
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
