import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

KNOWLEDGE_FILE = Path("knowledge/langchain/knowledge.json")
DB_DIR = "db/chroma"

items = json.loads(KNOWLEDGE_FILE.read_text(encoding="utf-8"))

model = SentenceTransformer("BAAI/bge-small-zh-v1.5")

client = chromadb.PersistentClient(path=DB_DIR)

collection = client.get_or_create_collection(
    name="github_rag_knowledge"
)

ids = []
documents = []
metadatas = []

for item in items:
    text = f"{item['title']}\n\n{item['content']}"

    ids.append(item["chunk_id"])
    documents.append(text)
    metadatas.append({
        "source": item["source"],
        "file": item["file"],
        "title": item["title"],
        "chunk_id": item["chunk_id"]
    })

embeddings = model.encode(
    documents,
    normalize_embeddings=True
).tolist()

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

print(f"Vector DB built successfully: {len(ids)} chunks")
