---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-firebase-realtimedb/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-firebase-realtimedb/README.md
---
# Firebase Realtime Database Loader

```bash
pip install llama-index-readers-firebase-realtimedb
```

This loader retrieves documents from Firebase Realtime Database. The user specifies the Firebase Realtime Database URL and, optionally, the path to a service account key file for authentication.

## Usage

Here's an example usage of the FirebaseRealtimeDatabaseReader.

```python
from llama_index.readers.firebase_realtimedb import (
    FirebaseRealtimeDatabaseReader,
)

database_url = ""
service_account_key_path = ""
path = ""
reader = FirebaseRealtimeDatabaseReader(database_url, service_account_key_path)
documents = reader.load_data(path)
```

This loader is designed to be used as a way to load data into LlamaIndex.
