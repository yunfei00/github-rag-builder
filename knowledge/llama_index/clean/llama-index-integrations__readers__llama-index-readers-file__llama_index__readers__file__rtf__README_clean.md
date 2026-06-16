---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/rtf/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/rtf/README.md
---
# RTF (Rich Text Format) Loader

This loader strips all RTF formatting from file and create a Document.

## Usage

To use this loader, you need to pass a `Path` object or a `str` to a local file.

```python
from pathlib import Path
from llama_index import download_loader

RTFReader = download_loader("RTFReader")

loader = RTFReader()
documents = RTFReader().load_data(file=Path("./example.rtf"))
```

This loader is designed to be used as a way to load data into LlamaIndex.
