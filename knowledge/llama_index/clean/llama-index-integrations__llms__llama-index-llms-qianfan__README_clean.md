---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/llms/llama-index-llms-qianfan/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-qianfan/README.md
---
# LlamaIndex Llms Integration: Baidu Qianfan

Baidu Intelligent Cloud's Qianfan LLM Platform offers API services for all Baidu LLMs, such as ERNIE-3.5-8K and ERNIE-4.0-8K. It also provides a small number of open-source LLMs like Llama-2-70b-chat.

Before using the chat client, you need to activate the LLM service on the Qianfan LLM Platform console's online service page. Then, Generate an Access Key and a Secret Key in the Security Authentication page of the console.

## Installation

Install the necessary package:

```
pip install llama-index-llms-qianfan
```

## Initialization

```python
from llama_index.llms.qianfan import Qianfan

access_key = "XXX"
secret_key = "XXX"
model_name = "ERNIE-Speed-8K"
endpoint_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed"
context_window = 8192
llm = Qianfan(access_key, secret_key, model_name, endpoint_url, context_window)
```
