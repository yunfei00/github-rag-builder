import re
import shutil
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"


def split_front_matter(text):
    if not text.startswith("---\n"):
        return "", text

    end = text.find("\n---\n", 4)
    if end == -1:
        return "", text

    return text[:end + len("\n---\n")], text[end + len("\n---\n"):]


def clean_markdown(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"<img\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[!\[[^\]]*\]\([^)]+\)\]\([^)]+\)", "", text)
    text = re.sub(r"\[\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = remove_badge_lines(text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() + "\n"


def remove_badge_lines(text):
    cleaned_lines = []

    for line in text.splitlines():
        lower_line = line.lower()

        if "shields.io" in lower_line:
            continue

        if "badge" in lower_line and not line.strip().startswith("#"):
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def clean_file_name(raw_file):
    return f"{raw_file.stem}_clean.md"


def main():
    project_count = 0
    file_count = 0

    for project_dir in sorted(path for path in KNOWLEDGE_DIR.iterdir() if path.is_dir()):
        raw_dir = project_dir / "raw"

        if not raw_dir.exists():
            continue

        clean_dir = project_dir / "clean"
        if clean_dir.exists():
            shutil.rmtree(clean_dir)
        clean_dir.mkdir(parents=True, exist_ok=True)

        project_count += 1

        for raw_file in sorted(raw_dir.iterdir()):
            if not raw_file.is_file():
                continue

            front_matter, body = split_front_matter(
                raw_file.read_text(encoding="utf-8", errors="ignore")
            )
            output_file = clean_dir / clean_file_name(raw_file)
            output_file.write_text(
                front_matter + clean_markdown(body),
                encoding="utf-8"
            )
            file_count += 1

    print(f"Projects: {project_count}")
    print(f"Files: {file_count}")


if __name__ == "__main__":
    main()
