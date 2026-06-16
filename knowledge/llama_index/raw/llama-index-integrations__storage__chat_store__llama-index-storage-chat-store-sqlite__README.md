---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-sqlite/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-sqlite/README.md
---

# LlamaIndex Chat_Store Integration: SQLite Chat Store

## Installation

`pip install llama-index-storage-chat-store-sqlite`

## Usage

Using `SQLiteChatStore`, you can store your chat history remotely, without having to worry about manually persisting and loading the chat history.

```python
from llama_index.storage.chat_store.sqlite import SQLiteChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = SQLiteChatStore.from_uri(
    uri="sqlite+aiosqlite:///chat_store.db",
)

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```
