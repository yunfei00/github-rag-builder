---
source: firecrawl
owner: firecrawl
repo: firecrawl
path: apps/api/sharedLibs/go-html-to-md/README.md
url: https://github.com/firecrawl/firecrawl/blob/main/apps/api/sharedLibs/go-html-to-md/README.md
---
To build the `go-html-to-md` library, run the following command:

```bash
cd apps/api/sharedLibs/go-html-to-md
go build -o  -buildmode=c-shared html-to-markdown.go
```

Replace `` with the correct filename for your OS:

- Windows → `html-to-markdown.dll`
- Linux → `libhtml-to-markdown.so`
- macOS → `libhtml-to-markdown.dylib`
