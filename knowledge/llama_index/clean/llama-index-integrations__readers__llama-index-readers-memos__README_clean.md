---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-memos/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-memos/README.md
---
# Memos Loader

```bash
pip install llama-index-readers-memos
```

This loader fetches text from self-hosted memos.

## Usage

To use this loader, you need to specify the host where memos is deployed. If you need to filter, pass the corresponding parameter in `load_data`.

```python
from llama_index.readers.memos import MemosReader

loader = MemosReader("https://demo.usememos.com/")
documents = loader.load_data({"creatorId": 101})
```

This loader is designed to be used as a way to load data into LlamaIndex.
