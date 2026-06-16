---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/retrievers/llama-index-retrievers-mongodb-atlas-bm25-retriever/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/retrievers/llama-index-retrievers-mongodb-atlas-bm25-retriever/README.md
---

# LlamaIndex Retrievers Integration: MongoDBAtlasBM25Retriever

## What is this?

This is a BM25 Retriever for MongoDB Atlas that can be used with LlamaIndex.

## How to use

This was created with reference to [MongoDBAtlasVectorSearch](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MongoDBAtlasVectorSearch.html), so it's mostly the same.

Please refer to that.

However, while `MongoDBAtlasVectorSearch` is an VectorStore, `MongoDBAtlasBM25Retriever` is a Retriever.

MongoDBAtlasBM25Retriever Example:

```python
mongodb_client = pymongo.MongoClient(mongo_uri)

retriever = MongoDBAtlasBM25Retriever(
    mongodb_client=mongodb_client,
    db_name="vectorstore",
    collection_name="vector_collection",
    index_name="index_vector_collection",
)
nodes = retriever.retrieve("retrieve_query")
```
