from pathlib import Path
import re
import json

SOURCE = "langchain"
FILE_NAME = "README.md"

text = Path(
    "knowledge/langchain/README_clean.md"
).read_text(
    encoding="utf-8"
)

sections = re.split(
    r"\n## ",
    text
)

knowledge = []

for idx, section in enumerate(sections[1:], start=1):

    lines = section.split("\n")

    title = lines[0].strip()

    content = "\n".join(
        lines[1:]
    ).strip()

    item = {
        "chunk_id": f"{SOURCE}_{idx:03d}",
        "source": SOURCE,
        "file": FILE_NAME,
        "title": title,
        "content": content
    }

    knowledge.append(item)

output = Path(
    "knowledge/langchain/knowledge.json"
)

output.write_text(
    json.dumps(
        knowledge,
        ensure_ascii=False,
        indent=2
    ),
    encoding="utf-8"
)

print(
    f"Build knowledge.json success: {len(knowledge)} chunks"
)
