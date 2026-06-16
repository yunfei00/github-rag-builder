import json
from collections import Counter
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_FILE = ROOT_DIR / "knowledge" / "knowledge_all.json"


def main():
    items = json.loads(KNOWLEDGE_FILE.read_text(encoding="utf-8"))

    projects = {item["source"] for item in items}
    files = {(item["source"], item["file"]) for item in items}
    chunk_counts = Counter(item["source"] for item in items)

    print(f"Project Count: {len(projects)}")
    print(f"File Count: {len(files)}")
    print(f"Chunk Count: {len(items)}")
    print()
    print("Chunks by Project:")

    for source in sorted(chunk_counts):
        print(f"{source}: {chunk_counts[source]}")


if __name__ == "__main__":
    main()
