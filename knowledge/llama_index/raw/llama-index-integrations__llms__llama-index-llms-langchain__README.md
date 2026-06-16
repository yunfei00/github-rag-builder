---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/llms/llama-index-llms-langchain/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-langchain/README.md
---

# LlamaIndex Llms Integration: Langchain

## Installation

1. Install the required Python packages:

   ```bash
   %pip install llama-index-llms-langchain
   ```

## Usage

### Import Required Libraries

```python
from langchain.llms import OpenAI
from llama_index.llms.langchain import LangChainLLM
```

### Initialize LangChain LLM

To create an instance of `LangChainLLM` with OpenAI:

```python
llm = LangChainLLM(llm=OpenAI())
```

### Generate Streaming Response

To generate a streaming response, use the following code:

```python
response_gen = llm.stream_complete("Hi this is")
for delta in response_gen:
    print(delta.delta, end="")
```

### LLM Implementation example

https://docs.llamaindex.ai/en/stable/examples/llm/langchain/
