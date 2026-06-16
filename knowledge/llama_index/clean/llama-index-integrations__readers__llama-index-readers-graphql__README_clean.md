---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-graphql/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-graphql/README.md
---
# GraphQL Loader

```bash
pip install llama-index-readers-graphql
```

This loader loads documents via GraphQL queries from a GraphQL endpoint.
The user specifies a GraphQL endpoint URL with optional credentials to initialize the reader.
By declaring the GraphQL query and optional variables (parameters) the loader can fetch the nested result docs.

## Usage

Here's an example usage of the GraphQLReader.
You can test out queries directly on the site

```python
import os

from llama_index.readers.graphql import GraphQLReader

uri = "https://countries.trevorblades.com/"
headers = {}
query = """
    query getContinents {
        continents {
            code
            name
        }
    }
"""
reader = GraphQLReader(uri, headers)
documents = reader.query(query, variables={})
```

This loader is designed to be used as a way to load data into LlamaIndex
and/or subsequently used as a Tool in a LangChain Agent.

It uses the gql GraphQL library for the GraphQL queries.
