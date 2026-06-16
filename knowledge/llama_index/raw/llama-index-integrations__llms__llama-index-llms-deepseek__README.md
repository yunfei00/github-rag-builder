---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/llms/llama-index-llms-deepseek/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-deepseek/README.md
---

# LlamaIndex Llms Integration: DeepSeek

This is the DeepSeek integration for LlamaIndex. Visit [DeepSeek](https://api-docs.deepseek.com/) for information on how to get an API key and which models are supported.

## Installation

```bash
pip install llama-index-llms-deepseek
```

## Usage

```python
from llama_index.llms.deepseek import DeepSeek

llm = DeepSeek(model="deepseek-chat", api_key="your-api-key")
```
