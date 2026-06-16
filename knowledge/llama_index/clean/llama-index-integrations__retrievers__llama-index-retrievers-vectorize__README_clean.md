---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/retrievers/llama-index-retrievers-vectorize/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/retrievers/llama-index-retrievers-vectorize/README.md
---
# LlamaIndex Retrievers Integration: Vectorize

> Vectorize RAG-as-a-Service handles the messy, hard parts of AI development,
> so you can focus on building your applications.

## Installation

```bash
pip install llama-index-retrievers-vectorize
```

### Usage

```python
from llama_index.retrievers.vectorize import VectorizeRetriever

retriever = VectorizeRetriever(
    api_token="...",
    organization="...",
    pipeline_id="...",
)
retriever.retrieve("query")
```
