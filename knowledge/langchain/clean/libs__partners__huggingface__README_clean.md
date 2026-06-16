---
source: langchain
owner: langchain-ai
repo: langchain
path: libs/partners/huggingface/README.md
url: https://github.com/langchain-ai/langchain/blob/master/libs/partners/huggingface/README.md
---
# langchain-huggingface

Looking for the JS/TS version? Check out LangChain.js.

## Quick Install

```bash
uv add langchain-huggingface
```

> **Note:** The base install does not include `sentence-transformers` or `transformers`.
> If you plan to use `HuggingFaceEmbeddings` or `HuggingFacePipeline` for **local inference**,
> install the `[full]` extra which includes `sentence-transformers>=5.2.0` and `transformers>=5.0.0`:
>
> ```bash
> uv add "langchain-huggingface[full]"
> ```
>
> **Migrating from `langchain-community`?** Note that `langchain-community` accepted
> `sentence-transformers>=2.2.0`, but `langchain-huggingface[full]` requires `>=5.2.0`.
> If your project pins an older version, upgrade it:
>
> ```bash
> uv add "sentence-transformers>=5.2.0"
> ```

## 🤔 What is this?

This package contains the LangChain integrations for Hugging Face related classes.

## 📖 Documentation

For full documentation, see the API reference. For conceptual guides, tutorials, and examples on using these classes, see the LangChain Docs.

## 📕 Releases & Versioning

See our Releases and Versioning policies.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the Contributing Guide.

## Resources

- LangChain Academy — comprehensive, free courses on LangChain libraries and products, made by the LangChain team
- Code of Conduct — community guidelines and standards
