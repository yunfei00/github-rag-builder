---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/callbacks/llama-index-callbacks-langfuse/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/callbacks/llama-index-callbacks-langfuse/README.md
---
# LlamaIndex Callbacks Integration: Langfuse

Langfuse is an open source LLM engineering platform to help teams collaboratively debug, analyze and iterate on their LLM Applications. With the Langfuse integration, you can seamlessly track and monitor performance, traces, and metrics of your LlamaIndex application. Detailed traces of the LlamaIndex context augmentation and the LLM querying processes are captured and can be inspected directly in the Langfuse UI.

#### Usage Pattern

```python
from llama_index.core import set_global_handler

# Make sure you've installed the 'llama-index-callbacks-langfuse' integration package.

# NOTE: Set your environment variables 'LANGFUSE_SECRET_KEY', 'LANGFUSE_PUBLIC_KEY' and 'LANGFUSE_HOST'
# as shown in your langfuse.com project settings.

set_global_handler("langfuse")
```
