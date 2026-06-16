import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config_loader import load_config
from src.knowledge_utils import (
    ask_llm,
    chunks_for_source,
    format_chunks,
    load_knowledge,
    select_representative_chunks,
)


MAX_CHUNKS = 30


def build_prompt(source, chunks):
    return f"""你是高级技术项目分析助手。
请基于下面项目资料，生成项目技术摘要。

要求：
1. 只能依据资料内容总结
2. 不允许编造
3. 如果资料不足，请说明
4. 输出中文

输出结构：

# 项目概述

# 主要功能

# 技术栈

# 核心模块

# 数据流程 / 业务流程

# 项目亮点

# 当前不足

# 可扩展方向

# 简历表达建议

项目：
{source}

资料：
{format_chunks(chunks)}
"""


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/project_summary.py <source>")
        sys.exit(1)

    source = sys.argv[1].strip()

    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    items = load_knowledge(cfg)
    source_chunks = chunks_for_source(items, source)

    if not source_chunks:
        print(f"Source not found: {source}")
        sys.exit(1)

    chunks = select_representative_chunks(source_chunks, MAX_CHUNKS)
    prompt = build_prompt(source, chunks)
    answer = ask_llm(
        cfg,
        "你是高级技术项目分析助手，只能依据提供的项目资料进行分析。",
        prompt
    )

    print(f"Project: {source}")
    print(f"Chunks used: {len(chunks)}")
    print()
    print("Answer:")
    print(answer)


if __name__ == "__main__":
    main()
