---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-linear/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-linear/README.md
---

# Linear Reader

```bash
pip install llama-index-readers-linear
```

The Linear loader returns issue based on the query.

## Usage

Here's an example of how to use it

```python
from llama_index.readers.linear import LinearReader

reader = LinearReader(api_key=api_key)
query = """
    query Team {
        team(id: "9cfb482a-81e3-4154-b5b9-2c805e70a02d") {
            id
            name
            issues {
                nodes {
                    id
                    title
                    description
                    assignee {
                        id
                        name
                    }
                    createdAt
                    archivedAt
                }
            }
        }
    }
"""

documents = reader.load_data(query=query)
```

Alternately, you can also use download_loader from llama_index

```python
from llama_index.readers.linear import LinearReader

reader = LinearReader(api_key=api_key)
query = """
    query Team {
        team(id: "9cfb482a-81e3-4154-b5b9-2c805e70a02d") {
            id
            name
            issues {
                nodes {
                    id
                    title
                    description
                    assignee {
                        id
                        name
                    }
                    createdAt
                    archivedAt
                }
            }
        }
    }
"""
documents = reader.load_data(query=query)
```
