---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-web/llama_index/readers/web/browserbase_web/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-web/llama_index/readers/web/browserbase_web/README.md
---
# Browserbase Web Reader

Browserbase is a developer platform to reliably run, manage, and monitor headless browsers.

Power your AI data retrievals with:

- Serverless Infrastructure providing reliable browsers to extract data from complex UIs
- Stealth Mode with included fingerprinting tactics and automatic captcha solving
- Session Debugger to inspect your Browser Session with networks timeline and logs
- Live Debug to quickly debug your automation

## Installation and setup

- Get an API key and Project ID from browserbase.com and set it in environment variables (`BROWSERBASE_API_KEY`, `BROWSERBASE_PROJECT_ID`).
- Install the Browserbase SDK:

```bash
pip install browserbase
```

## Loading documents

You can load webpages into LlamaIndex using `BrowserbaseWebReader`. Optionally, you can set `text_content` parameter to convert the pages to text-only representation.

```python
from llama_index.readers.web import BrowserbaseWebReader

reader = BrowserbaseWebReader()
docs = reader.load_data(
    urls=[
        "https://example.com",
    ],
    # Text mode
    text_content=False,
)
```

### Parameters

- `urls` Required. A list of URLs to fetch.
- `text_content` Retrieve only text content. Default is `False`.
- `session_id` Optional. Provide an existing Session ID.
- `proxy` Optional. Enable/Disable Proxies.## Loading images

You can also load screenshots of webpages (as bytes) for multi-modal models.

```python
from browserbase import Browserbase
from base64 import b64encode

browser = Browserbase()
screenshot = browser.screenshot("https://browserbase.com")

# Optional. Convert to base64
img_encoded = b64encode(screenshot).decode()
```
