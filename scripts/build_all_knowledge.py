import json
import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"
OUTPUT_FILE = KNOWLEDGE_DIR / "knowledge_all.json"


def iter_project_dirs():
    return sorted(
        path
        for path in KNOWLEDGE_DIR.iterdir()
        if path.is_dir()
    )


def iter_clean_files(project_dir):
    return sorted(project_dir.rglob("*_clean.md"))


def original_file_name(project_dir, clean_file):
    relative_path = clean_file.relative_to(project_dir)
    file_name = relative_path.name.replace("_clean.md", ".md")
    return str(relative_path.with_name(file_name)).replace("\\", "/")


def chunk_markdown(text):
    chunks = []
    current_title = None
    current_lines = []

    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)

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

    return chunks


def main():
    knowledge = []
    project_count = 0
    file_count = 0

    for project_dir in iter_project_dirs():
        clean_files = iter_clean_files(project_dir)

        if not clean_files:
            continue

        project_count += 1
        source = project_dir.name
        project_chunk_index = 1

        for clean_file in clean_files:
            file_count += 1
            file_name = original_file_name(project_dir, clean_file)
            text = clean_file.read_text(encoding="utf-8")

            for chunk in chunk_markdown(text):
                knowledge.append({
                    "chunk_id": f"{source}_{project_chunk_index:03d}",
                    "source": source,
                    "file": file_name,
                    "title": chunk["title"],
                    "content": chunk["content"],
                })
                project_chunk_index += 1

    OUTPUT_FILE.write_text(
        json.dumps(knowledge, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Projects: {project_count}")
    print(f"Files: {file_count}")
    print(f"Chunks: {len(knowledge)}")


if __name__ == "__main__":
    main()
