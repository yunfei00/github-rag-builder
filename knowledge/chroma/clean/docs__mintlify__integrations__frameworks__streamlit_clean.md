---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/integrations/frameworks/streamlit.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/integrations/frameworks/streamlit.mdx
---
---
title: Streamlit
---

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

Apache 2.0 License | Site

| Languages | Docs | Github |
|--|--|--|
| Python | Docs | Code

### Install

Install Streamlit:
`pip install streamlit`

Install `streamlit-chromadb-connection`, which connects your Streamlit app to Chroma through `st.connection`:
`pip install streamlit-chromadb-connection`

### Main Benefits

- Easy to get started with Streamlit's straightforward syntax
- Built-in chatbot functionality
- Pre-built integration with Chroma via `streamlit-chromadb-connection`
- Deploy apps for free on Streamlit Community Cloud

### Simple Example

#### Python

```python
import streamlit as st
from streamlit_chromadb_connection.chromadb_connection import ChromadbConnection

configuration = {
    "client": "PersistentClient",
    "path": "/tmp/.chroma"
}

collection_name = "documents_collection"

conn = st.connection("chromadb",
                     type=ChromaDBConnection,
                     **configuration)
documents_collection_df = conn.get_collection_data(collection_name)
st.dataframe(documents_collection_df)
```

### Resources

- Instructions for using `streamlit-chromadb-connection` to connect your Streamlit app to Chroma
- Demo app for `streamlit-chromadb-connection`
- Streamlit's `st.connection` documentation
- Guide to using vector databases with Streamlit

#### Tutorials

- Build an "Ask the Doc" app using Chroma, Streamlit, and LangChain
- Summarize documents with Chroma, Streamlit, and LangChain
- Build a custom chatbot with Chroma, Streamlit, and LangChain
- Build a RAG bot using Chroma, Streamlit, and LangChain
- Build a PDF QA chatbot with Chroma, Streamlit, and OpenAI
