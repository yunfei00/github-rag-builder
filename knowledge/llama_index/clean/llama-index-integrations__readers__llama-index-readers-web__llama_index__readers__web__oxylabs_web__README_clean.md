---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-web/llama_index/readers/web/oxylabs_web/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-web/llama_index/readers/web/oxylabs_web/README.md
---
# Oxylabs Webpage Loader

Use Oxylabs Webpage Loader to load a webpage from any URL.

For more information checkout out the Oxylabs documentation.

## Instructions for OxylabsReader

### Setup and Installation

Installation with `pip`

```shell
pip install llama-index-readers-web
```

Installation with `poetry`

```shell
poetry add llama-index-readers-web
```

Installation with `uv`

```shell
uv add llama-index-readers-web
```

### Get Oxylabs credentials

Set up your Oxylabs account and get the username and password.

### Using OxylabsReader

```python
from llama_index.readers.web import OxylabsWebReader

reader = OxylabsWebReader(
    username="OXYLABS_USERNAME",
    password="OXYLABS_PASSWORD",
)

docs = reader.load_data(["https://ip.oxylabs.io"])

print(docs)
```
