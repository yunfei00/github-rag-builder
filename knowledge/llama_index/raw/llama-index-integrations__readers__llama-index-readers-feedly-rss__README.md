---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-feedly-rss/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-feedly-rss/README.md
---

# Feedly Loader

```bash
pip install llama-index-readers-feedly-rss
```

This loader fetches the entries from a list of RSS feeds subscribed in [Feedly](https://feedly.com). You must initialize the loader with your [Feedly API token](https://developer.feedly.com), and then pass the category name which you want to extract.

## Usage

```python
from llama_index.readers.feedly_rss import FeedlyRssReader

loader = feedlyRssReader(bearer_token="[YOUR_TOKEN]")
documents = loader.load_data(category_name="news", max_count=100)
```

## Dependencies

[feedly-client](https://pypi.org/project/feedly-client/)
