---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/node_parser/llama-index-node-parser-alibabacloud-aisearch/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/node_parser/llama-index-node-parser-alibabacloud-aisearch/README.md
---
# LlamaIndex Node_Parser Integration: Alibabacloud_Aisearch

## Installation

```
pip install llama-index-node-parser-alibabacloud-aisearch
```

## Optional Installation

For automatic parsing of image slices, you can optionally install `llama-index-readers-alibabacloud-aisearch`.

```
pip install llama-index-readers-alibabacloud-aisearch
```

## Usage

For further details, please visit document-split-api-details.

You can specify the `endpoint` and `aisearch_api_key` in the constructor, or set the environment variables `AISEARCH_ENDPOINT` and `AISEARCH_API_KEY`.

```python
from llama_index.node_parser.alibabacloud_aisearch import (
    AlibabaCloudAISearchNodeParser,
)
from llama_index.core import Document

try:
    from llama_index.readers.alibabacloud_aisearch import (
        AlibabaCloudAISearchImageReader,
    )

    image_reader = AlibabaCloudAISearchImageReader(
        service_id="ops-image-analyze-vlm-001"
    )
except ImportError:
    image_reader = None
node_parser = AlibabaCloudAISearchNodeParser(
    chunk_size=1024, image_reader=image_reader
)
nodes = node_parser(
    [
        Document(text="content1", mimetype="text/markdown"),
        Document(
            text="content2 ",
            mimetype="text/markdown",
        ),
    ],
    show_progress=True,
)
for i, node in enumerate(nodes):
    print(f"[SPLIT#{i}]:\n{node.get_content()}")
    print("-" * 80)
```
