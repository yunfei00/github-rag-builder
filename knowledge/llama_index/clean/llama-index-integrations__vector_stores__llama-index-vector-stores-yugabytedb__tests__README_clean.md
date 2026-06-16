---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/vector_stores/llama-index-vector-stores-yugabytedb/tests/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/vector_stores/llama-index-vector-stores-yugabytedb/tests/README.md
---
# Testing Setup

You will need to start a Yugabytedb instance locally to run the tests for this integration. You can do this easily via docker cli:

```
./bin/yugabyted start
```

For more information about starting a Yugabytedb cluster, see here.

Run the tests:

```
 uv run -- pytest
```
