---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-airbyte-hubspot/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-airbyte-hubspot/README.md
---
# Airbyte Hubspot Loader

```bash
pip install llama-index-readers-airbyte-hubspot
```

The Airbyte Hubspot Loader allows you to access different Hubspot objects.

## Usage

Here's an example usage of the AirbyteHubspotReader.

```python
from llama_index.readers.airbyte_hubspot import AirbyteHubspotReader

hubspot_config = {
    # ...
}
reader = AirbyteHubspotReader(config=hubspot_config)
documents = reader.load_data(stream_name="products")
```

## Configuration

Check out the Airbyte documentation page for details about how to configure the reader.
The JSON schema the config object should adhere to can be found on Github: https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-hubspot/source_hubspot/spec.yaml.

The general shape looks like this:

```python
{
    "start_date": "",
    "credentials": {
        "credentials_title": "Private App Credentials",
        "access_token": "",
    },
}
```

By default all fields are stored as metadata in the documents and the text is set to the JSON representation of all the fields. Construct the text of the document by passing a `record_handler` to the reader:

```python
def handle_record(record, id):
    return Document(
        doc_id=id, text=record.data["title"], extra_info=record.data
    )

reader = AirbyteHubspotReader(
    config=hubspot_config, record_handler=handle_record
)
```

## Lazy loads

The `reader.load_data` endpoint will collect all documents and return them as a list. If there are a large number of documents, this can cause issues. By using `reader.lazy_load_data` instead, an iterator is returned which can be consumed document by document without the need to keep all documents in memory.

## Incremental loads

This loader supports loading data incrementally (only returning documents that weren't loaded last time or got updated in the meantime):

```python
reader = AirbyteHubspotReader(config={...})
documents = reader.load_data(stream_name="products")
current_state = reader.last_state  # can be pickled away or stored otherwise

updated_documents = reader.load_data(
    stream_name="products", state=current_state
)  # only loads documents that were updated since last time
```

This loader is designed to be used as a way to load data into LlamaIndex.
