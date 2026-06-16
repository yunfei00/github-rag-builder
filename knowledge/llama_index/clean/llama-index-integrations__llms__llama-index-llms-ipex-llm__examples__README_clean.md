---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/llms/llama-index-llms-ipex-llm/examples/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/llms/llama-index-llms-ipex-llm/examples/README.md
---
# IpexLLM Examples

This folder contains examples showcasing how to use LlamaIndex with `ipex-llm` LLM integration `llama_index.llms.ipex_llm.IpexLLM`.

## Installation

### On CPU

Install `llama-index-llms-ipex-llm`. This will also install `ipex-llm` and its dependencies.

```bash
pip install llama-index-llms-ipex-llm
```

### On GPU

Install `llama-index-llms-ipex-llm`. This will also install `ipex-llm` and its dependencies.

```bash
pip install llama-index-llms-ipex-llm[xpu] --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/
```

## List of Examples

### Basic Example

The example basic.py shows how to run `IpexLLM` on Intel CPU or GPU and conduct tasks such as text completion. Run the example as following:

```bash
python basic.py -m  -d  -q 
```

> Please note that in this example we'll use HuggingFaceH4/zephyr-7b-alpha model for demonstration. It requires updating `transformers` and `tokenizers` packages.
>
> ```bash
> pip install -U transformers==4.37.0 tokenizers==0.15.2
> ```

### Low Bit Example

The example low_bit.py shows how to save and load low_bit model by `IpexLLM` on Intel CPU or GPU and conduct tasks such as text completion. Run the example as following:

```bash
python low_bit.py -m  -d  -q  -s 
```

> Please note that in this example we'll use HuggingFaceH4/zephyr-7b-alpha model for demonstration. It requires updating `transformers` and `tokenizers` packages.
>
> ```bash
> pip install -U transformers==4.37.0 tokenizers==0.15.2
> ```

### More Data Types Example

By default, `IpexLLM` loads the model in int4 format. To load a model in different data formats like `sym_int5`, `sym_int8`, etc., you can use the `load_in_low_bit` option in `IpexLLM`.

```bash
python more_data_type.py -m  -t  -l  -d  -q 
```

> Note: If you're using meta-llama/Llama-2-7b-hf model in this example, it is recommended to use transformers version
> <=4.34.
