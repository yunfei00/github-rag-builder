---
source: llama_index
owner: run-llama
repo: llama_index
path: docs/src/content/docs/framework/understanding/rag/loading/llamahub.md
url: https://github.com/run-llama/llama_index/blob/main/docs/src/content/docs/framework/understanding/rag/loading/llamahub.md
---
---
title: LlamaHub
---

Our data connectors are offered through LlamaHub 🦙.
LlamaHub contains a registry of open-source data connectors that you can easily plug into any LlamaIndex application (+ Agent Tools, and Llama Packs).

## Usage Pattern

Get started with:

```python
from llama_index.core import download_loader

from llama_index.readers.google import GoogleDocsReader

loader = GoogleDocsReader()
documents = loader.load_data(document_ids=[...])
```

## Built-in connector: SimpleDirectoryReader

`SimpleDirectoryReader`. Can support parsing a wide range of file types including `.md`, `.pdf`, `.jpg`, `.png`, `.docx`, as well as audio and video types. It is available directly as part of LlamaIndex:

```python
from llama_index.core import SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
```

## Available connectors

Browse LlamaHub directly to see the hundreds of connectors available, including:

- Notion (`NotionPageReader`)
- Google Docs (`GoogleDocsReader`)
- Slack (`SlackReader`)
- Discord (`DiscordReader`)
- Apify Actors (`ApifyActor`). Can crawl the web, scrape webpages, extract text content, download files including `.pdf`, `.jpg`, `.png`, `.docx`, etc.
