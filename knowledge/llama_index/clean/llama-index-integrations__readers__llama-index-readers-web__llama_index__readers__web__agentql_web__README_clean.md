---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-web/llama_index/readers/web/agentql_web/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-web/llama_index/readers/web/agentql_web/README.md
---
# AgentQL Web Loader

## Instructions for AgentQL Web Loader

### Setup and Installation

1. **API Key**: Secure an API key from AgentQL to access the AgentQL services.

And you are good to go!

### Using AgentQL Web Loader

- **Initialization**: Initialize the AgentQLWebReader by providing the API key, along with any optional parameters you wish to set for the AgentQL API. You can view all the settable parameters here.

  ```python
  from llama_index.readers.web import AgentQLWebReader

  agentql_reader = AgentQLWebReader(
      api_key="Your AgentQL API key Here",  # Replace with your actual API key from https://dev.agentql.com
      # Optional additional parameters
      params={
          "is_scroll_to_bottom_enabled": True
      },  # for example, here we enable scroll to bottom
  )
  ```

- **Loading Data**: To load data, use the `load_data` method with the URL you wish to scrape and the Agentql Query you wish to run. To learn more about the Agentql Query, please refer to the AgentQL query language documentation.

```python
document = agentql_reader.load_data(
    url="https://example.com", query="{ products[] { name price } }"
)
```

### Example Usage

Here is an example demonstrating how to initialize the AgentQLWebReader, load document from a URL and an AgentQL Query, and then create a summary index from those documents for querying.

```python
# Initialize the AgentQLWebReader with your API key and parameters
agentql_reader = AgentQLWebReader(
    api_key="Your AgentQL API key Here",  # Replace with your actual API key from https://dev.agentql.com
    params={
        "is_scroll_to_bottom_enabled": True
    },  # Optional additional parameters
)

# Load documents from scrapeme.live/shop/ which contains a list of pokemons and their prices
document = agentql_reader.load_data(
    url="https://scrapeme.live/shop/", query="{ pokemons[] { name price } }"
)

# Create a summary index from the loaded documents for querying
index = SummaryIndex.from_documents(document)

# Convert the summary index into a query engine
query_engine = index.as_query_engine()

# Perform a query on the index to find insights from Paul Graham's essays
response = query_engine.query("What is the average price of the pokemons?")

# Display the query response
print(response)
```
