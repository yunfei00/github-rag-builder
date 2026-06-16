import json
from collections import defaultdict
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
KNOWLEDGE_FILE = ROOT_DIR / "knowledge" / "knowledge_all.json"


def main():
    items = json.loads(KNOWLEDGE_FILE.read_text(encoding="utf-8"))

    source_file_counts = defaultdict(int)
    source_chunk_counts = defaultdict(int)

    for source_dir in sorted(path for path in KNOWLEDGE_DIR.iterdir() if path.is_dir()):
        clean_dir = source_dir / "clean"

        if not clean_dir.exists():
            continue

        source_file_counts[source_dir.name] = len(list(clean_dir.glob("*.md")))

    for item in items:
        source = item["source"]
        source_chunk_counts[source] += 1

    sources = set(source_file_counts) | set(source_chunk_counts)
    file_count = sum(source_file_counts.values())

    print(f"Project Count: {len(sources)}")
    print(f"File Count: {file_count}")
    print(f"Chunk Count: {len(items)}")
    print()
    print("By Source:")

    for source in sorted(sources):
        print(
            f"{source}: "
            f"files={source_file_counts[source]}, "
            f"chunks={source_chunk_counts[source]}"
        )


if __name__ == "__main__":
    main()
