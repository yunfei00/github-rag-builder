---
source: llama_index
owner: run-llama
repo: llama_index
path: docs/src/content/docs/framework/understanding/rag/loading/llamacloud.md
url: https://github.com/run-llama/llama_index/blob/main/docs/src/content/docs/framework/understanding/rag/loading/llamacloud.md
---
---
title: Loading from LlamaCloud
---

Our enterprise service, LlamaCloud, allows you to store and query your data in a fully-managed, scalable, and secure environment. For a full explanation of how to use LlamaCloud, see the LlamaCloud documentation, in particular the framework integration guide.

## Using LlamaCloud from LlamaIndex

You can use LlamaCloud to connect to your data stores and automatically index them. Once an index is created, you can use it in just a few lines of code:

```python
import os
from llama_cloud_services import LlamaCloudIndex

os.environ["LLAMA_CLOUD_API_KEY"] = "llx-..."

index = LlamaCloudIndex("my_first_index", project_name="Default")
query_engine = index.as_query_engine()
answer = query_engine.query("Example query")
```

It's also possible to programmatically load documents into a LlamaCloud index; check the documentation for more details.
