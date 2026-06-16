import json
from collections import defaultdict

from openai import OpenAI

from src.config_loader import project_path


SUMMARY_KEYWORDS = [
    "README",
    "overview",
    "architecture",
    "设计",
    "架构",
    "功能",
    "usage",
    "quickstart",
    "workflow",
    "pipeline",
    "model",
    "training",
    "deployment",
    "scan",
    "scanner",
]


def load_knowledge(cfg):
    knowledge_file = project_path(cfg["knowledge"]["file"])

    return json.loads(knowledge_file.read_text(encoding="utf-8"))


def source_stats(items):
    files_by_source = defaultdict(set)
    chunks_by_source = defaultdict(int)

    for item in items:
        source = item["source"]
        files_by_source[source].add(item["file"])
        chunks_by_source[source] += 1

    rows = []
    for source in sorted(chunks_by_source, key=lambda name: (-chunks_by_source[name], name)):
        rows.append({
            "source": source,
            "chunk_count": chunks_by_source[source],
            "file_count": len(files_by_source[source]),
        })

    return rows


def chunks_for_source(items, source):
    return [
        item
        for item in items
        if item["source"] == source
    ]


def select_representative_chunks(chunks, limit):
    indexed_chunks = list(enumerate(chunks))

    ranked = sorted(
        indexed_chunks,
        key=lambda pair: (-chunk_score(pair[1]), pair[0])
    )

    return [
        chunk
        for _, chunk in ranked[:limit]
    ]


def chunk_score(chunk):
    title = chunk.get("title", "")
    content = chunk.get("content", "")
    file_name = chunk.get("file", "")
    haystack = f"{title}\n{content}".lower()
    score = 0

    if "readme" in file_name.lower():
        score += 3

    for keyword in SUMMARY_KEYWORDS:
        keyword_lower = keyword.lower()
        if keyword_lower in title.lower():
            score += 3
        if keyword_lower in haystack:
            score += 1

    return score


def format_chunks(chunks, max_chars=1200):
    blocks = []

    for index, chunk in enumerate(chunks, start=1):
        content = chunk.get("content", "").strip()

        if len(content) > max_chars:
            content = content[:max_chars].rstrip() + "\n..."

        blocks.append(
            f"资料{index}:\n"
            f"source: {chunk.get('source', '')}\n"
            f"file: {chunk.get('file', '')}\n"
            f"title: {chunk.get('title', '')}\n"
            f"url: {chunk.get('url', '')}\n"
            f"content:\n{content}"
        )

    return "\n\n".join(blocks)


def ask_llm(cfg, system_prompt, user_prompt):
    client = OpenAI(
        api_key=cfg["llm"]["api_key"],
        base_url=cfg["llm"]["base_url"]
    )

    completion = client.chat.completions.create(
        model=cfg["llm"]["model"],
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2
    )

    return completion.choices[0].message.content or ""
