---
source: llama_index
owner: run-llama
repo: llama_index
path: docs/src/content/docs/framework/community/integrations/trulens.md
url: https://github.com/run-llama/llama_index/blob/main/docs/src/content/docs/framework/community/integrations/trulens.md
---
---
title: Evaluating and Tracking with TruLens
---

This page covers how to use TruLens to evaluate and track LLM apps built on Llama-Index.

## What is TruLens?

TruLens is an opensource package that provides instrumentation and evaluation tools for large language model (LLM) based applications. This includes feedback function evaluations of relevance, sentiment and more, plus in-depth tracing including cost and latency.

As you iterate on new versions of your LLM application, you can compare their performance across all of the different quality metrics you've set up. You'll also be able to view evaluations at a record level, and explore the app metadata for each record.

### Installation and Setup

Adding TruLens is simple, just install it from pypi!

```sh
pip install trulens-eval
```

```python
from trulens_eval import TruLlama
```

## Try it out!

llama_index_quickstart.ipynb

## Read more

- Build and Evaluate LLM Apps with LlamaIndex and TruLens
- More examples
- trulens.org
