from pathlib import Path
import re

text = Path(
    "knowledge/langchain/README_clean.md"
).read_text(
    encoding="utf-8"
)

sections = re.split(
    r"\n## ",
    text
)

print(f"Sections: {len(sections)-1}")

for idx, section in enumerate(sections[1:]):
    title = section.split("\n")[0].strip()

    print()
    print("=" * 50)
    print(f"Chunk {idx+1}")
    print(f"Title: {title}")
    print("=" * 50)

    content = "\n".join(
        section.split("\n")[1:]
    )

    print(content[:300])
