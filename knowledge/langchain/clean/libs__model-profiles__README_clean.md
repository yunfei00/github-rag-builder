---
source: langchain
owner: langchain-ai
repo: langchain
path: libs/model-profiles/README.md
url: https://github.com/langchain-ai/langchain/blob/master/libs/model-profiles/README.md
---
# 🦜🪪 langchain-model-profiles

> [!WARNING]
> This package is currently in development and the API is subject to change.

CLI tool for updating model profile data in LangChain integration packages.

## Quick Install

```bash
uv add langchain-model-profiles
```

## 🤔 What is this?

`langchain-model-profiles` is a CLI tool for fetching and updating model capability data from models.dev for use in LangChain integration packages.

LangChain chat models expose a `.profile` field that provides programmatic access to model capabilities such as context window sizes, supported modalities, tool calling, structured output, and more. This CLI tool helps maintainers keep that data up-to-date.

## Data sources

This package is built on top of the excellent work by the models.dev project, an open source initiative that provides model capability data.

LangChain model profiles augment the data from models.dev with some additional fields. We intend to keep this aligned with the upstream project as it evolves.

## 📖 Documentation

For full documentation, see the API reference. For conceptual guides, tutorials, and examples on using LangChain, see the LangChain Docs. You can also chat with the docs using Chat LangChain.

## Usage

Update model profile data for a specific provider:

```bash
langchain-profiles refresh --provider anthropic --data-dir ./langchain_anthropic/data
```

This downloads the latest model data from models.dev, merges it with any augmentations defined in `profile_augmentations.toml`, and generates a `profiles.py` file.

## Resources

- LangChain Academy — comprehensive, free courses on LangChain libraries and products, made by the LangChain team
- Code of Conduct — community guidelines and standards
