---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-intercom/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-intercom/README.md
---

# Intercom Loader

```bash
pip install llama-index-readers-intercom
```

This loader fetches the text from Intercom help articles using the Intercom API. It also uses the BeautifulSoup library to parse the HTML and extract the text from the articles.

## Usage

To use this loader, you need to pass in an Intercom account access token.

```python
from llama_index.readers.intercom import IntercomReader

loader = IntercomReader(intercom_access_token="my_access_token")
documents = loader.load_data()
```

This loader is designed to be used as a way to load data into [LlamaIndex](https://github.com/run-llama/llama_index/).
