---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/embeddings/llama-index-embeddings-oci-data-science/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/embeddings/llama-index-embeddings-oci-data-science/README.md
---
# LlamaIndex Embeddings Integration: Oracle Cloud Infrastructure (OCI) Data Science Service

Oracle Cloud Infrastructure (OCI) Data Science is a fully managed, serverless platform for data science teams to build, train, and manage machine learning models in Oracle Cloud Infrastructure.

It offers AI Quick Actions, which can be used to deploy embedding models in OCI Data Science. AI Quick Actions target users who want to quickly leverage the capabilities of AI. They aim to expand the reach of foundation models to a broader set of users by providing a streamlined, code-free, and efficient environment for working with foundation models. AI Quick Actions can be accessed from the Data Science Notebook.

Detailed documentation on how to deploy embedding models in OCI Data Science using AI Quick Actions is available here and here.

## Installation

Install the required packages:

```bash
pip install oracle-ads llama-index-core llama-index-embeddings-oci-data-science

```

The oracle-ads is required to simplify the authentication within OCI Data Science.

## Authentication

The authentication methods supported for LlamaIndex are equivalent to those used with other OCI services and follow the standard SDK authentication methods, specifically API Key, session token, instance principal, and resource principal. More details can be found here. Make sure to have the required policies to access the OCI Data Science Model Deployment endpoint.

## Usage

```bash
import ads
from llama_index.embeddings.oci_data_science import OCIDataScienceEmbedding

ads.set_auth(auth="security_token", profile="")

embedding = OCIDataScienceEmbedding(
    endpoint="https:///predict",
)

e1 = embeddings.get_text_embedding("This is a test document")
print(e1)

e2 = embeddings.get_text_embedding_batch([
        "This is a test document",
        "This is another test document"
    ])
print(e2)
```

## Async

```bash
import ads
from llama_index.embeddings.oci_data_science import OCIDataScienceEmbedding

ads.set_auth(auth="security_token", profile="")

embedding = OCIDataScienceEmbedding(
    endpoint="https:///predict",
)

e1 = await embeddings.aget_text_embedding("This is a test document")
print(e1)

e2 = await embeddings.aget_text_embedding_batch([
        "This is a test document",
        "This is another test document"
    ])
print(e2)
```

## More examples

https://docs.llamaindex.ai/en/stable/examples/embeddings/oci_data_science/
