---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-trello/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-trello/README.md
---
# Trello Loader

```bash
pip install llama-index-readers-trello
```

This loader loads documents from Trello. The user specifies an API key and API token to initialize the TrelloReader. They then specify a board_id to
load in the corresponding Document objects representing Trello cards.

## Usage

Here's an example usage of the TrelloReader.

```python
import os

from llama_index.readers.trello import TrelloReader

reader = TrelloReader("", "")
documents = reader.load_data(board_id="")
```

This loader is designed to be used as a way to load data into LlamaIndex and/or subsequently used as a Tool in a LangChain Agent. See here for
examples.
