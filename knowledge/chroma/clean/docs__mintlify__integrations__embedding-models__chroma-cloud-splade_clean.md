---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/embedding-models/chroma-cloud-splade.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/embedding-models/chroma-cloud-splade.mdx
---
---
title: Chroma Cloud Splade
---

import { Callout } from '/snippets/callout.mdx';

Chroma provides a convenient wrapper around Chroma Cloud's Splade sparse embedding API. This embedding function runs remotely on Chroma Cloud's servers, and requires a Chroma API key. You can get an API key by signing up for an account at Chroma Cloud.

Sparse embeddings are useful for retrieval tasks where you want to match on specific keywords or terms, rather than semantic similarity.

This embedding function relies on the `httpx` python package, which you can install with `pip install httpx`.

```python
from chromadb.utils.embedding_functions import ChromaCloudSpladeEmbeddingFunction, ChromaCloudSpladeEmbeddingModel
import os

os.environ["CHROMA_API_KEY"] = "YOUR_API_KEY"
splade_ef = ChromaCloudSpladeEmbeddingFunction(
    model=ChromaCloudSpladeEmbeddingModel.SPLADE_PP_EN_V1
)

texts = ["Hello, world!", "How are you?"]
sparse_embeddings = splade_ef(texts)
```

You can optionally pass in a `model` argument. By default, Chroma uses `prithivida/Splade_PP_en_v1`.

```typescript
// npm install @chroma-core/chroma-cloud-splade

import { ChromaCloudSpladeEmbeddingFunction, ChromaCloudSpladeEmbeddingModel } from "@chroma-core/chroma-cloud-splade";

const embedder = new ChromaCloudSpladeEmbeddingFunction({
  apiKeyEnvVar: "CHROMA_API_KEY", // Or set CHROMA_API_KEY env var
  model: ChromaCloudSpladeEmbeddingModel.SPLADE_PP_EN_V1,
});

// use directly
const sparseEmbeddings = await embedder.generate(["document1", "document2"]);
```

To use the Chroma Cloud Embedding API directly, see the Generate Sparse Embeddings API reference for detailed request and response formats.
