---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/embedding-models/mistral.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/embedding-models/mistral.mdx
---
---
title: Mistral
---

Chroma provides a convenient wrapper around Mistral's embedding API. This embedding function runs remotely on Mistral's servers, and requires an API key. You can get an API key by signing up for an account at Mistral.

This embedding function relies on the `mistralai` python package, which you can install with `pip install mistralai`.

```python
from chromadb.utils.embedding_functions import MistralEmbeddingFunction
import os

os.environ["MISTRAL_API_KEY"] = "************"
mistral_ef  = MistralEmbeddingFunction(model="mistral-embed")
mistral_ef(input=["document1","document2"])
```

```typescript
// npm install @chroma-core/mistral

import { MistralEmbeddingFunction } from "@chroma-core/mistral";

const embedder = new MistralEmbeddingFunction({
    apiKey: "your-api-key", // Or set MISTRAL_API_KEY env var
    model: "mistral-embed",
});
```

You must pass in a `model` argument, which selects the Mistral embedding model to use. You can see the supported embedding types and models in Mistral's docs here
