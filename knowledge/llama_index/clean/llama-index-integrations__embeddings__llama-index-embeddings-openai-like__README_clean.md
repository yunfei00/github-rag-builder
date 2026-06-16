---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/embeddings/llama-index-embeddings-openai-like/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/embeddings/llama-index-embeddings-openai-like/README.md
---
# OpenAILike Embeddings

This integration allows you to use OpenAI-like embeddings APIs with LlamaIndex.

## Installation

```bash
pip install llama-index-embeddings-openai-like
```

## Usage

```python
from llama_index.embeddings.openai_like import OpenAILikeEmbedding

embedding = OpenAILikeEmbedding(
    model_name="my-model-name",
    api_key="fake",
    api_base="http://localhost:1234/v1",
    embed_batch_size=10,
)
```
