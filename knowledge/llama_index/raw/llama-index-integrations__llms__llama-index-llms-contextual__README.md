---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/llms/llama-index-llms-contextual/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-contextual/README.md
---

# Contextual LLM Integration for LlamaIndex

This package provides a Contextual LLM integration for LlamaIndex.

## Installation

```bash
pip install llama-index-llms-contextual
```

## Usage

```python
from llama_index.llms.contextual import Contextual

llm = Contextual(model="contextual-clm", api_key="your_api_key")

response = llm.complete("Explain the importance of Grounded Language Models.")
```

See [Colab Notebook](https://colab.research.google.com/github/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-contextual/llama_index/llms/contextual/test-contextual.ipynb) for more examples.
