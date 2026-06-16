---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/embedding-models/cloudflare-workers-ai.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/embedding-models/cloudflare-workers-ai.mdx
---
---
title: Cloudflare Workers AI
---

Chroma provides a wrapper around Cloudflare Workers AI embedding models. This embedding function runs remotely against the Cloudflare Workers AI servers, and will require an API key and a Cloudflare account. You can find more information in the Cloudflare Workers AI Docs.

You can also optionally use the Cloudflare AI Gateway for a more customized solution by setting a `gateway_id` argument. See the Cloudflare AI Gateway Docs for more info.

```python Python
from chromadb.utils.embedding_functions import CloudflareWorkersAIEmbeddingFunction

os.environ["CHROMA_CLOUDFLARE_API_KEY"] = ""

ef = CloudflareWorkersAIEmbeddingFunction(
    account_id="",
    model_name="@cf/baai/bge-m3",
)
ef(input=["This is my first text to embed", "This is my second document"])
```

```typescript TypeScript
// npm install @chroma-core/cloudflare-worker-ai

import { CloudflareWorkersAIEmbeddingFunction } from '@chroma-core/cloudflare-worker-ai';

process.env.CLOUDFLARE_API_KEY = ""

const embedder = new CloudflareWorkersAIEmbeddingFunction({
    account_id="",
    model_name="@cf/baai/bge-m3",
});

// use directly
embedder.generate(['This is my first text to embed', 'This is my second document']);
```

You must pass in an `account_id` and `model_name` to the embedding function. It is recommended to set the `CHROMA_CLOUDFLARE_API_KEY` for the api key, but the embedding function also optionally takes in an `api_key` variable.
