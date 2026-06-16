---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/vector_stores/llama-index-vector-stores-bigquery/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/vector_stores/llama-index-vector-stores-bigquery/README.md
---

# LlamaIndex Vector_Stores Integration: BigQuery

Vector store index using Google BigQuery.
Supports efficient storage and querying of vector embeddings using BigQuery's native vector search capabilities.
For more information, see the official [BigQuery Vector Search Documentation](https://cloud.google.com/bigquery/docs/vector-search-intro)

## 🔐 Required IAM Permissions

To use this integration, ensure your account has the following permissions:

- `roles/bigquery.dataOwner` (BigQuery Data Owner)
- `roles/bigquery.dataEditor` (BigQuery Data Editor)

## 🔧 Installation

```bash
pip install llama-index-vector-stores-bigquery
```

## 💻 Example Usage

```python
from google.cloud.bigquery import Client
from llama_index.vector_stores.bigquery import BigQueryVectorStore

client = Client()

vector_store = BigQueryVectorStore(
    table_id="my_bigquery_table",
    dataset_id="my_bigquery_dataset",
    bigquery_client=client,
)
```
