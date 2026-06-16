---
source: llama_index
owner: run-llama
repo: llama_index
path: docs/src/content/docs/framework/community/integrations/graphsignal.md
url: https://github.com/run-llama/llama_index/blob/main/docs/src/content/docs/framework/community/integrations/graphsignal.md
---
---
title: Tracing with Graphsignal
---

Graphsignal provides observability for AI agents and LLM-powered applications. It helps developers ensure AI applications run as expected and users have the best experience.

Graphsignal **automatically** traces and monitors LlamaIndex. Traces and metrics provide execution details for query, retrieval, and index operations. These insights include **prompts**, **completions**, **embedding statistics**, **retrieved nodes**, **parameters**, **latency**, and **exceptions**.

When OpenAI APIs are used, Graphsignal provides additional insights such as **token counts** and **costs** per deployment, model or any context.

### Installation and Setup

Adding Graphsignal tracer is simple, just install and configure it:

```sh
pip install graphsignal
```

```python
import graphsignal

# Provide an API key directly or via GRAPHSIGNAL_API_KEY environment variable
graphsignal.configure(
    api_key="my-api-key", deployment="my-llama-index-app-prod"
)
```

You can get an API key here.

See the Quick Start guide, Integration guide, and an example app for more information.

### Tracing Other Functions

To additionally trace any function or code, you can use a decorator or a context manager:

```python
with graphsignal.start_trace("load-external-data"):
    reader.load_data()
```

See Python API Reference for complete instructions.

### Useful Links

- Tracing and Monitoring LlamaIndex Applications
- Monitor OpenAI API Latency, Tokens, Rate Limits, and More
- OpenAI API Cost Tracking: Analyzing Expenses by Model, Deployment, and Context
