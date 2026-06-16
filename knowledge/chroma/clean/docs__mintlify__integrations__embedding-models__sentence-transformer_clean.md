---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/embedding-models/sentence-transformer.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/embedding-models/sentence-transformer.mdx
---
---
title: Sentence Transformer
---

import { Callout } from '/snippets/callout.mdx';

Chroma provides a convenient wrapper around the Sentence Transformers library. This embedding function runs locally and uses pre-trained models from Hugging Face.

This embedding function relies on the `sentence_transformers` python package, which you can install with `pip install sentence_transformers`.

```python
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

sentence_transformer_ef = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2",
    device="cpu",
    normalize_embeddings=False
)

texts = ["Hello, world!", "How are you?"]
embeddings = sentence_transformer_ef(texts)
```

You can pass in optional arguments:

- `model_name`: The name of the Sentence Transformer model to use (default: "all-MiniLM-L6-v2")
- `device`: Device used for computation, "cpu" or "cuda" (default: "cpu")
- `normalize_embeddings`: Whether to normalize returned vectors (default: False)

For a full list of available models, visit Sentence Transformers models on Hugging Face or SBERT documentation.

```typescript
// npm install @chroma-core/sentence-transformer

import { SentenceTransformersEmbeddingFunction } from "@chroma-core/sentence-transformer";

const sentenceTransformerEF = new SentenceTransformersEmbeddingFunction({
    modelName: "all-MiniLM-L6-v2",
    device: "cpu",
    normalizeEmbeddings: false,
});

const texts = ["Hello, world!", "How are you?"];
const embeddings = await sentenceTransformerEF.generate(texts);
```

Sentence Transformers are great for semantic search tasks. Popular models include `all-MiniLM-L6-v2` (fast and efficient) and `all-mpnet-base-v2` (higher quality). Visit SBERT documentation for more model recommendations.
