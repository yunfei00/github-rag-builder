import json
import sys
from pathlib import Path

query = " ".join(sys.argv[1:]).strip()

if not query:
    print("Usage: python scripts/search_keyword.py <your question>")
    sys.exit(1)

knowledge_file = Path("knowledge/langchain/knowledge.json")

items = json.loads(
    knowledge_file.read_text(encoding="utf-8")
)

results = []

for item in items:
    text = (item["title"] + "\n" + item["content"]).lower()
    score = 0

    for word in query.lower().split():
        if word in text:
            score += 1

    if score > 0:
        results.append((score, item))

results.sort(key=lambda x: x[0], reverse=True)

print(f"Query: {query}")
print(f"Results: {len(results)}")

for score, item in results[:3]:
    print()
    print("=" * 50)
    print(f"Score: {score}")
    print(f"Chunk ID: {item['chunk_id']}")
    print(f"Source: {item['source']}")
    print(f"File: {item['file']}")
    print(f"Title: {item['title']}")
    print("-" * 50)
    print(item["content"][:500])
