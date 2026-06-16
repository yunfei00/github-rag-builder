---
source: llama_index
owner: run-llama
repo: llama_index
path: docs/src/content/docs/framework/module_guides/supporting_modules/supporting_modules.md
url: https://github.com/run-llama/llama_index/blob/main/docs/src/content/docs/framework/module_guides/supporting_modules/supporting_modules.md
---

---
title: Supporting Modules
---

We have two configuration modules that can be configured separately and passed to individual indexes, or set globally.

- The [Settings](/python/framework/module_guides/supporting_modules/settings) includes the LLM you're using, the embedding model, your node parser, your callback manager and more.
- The `StorageContext` lets you specify where and how to store your documents, your vector embeddings, and your indexes. To learn more, read about [customizing storage](/python/framework/module_guides/storing/customization)
