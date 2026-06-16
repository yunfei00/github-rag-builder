from pathlib import Path
import re

input_file = Path(
    "knowledge/langchain/README.md"
)

text = input_file.read_text(
    encoding="utf-8"
)

# 删除HTML标签
text = re.sub(
    r"<[^>]+>",
    "",
    text
)

# 删除图片链接
text = re.sub(
    r"!\[.*?\]\(.*?\)",
    "",
    text
)

# 删除连续空行
text = re.sub(
    r"\n{3,}",
    "\n\n",
    text
)

output_file = Path(
    "knowledge/langchain/README_clean.md"
)

output_file.write_text(
    text,
    encoding="utf-8"
)

print("clean done")
