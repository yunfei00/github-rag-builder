---
source: llama_index
owner: run-llama
repo: llama_index
path: llama-index-integrations/readers/llama-index-readers-twitter/README.md
url: https://github.com/run-llama/llama_index/blob/main/llama-index-integrations/readers/llama-index-readers-twitter/README.md
---
# LlamaIndex Readers Integration: TwitterTweet

## Overview

The TwitterTweet Reader allows you to read tweets of a specified Twitter handle. It retrieves tweets from Twitter using the Twitter API.

### Installation

You can install the TwitterTweet Reader via pip:

```bash
pip install llama-index-readers-twitter
```

Check Twitter API on how to get access to twitter API.

### Usage

```python
from llama_index.readers.twitter import TwitterTweetReader

# Initialize TwitterTweetReader
reader = TwitterTweetReader(
    bearer_token="", num_tweets=100
)

# Load tweets of user twitter handles
documents = reader.load_data(twitterhandles=["user1", "user2"])
```

This loader is designed to be used as a way to load data into
LlamaIndex and/or subsequently
used as a Tool in a LangChain Agent.
