import json
import re
from collections import Counter
from pathlib import Path

import yaml


ROOT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
OUTPUT_FILE = KNOWLEDGE_DIR / "knowledge_all.json"


def iter_clean_dirs():
    return sorted(
        path / "clean"
        for path in KNOWLEDGE_DIR.iterdir()
        if path.is_dir() and (path / "clean").exists()
    )


def split_front_matter(text):
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    metadata_text = text[4:end]
    body = text[end + len("\n---\n"):]

    return yaml.safe_load(metadata_text) or {}, body


def chunk_markdown(text, fallback_title):
    chunks = chunk_by_heading(text, level=2)

    if chunks:
        return chunks

    chunks = chunk_by_heading(text, level=1)

    if chunks:
        return chunks

    content = text.strip()
    if not content:
        return []

    return [{
        "title": fallback_title,
        "content": content,
    }]


def chunk_by_heading(text, level):
    heading = "#" * level
    pattern = re.compile(rf"^{heading}\s+(.+?)\s*$")
    chunks = []
    current_title = None
    current_lines = []

    for line in text.splitlines():
        match = pattern.match(line)

        if match:
            if current_title is not None:
                chunks.append({
                    "title": current_title,
                    "content": "\n".join(current_lines).strip(),
                })

            current_title = match.group(1).strip()
            current_lines = []
            continue

        if current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        chunks.append({
            "title": current_title,
            "content": "\n".join(current_lines).strip(),
        })

    return [
        chunk
        for chunk in chunks
        if chunk["title"] or chunk["content"]
    ]


def default_file_name(clean_file):
    return clean_file.name.replace("_clean.md", ".md")


def main():
    knowledge = []
    file_count = 0
    source_chunk_counts = Counter()
    source_indexes = Counter()

    for clean_dir in iter_clean_dirs():
        source = clean_dir.parent.name

        for clean_file in sorted(clean_dir.glob("*.md")):
            file_count += 1
            metadata, body = split_front_matter(
                clean_file.read_text(encoding="utf-8", errors="ignore")
            )

            file_path = metadata.get("path") or default_file_name(clean_file)
            fallback_title = Path(file_path).stem.replace("_", " ").strip() or file_path

            for chunk in chunk_markdown(body, fallback_title):
                source_indexes[source] += 1
                source_chunk_counts[source] += 1

                knowledge.append({
                    "chunk_id": f"{source}_{source_indexes[source]:04d}",
                    "source": metadata.get("source", source),
                    "file": file_path,
                    "title": chunk["title"],
                    "content": chunk["content"],
                    "repo": metadata.get("repo", ""),
                    "path": metadata.get("path", file_path),
                    "url": metadata.get("url", ""),
                })

    OUTPUT_FILE.write_text(
        json.dumps(knowledge, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Projects: {len(source_chunk_counts)}")
    print(f"Files: {file_count}")
    print(f"Chunks: {len(knowledge)}")
    print()
    print("Chunks by Source:")

    for source in sorted(source_chunk_counts):
        print(f"{source}: {source_chunk_counts[source]}")


if __name__ == "__main__":
    main()
