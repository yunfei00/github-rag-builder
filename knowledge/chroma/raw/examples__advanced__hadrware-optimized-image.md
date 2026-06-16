---
source: chroma
owner: chroma-core
repo: chroma
path: examples/advanced/hadrware-optimized-image.md
url: https://github.com/chroma-core/chroma/blob/main/examples/advanced/hadrware-optimized-image.md
---

# Building Hardware Optimized ChromaDB Image

The default Chroma DB image comes with binary distribution of hnsw lib which is not optimized to take advantage of
certain CPU architectures (Intel-based) with AVX support. This can be improved by building an image with hnsw rebuilt
from source. To do that run:

```bash
docker build -t chroma-test1 --build-arg REBUILD_HNSWLIB=true --no-cache .
```
