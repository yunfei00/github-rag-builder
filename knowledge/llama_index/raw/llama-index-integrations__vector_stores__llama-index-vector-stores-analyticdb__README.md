---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/vector_stores/llama-index-vector-stores-analyticdb/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/vector_stores/llama-index-vector-stores-analyticdb/README.md
---

# Analytic DB Vector Store

A LlamaIndex vector store using Analytic DB as the backend.

## Usage

Pre-requisite:

```bash
pip install llama-index-vector-stores-analyticdb
```

A minimal example:

```python
from llama_index.vector_stores.analyticdb import AnalyticDBVectorStore

vector_store = AnalyticDBVectorStore.from_params(
    access_key_id="your-ak",  # Your alibaba cloud ram access key id
    access_key_secret="your-sk",  # Your alibaba cloud ram access key secret
    region_id="cn-hangzhou",  #  Region id of the AnalyticDB instance
    instance_id="gp-ab123456",  # Your AnalyticDB instance id
    account="testaccount",  # Account of the AnalyticDB instance
    account_password="testpassword",  # Account password of the AnalyticDB instance
    namespace="llama",  # Schema name of the AnalyticDB instance
    collection="llama",  # Table name of the AnalyticDB instance
    namespace_password="llamapassword",  # Namespace corresponding password of the AnalyticDB instance
    metrics="cosine",  # Similarity algorithm, e.g. "cosine", "l2", "ip"
    embedding_dimension=1536,  # Embedding dimension of the embeddings model used
)
```

## More references

[AnalyticDB for PostgreSQL](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/product-overview/overview-product-overview) is a massively parallel processing (MPP) data warehousing service that is designed to analyze large volumes of data online.

A more detailed usage guide can be found [at this document](https://www.alibabacloud.com/help/en/analyticdb-for-postgresql/getting-started/instances-with-vector-engine-optimization-enabled/).
