---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/docs/run-chroma/client-server.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/docs/run-chroma/client-server.mdx
---
---
title: "Client-Server Mode"
description: "Learn how to run Chroma in client-server mode."
---

Chroma can also be configured to run in client/server mode. In this mode, the Chroma client connects to a Chroma server running in a separate process.

To start the Chroma server, run the following command:

```bash
chroma run --path /db_path
```

Then use the Chroma `HttpClient` to connect to the server:

```python
import chromadb

chroma_client = chromadb.HttpClient(host='localhost', port=8000)
```

That's it! Chroma's API will run in `client-server` mode with just this change.

Chroma also provides the async HTTP client. The behaviors and method signatures are identical to the synchronous client, but all methods that would block are now async. To use it, call `AsyncHttpClient` instead:

```python
import asyncio
import chromadb

async def main():
    client = await chromadb.AsyncHttpClient()

    collection = await client.create_collection(name="my_collection")
    await collection.add(
        documents=["hello world"],
        ids=["id1"]
    )

asyncio.run(main())
```

If you deploy your Chroma server, you can also use our http-only package.

Then you can connect to it by instantiating a new `ChromaClient`:

```typescript
import { ChromaClient } from "chromadb";

const client = new ChromaClient();
```

If you run your Chroma server using a different configuration, or deploy your Chroma server, you can specify the `host`, `port`, and whether the client should connect over `ssl`:

```typescript
import { ChromaClient } from "chromadb";

const client = new ChromaClient({
  host: "YOUR-HOST",
  port: "YOUR-PORT",
  ssl: true,
});
```

You can connect to it by instantiating a new `ChromaHttpClient`:

```rust
let options = ChromaHttpClientOptions {
    endpoint: "http://localhost:8000".parse()?,
    ..Default::default()
};
let client = ChromaHttpClient::new(options);
```
