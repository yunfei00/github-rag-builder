---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_deplot/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-file/llama_index/readers/file/image_deplot/README.md
---

# Image Tabular Chart Loader (Deplot)

```bash
pip install llama-index-readers-file
```

This loader captions an image file containing a tabular chart (bar chart, line charts) using deplot.

## Usage

To use this loader, you need to pass in a `Path` to a local file.

```python
from pathlib import Path
from llama_index.readers.file import ImageTabularChartReader

loader = ImageTabularChartReader()
documents = loader.load_data(file=Path("./image.png"))
```
