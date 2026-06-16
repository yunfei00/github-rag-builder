---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-patentsview/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-patentsview/README.md
---
# Patentsview Loader

```bash
pip install llama-index-readers-patentsview
```

This loader loads patent abstract from `a list of patent numbers` with API provided by Patentsview.

> Note: The API now requires an API key which can be requested on this page.
> PatentsviewReader looks for its value in the environmental variable `PATENTSVIEW_API_KEY`

## Usage

Here'a an example usage of PatentsviewReader.

```python
from llama_index.readers.patentsview import PatentsviewReader

loader = PatentsviewReader(api_key=os.getenv("PATENTSVIEW_API_KEY"))
patents = ["8848839", "10452978"]
abstracts = loader.load_data(patents)
```

This loader is designed for loading data into LlamaIndex.
