# github-rag-builder

一个实用的 RAG Demo：采集公开 GitHub 项目文档，清洗成标准 Markdown，按 Header Chunk 切分，构建 Chroma 向量数据库，并支持语义检索与 RAG 问答。

## 使用方式

安装依赖：

```bash
pip install -r requirements.txt
```

构建知识库与向量库后，可以运行语义检索：

```bash
python scripts/search_vector.py "你的问题"
```

运行 RAG Chat：

```bash
python scripts/rag_chat.py
```

RAG Chat 需要配置 OpenAI Compatible API 环境变量：

```bash
export LLM_BASE_URL="https://your-api-base-url/v1"
export LLM_API_KEY="your-api-key"
export LLM_MODEL="your-model"
```

Windows PowerShell 示例：

```powershell
$env:LLM_BASE_URL="https://your-api-base-url/v1"
$env:LLM_API_KEY="your-api-key"
$env:LLM_MODEL="your-model"
python scripts/rag_chat.py
```
