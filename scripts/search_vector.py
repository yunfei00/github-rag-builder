import sys

import chromadb
from sentence_transformers import SentenceTransformer

query = " ".join(sys.argv[1:]).strip()

if not query:
    print("Usage: python scripts/search_vector.py <question>")
    sys.exit(1)

model = SentenceTransformer("BAAI/bge-small-zh-v1.5")

client = chromadb.PersistentClient(path="db/chroma")

collection = client.get_collection(
    name="github_rag_knowledge"
)

query_embedding = model.encode(
    [query],
    normalize_embeddings=True
).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

print(f"Query: {query}")

for i in range(len(results["ids"][0])):
    print()
    print("=" * 50)
    print(f"Rank: {i + 1}")
    print(f"ID: {results['ids'][0][i]}")
    print(f"Distance: {results['distances'][0][i]}")
    print(f"Title: {results['metadatas'][0][i]['title']}")
    print(f"Source: {results['metadatas'][0][i]['source']}")
    print("-" * 50)
    print(results["documents"][0][i][:500])
