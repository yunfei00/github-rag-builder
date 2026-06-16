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


MAX_CHUNKS_PER_PROJECT = 20


def build_prompt(source_a, chunks_a, source_b, chunks_b):
    return f"""你是高级技术项目分析助手。
请严格依据下面两个项目的资料，生成中文项目对比报告。

要求：
1. 只能依据资料内容总结
2. 不允许编造
3. 如果资料不足，请明确说明
4. 输出中文

输出结构：

# 项目A概述

# 项目B概述

# 技术方向对比

# 架构复杂度对比

# 数据处理方式对比

# 工程化程度对比

# 简历价值对比

# 后续优化建议

项目A：{source_a}
资料A：
{format_chunks(chunks_a, max_chars=1000)}

项目B：{source_b}
资料B：
{format_chunks(chunks_b, max_chars=1000)}
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/compare_projects.py <source_a> <source_b>")
        sys.exit(1)

    source_a = sys.argv[1].strip()
    source_b = sys.argv[2].strip()

    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    items = load_knowledge(cfg)
    chunks_a = chunks_for_source(items, source_a)
    chunks_b = chunks_for_source(items, source_b)

    if not chunks_a:
        print(f"Source not found: {source_a}")
        sys.exit(1)

    if not chunks_b:
        print(f"Source not found: {source_b}")
        sys.exit(1)

    selected_a = select_representative_chunks(chunks_a, MAX_CHUNKS_PER_PROJECT)
    selected_b = select_representative_chunks(chunks_b, MAX_CHUNKS_PER_PROJECT)
    prompt = build_prompt(source_a, selected_a, source_b, selected_b)
    answer = ask_llm(
        cfg,
        "你是高级技术项目分析助手，只能依据提供的项目资料进行对比。",
        prompt
    )

    print(f"Project A: {source_a}")
    print(f"Project B: {source_b}")
    print(f"Chunks used: {source_a}={len(selected_a)}, {source_b}={len(selected_b)}")
    print()
    print("Answer:")
    print(answer)


if __name__ == "__main__":
    main()
