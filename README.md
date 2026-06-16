# github-rag-builder

一个实用的 RAG Demo：采集公开 GitHub 项目文档，清洗成标准 Markdown，按标题切分，构建 Chroma 向量数据库，并支持 DashScope 百炼 OpenAI Compatible API 的 RAG 问答。

## Configuration

复制配置文件：

```bash
cp config/config.example.yaml config/config.yaml
```

然后编辑：

```bash
config/config.yaml
```

填写：

```yaml
llm.api_key
```

## Collect GitHub Docs

```bash
python scripts/collect_github_docs.py
```

## Clean Markdown

```bash
python scripts/clean_all_markdown.py
```

## Build Knowledge JSON

```bash
python scripts/build_all_knowledge.py
```

## Stats

```bash
python scripts/stats.py
```

## Build Vector DB

```bash
python scripts/build_vector_db.py
```

## Semantic Search

```bash
python scripts/search_vector.py "为什么要使用 LangChain"
```

## Debug Search

```bash
python scripts/debug_search.py "RAG 是什么"
```

## RAG Chat

```bash
python scripts/rag_chat.py
```
