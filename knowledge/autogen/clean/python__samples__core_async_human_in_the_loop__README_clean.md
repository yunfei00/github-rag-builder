---
source: autogen
owner: microsoft
repo: autogen
path: python/samples/core_async_human_in_the_loop/README.md
url: https://github.com/microsoft/autogen/blob/main/python/samples/core_async_human_in_the_loop/README.md
---
# Async Human-in-the-Loop Example

An example showing human-in-the-loop which waits for human input before making the tool call.

## Prerequisites

First, you need a shell with AutoGen core and required dependencies installed.

```bash
pip install "autogen-ext[openai,azure]" "pyyaml"
```

## Model Configuration

The model configuration should defined in a `model_config.yml` file.
Use `model_config_template.yml` as a template.

## Running the example

```bash
python main.py
```
