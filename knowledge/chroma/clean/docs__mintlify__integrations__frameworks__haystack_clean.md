---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/frameworks/haystack.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/frameworks/haystack.mdx
---
---
title: Haystack
---

Haystack is an open-source LLM framework in Python. It provides embedders, generators and rankers via a number of LLM providers, tooling for preprocessing and data preparation, connectors to a number of vector databases including Chroma and more. Haystack allows you to build custom LLM applications using both components readily available in Haystack and custom components. Some of the most common applications you can build with Haystack are retrieval-augmented generation pipelines (RAG), question-answering and semantic search.

|Docs | Github | Haystack Integrations | Tutorials |

You can use Chroma together with Haystack by installing the integration and using the `ChromaDocumentStore`

### Installation

```terminal
pip install chroma-haystack
```

### Usage

- The Chroma Integration page
- Chroma + Haystack Example

#### Write documents into a ChromaDocumentStore

```python
import os
from pathlib import Path

from haystack import Pipeline
from haystack.components.converters import TextFileToDocument
from haystack.components.writers import DocumentWriter
from chroma_haystack import ChromaDocumentStore

file_paths = ["data" / Path(name) for name in os.listdir("data")]

document_store = ChromaDocumentStore()

indexing = Pipeline()
indexing.add_component("converter", TextFileToDocument())
indexing.add_component("writer", DocumentWriter(document_store))

indexing.connect("converter", "writer")
indexing.run({"converter": {"sources": file_paths}})
```

#### Build RAG on top of Chroma

```python
from chroma_haystack.retriever import ChromaQueryRetriever
from haystack.components.generators import HuggingFaceTGIGenerator
from haystack.components.builders import PromptBuilder

prompt = """
Answer the query based on the provided context.
If the context does not contain the answer, say 'Answer not found'.
Context:
{% for doc in documents %}
  {{ doc.content }}
{% endfor %}
query: {{query}}
Answer:
"""
prompt_builder = PromptBuilder(template=prompt)

llm = HuggingFaceTGIGenerator(model="mistralai/Mixtral-8x7B-Instruct-v0.1", token='YOUR_HF_TOKEN')
llm.warm_up()
retriever = ChromaQueryRetriever(document_store)

querying = Pipeline()
querying.add_component("retriever", retriever)
querying.add_component("prompt_builder", prompt_builder)
querying.add_component("llm", llm)

querying.connect("retriever.documents", "prompt_builder.documents")
querying.connect("prompt_builder", "llm")

results = querying.run({"retriever": {"queries": [query], "top_k": 3},
                        "prompt_builder": {"query": query}})
```
