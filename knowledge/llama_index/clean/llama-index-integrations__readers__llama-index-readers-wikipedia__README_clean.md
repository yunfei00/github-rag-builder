---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-wikipedia/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-wikipedia/README.md
---
# LlamaIndex Readers Integration: Wikipedia

## Overview

The Wikipedia Reader reads Wikipedia pages and retrieves their content. It allows you to specify a list of pages to read, and it retrieves the text content of each page.

### Installation

You can install the Wikipedia Reader via pip:

```bash
pip install llama-index-readers-wikipedia
```

### Usage

```python
from llama_index.readers.wikipedia import WikipediaReader

# Initialize WikipediaReader
reader = WikipediaReader()

# Load data from Wikipedia
documents = reader.load_data(pages=["Page Title 1", "Page Title 2", ...])
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
