---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-dad-jokes/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-dad-jokes/README.md
---

# DadJoke Loader

```bash
pip install llama-index-readers-dad-jokes
```

This loader fetches a joke from icanhazdadjoke.

## Usage

To use this loader, load it.

```python
from llama_index.readers.dad_jokes import DadJokesReader

loader = DadJokesReader()
documents = loader.load_data()
```

This loader is designed to be used as a way to load data into [LlamaIndex](https://github.com/run-llama/llama_index/).
