---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-whisper/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-whisper/README.md
---

# OpenAI Whisper Reader

## Overview

Whisper Reader reads audio files and transcribes them to text using the OpenAI Whisper API.

### Installation

You can install Whisper Reader via pip:

```bash
pip install llama-index-readers-whisper
```

## Usage

```python
from llama_index.readers.whisper import WhisperReader

# Initialize WhisperReader
reader = WhisperReader(
    model="whisper-1",
    api_key="your-api-key",
)

# Load data from audio file
documents = reader.load_data("path/to/your/audio/file.mp3")

# load data async
documents = await reader.aload_data("path/to/your/audio/file.mp3")
```
