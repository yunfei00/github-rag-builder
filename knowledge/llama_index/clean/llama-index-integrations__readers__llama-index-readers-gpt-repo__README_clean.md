---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-gpt-repo/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-gpt-repo/README.md
---
# GPT Repository Loader

```bash
pip install llama-index-readers-gpt-repo
```

This loader is an adaptation of https://github.com/mpoon/gpt-repository-loader
to LlamaIndex. Full credit goes to mpoon for coming up with this!

## Usage

To use this loader, you need to pass in a path to a local Git repository

```python
from llama_index.readers.gpt_repo import GPTRepoReader

loader = GPTRepoReader()
documents = loader.load_data(
    repo_path="/path/to/git/repo",
    preamble_str="",
)
```

This loader is designed to be used as a way to load data into LlamaIndex.
