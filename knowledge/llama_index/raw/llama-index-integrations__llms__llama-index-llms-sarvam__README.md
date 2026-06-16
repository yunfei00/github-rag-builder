---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/llms/llama-index-llms-sarvam/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-sarvam/README.md
---

# LlamaIndex Llms Integration: Sarvam

This is the Sarvam integration for LlamaIndex. Visit [Sarvam](https://docs.sarvam.ai/api-reference-docs/chat/completions) for information on how to get an API key and which models are supported.

## Installation

```bash
pip install llama-index-llms-sarvam
```

## Usage

```python
from llama_index.llms.sarvam import Sarvam

llm = Sarvam(model="sarvam-m", api_key="your-api-key")
```
