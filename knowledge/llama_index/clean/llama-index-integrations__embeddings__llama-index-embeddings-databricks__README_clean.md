---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/embeddings/llama-index-embeddings-databricks/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/embeddings/llama-index-embeddings-databricks/README.md
---
# LlamaIndex Embeddings Integration: Databricks

This integration adds support for embedding models hosted on the databricks platform via serving endpoints. The API follows the specifications of OpenAI, so this integration simply adapts the `llama-index-embeddings-openai` integration and internally uses the `openai` Python API library, too.

The signature furthermore aligns with the existing Databricks LLM integration with respect to the naming of the `model`, `api_key` and `endpoint` variables to ensure a smooth user experience.

## Installation

```
pip install llama-index
pip install llama-index-embeddings-databricks
```

## Usage

Passing the `api_key` and `endpoint` directly as arguments:

```python
import os
from llama_index.core import Settings
from llama_index.embeddings.databricks import DatabricksEmbedding

# Set up the DatabricksEmbedding class with the required model, API key and serving endpoint
embed_model = DatabricksEmbedding(
    model="databricks-bge-large-en",
    api_key="",
    endpoint="",
)
Settings.embed_model = embed_model

# Embed some text
embeddings = embed_model.get_text_embedding(
    "The DatabricksEmbedding integration works great."
)
```

Using environment variables:

```
export DATABRICKS_TOKEN=
export DATABRICKS_SERVING_ENDPOINT=
```

```python
import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.embeddings.databricks import DatabricksEmbedding

load_dotenv()
# Set up the DatabricksEmbedding class with the required model, API key and serving endpoint
embed_model = DatabricksEmbedding(model="databricks-bge-large-en")
Settings.embed_model = embed_model

# Embed some text
embeddings = embed_model.get_text_embedding(
    "The DatabricksEmbedding integration works great."
)
```
