---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/embedding-models/superlinked.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/embedding-models/superlinked.mdx
---
---
title: Superlinked
---

Superlinked is a self-hosted inference engine (SIE) for embedding, reranking, and extraction. The `sie-chroma` package exposes SIE as a Chroma `EmbeddingFunction`, giving you access to 85+ dense and sparse text embedding models from a single endpoint. You need a running SIE instance; see the Superlinked quickstart for deployment options.

Install the `sie-chroma` package:

```bash
pip install sie-chroma
```

Use `SIEEmbeddingFunction` for dense embeddings:

```python
import chromadb
from sie_chroma import SIEEmbeddingFunction

embedding_function = SIEEmbeddingFunction(
    base_url="http://localhost:8080",
    model="BAAI/bge-m3",
)

client = chromadb.Client()
collection = client.create_collection(
    name="documents",
    embedding_function=embedding_function,
)

collection.add(
    documents=[
        "Machine learning is a subset of artificial intelligence.",
        "Neural networks are inspired by biological neurons.",
        "Deep learning uses multiple layers of neural networks.",
    ],
    ids=["doc1", "doc2", "doc3"],
)

results = collection.query(query_texts=["What is deep learning?"], n_results=2)
```

For hybrid search on Chroma Cloud, `SIESparseEmbeddingFunction` returns learned sparse vectors (SPLADE / BGE-M3) as `dict[int, float]`:

```python
from sie_chroma import SIESparseEmbeddingFunction

sparse_ef = SIESparseEmbeddingFunction(
    base_url="http://localhost:8080",
    model="naver/splade-v3",
)
```

```bash
npm install @superlinked/sie-chroma
```

```typescript
import { ChromaClient } from "chromadb";
import { SIEEmbeddingFunction } from "@superlinked/sie-chroma";

const embedder = new SIEEmbeddingFunction({
  baseUrl: "http://localhost:8080",
  model: "BAAI/bge-m3",
});

const client = new ChromaClient();
const collection = await client.createCollection({
  name: "documents",
  embeddingFunction: embedder,
});

await collection.add({
  ids: ["doc1", "doc2", "doc3"],
  documents: [
    "Machine learning is a subset of artificial intelligence.",
    "Neural networks are inspired by biological neurons.",
    "Deep learning uses multiple layers of neural networks.",
  ],
});

const results = await collection.query({
  queryTexts: ["What is deep learning?"],
  nResults: 2,
});
```

## Multimodal

Chroma's `EmbeddingFunction` protocol accepts text input only. For image embedding with SIE-supported multimodal models (CLIP, SigLIP, ColPali), use the SIE SDK directly to pre-compute embeddings and pass them to Chroma via `collection.add(embeddings=...)`:

```python
from sie_sdk import SIEClient
from sie_sdk.types import Item
import chromadb

sie = SIEClient("http://localhost:8080")
chroma = chromadb.Client()
collection = chroma.create_collection("images")

results = sie.encode(
    "openai/clip-vit-large-patch14",
    [Item(images=["img1.jpg"]), Item(images=["img2.jpg"])],
    output_types=["dense"],
)

collection.add(
    ids=["img1", "img2"],
    embeddings=[r["dense"].tolist() for r in results],
    metadatas=[{"path": "img1.jpg"}, {"path": "img2.jpg"}],
)
```

## Links

- `sie-chroma` on PyPI
- `@superlinked/sie-chroma` on npm
- Superlinked on GitHub
- Superlinked docs
