---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-tablestore/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-tablestore/README.md
---
# LlamaIndex Chat_Store Integration: Tablestore Chat Store

Using `TablestoreChatStore`, you can store your chat history remotely, without having to worry about manually persisting and loading the chat history.

## Installation

```bash
pip install llama-index-storage-chat-store-tablestore
```

## Usage

```python
from llama_index.storage.chat_store.tablestore import TablestoreChatStore
from llama_index.core.memory import ChatMemoryBuffer

# 1. create tablestore vector store
chat_store = TablestoreChatStore(
    endpoint="",
    instance_name="",
    access_key_id="",
    access_key_secret="",
)
# You need to create a table for the first use
chat_store.create_table_if_not_exist()

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```
