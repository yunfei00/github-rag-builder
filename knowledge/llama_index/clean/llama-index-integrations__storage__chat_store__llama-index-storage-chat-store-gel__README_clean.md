---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-gel/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/storage/chat_store/llama-index-storage-chat-store-gel/README.md
---
# LlamaIndex Chat_Store Integration: Gel Chat Store

## Installation

`pip install llama-index-storage-chat-store-gel`

## Usage

Using `GelChatStore`, you can persist your chat history automatically and not have to worry about saving and loading it manually.

```python
from llama_index.storage.chat_store.gel import GelChatStore
from llama_index.core.memory import ChatMemoryBuffer

chat_store = GelChatStore()

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)
```
