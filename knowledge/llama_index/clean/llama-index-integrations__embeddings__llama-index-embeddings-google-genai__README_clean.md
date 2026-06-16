---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/embeddings/llama-index-embeddings-google-genai/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/embeddings/llama-index-embeddings-google-genai/README.md
---
# Google GenAI Embeddings

This package provides a wrapper around the Google GenAI API, allowing you to use Gemini and Vertex AI embeddings in your projects.

## Installation

```bash
pip install llama-index-embeddings-google-genai
```

## Usage

```python
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

embed_model = GoogleGenAIEmbedding(model_name="gemini-embedding-2-preview")

embeddings = embed_model.get_text_embedding("Hello, world!")
print(embeddings)
```

## Vertex AI

```python
embed_model = GoogleGenAIEmbedding(
    model_name="gemini-embedding-2-preview",
    vertexai_config={
        "project": "your-project-id",
        "location": "your-location",
    },
)
```
