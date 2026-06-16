---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-airbyte-zendesk-support/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-airbyte-zendesk-support/README.md
---
# Airbyte ZendeskSupport Loader

```bash
pip install llama-index-readers-airbyte-zendesk-support
```

The Airbyte ZendeskSupport Loader allows you to access different ZendeskSupport objects.

## Usage

Here's an example usage of the AirbyteZendeskSupportReader.

```python
from llama_index.readers.airbyte_zendesk_support import (
    AirbyteZendeskSupportReader,
)

zendesk_support_config = {
    # ...
}
reader = AirbyteZendeskSupportReader(config=zendesk_support_config)
documents = reader.load_data(stream_name="tickets")
```

## Configuration

Check out the Airbyte documentation page for details about how to configure the reader.
The JSON schema the config object should adhere to can be found on Github: https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zendesk-support/source_zendesk_support/spec.json.

The general shape looks like this:

```python
{
    "subdomain": "",
    "start_date": "",
    "credentials": {
        "credentials": "api_token",
        "email": "",
        "api_token": "",
    },
}
```

By default all fields are stored as metadata in the documents and the text is set to the JSON representation of all the fields. Construct the text of the document by passing a `record_handler` to the reader:

```python
def handle_record(record, id):
    return Document(
        doc_id=id, text=record.data["title"], extra_info=record.data
    )

reader = AirbyteZendeskSupportReader(
    config=zendesk_support_config, record_handler=handle_record
)
```

## Lazy loads

The `reader.load_data` endpoint will collect all documents and return them as a list. If there are a large number of documents, this can cause issues. By using `reader.lazy_load_data` instead, an iterator is returned which can be consumed document by document without the need to keep all documents in memory.

## Incremental loads

This loader supports loading data incrementally (only returning documents that weren't loaded last time or got updated in the meantime):

```python
reader = AirbyteZendeskSupportReader(config={...})
documents = reader.load_data(stream_name="tickets")
current_state = reader.last_state  # can be pickled away or stored otherwise

updated_documents = reader.load_data(
    stream_name="tickets", state=current_state
)  # only loads documents that were updated since last time
```

This loader is designed to be used as a way to load data into LlamaIndex.
