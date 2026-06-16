---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/sheets/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-google/llama_index/readers/google/sheets/README.md
---
# Google Sheets Loader

`pip install llama-index-readers-google`

This loader reads your upcoming Google Sheets and parses the relevant info into `Documents`.

As a prerequisite, you will need to register with Google and generate a `credentials.json` file in the directory where you run this loader. See here for instructions.

## Usage

Here's an example usage of the GoogleSheetsReader.

```python
from llama_index.readers.google import GoogleSheetsReader

loader = GoogleSheetsReader()
documents = loader.load_data()
```

## Example

This loader is designed to be used as a way to load data into LlamaIndex.

### LlamaIndex

```python
from llama_index.readers.google import GoogleSheetsReader
from llama_index.core import VectorStoreIndex, download_loader

loader = GoogleSheetsReader()
documents = loader.load_data()

index = VectorStoreIndex.from_documents(documents)
index.query("When am I meeting Gordon?")
```
