from pathlib import Path

text = Path(
    "knowledge/langchain/README.md"
).read_text(
    encoding="utf-8"
)

chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(
        text[i:i+chunk_size]
    )

print(f"Total chunks: {len(chunks)}")

for idx, chunk in enumerate(chunks[:3]):
    print("\n")
    print("=" * 50)
    print(f"Chunk {idx}")
    print("=" * 50)
    print(chunk[:300])
