import re


QUERY_INSTRUCTION = "为这个句子生成表示以用于检索相关文章："

TITLE_ALIASES = {
    "为什么": ["why"],
    "为何": ["why"],
    "使用": ["use"],
    "用": ["use"],
    "优势": ["benefit", "benefits", "advantage", "advantages"],
    "生态": ["ecosystem"],
    "资源": ["resources"],
    "快速": ["quickstart", "quick", "start"],
}


def build_query_text(question):
    return QUERY_INSTRUCTION + question


def candidate_count(top_k):
    return max(top_k * 3, 5)


def chunks_from_results(results):
    chunks = []

    for index, chunk_id in enumerate(results["ids"][0]):
        chunks.append({
            "id": chunk_id,
            "document": results["documents"][0][index],
            "metadata": results["metadatas"][0][index],
            "distance": results["distances"][0][index],
        })

    return chunks


def rerank_chunks(question, chunks, top_k):
    ranked_chunks = sorted(
        chunks,
        key=lambda chunk: chunk["distance"] - title_bonus(question, chunk["metadata"])
    )

    return ranked_chunks[:top_k]


def title_bonus(question, metadata):
    title = normalize_text(metadata.get("title", ""))
    terms = query_terms(question)

    hits = sum(1 for term in terms if term and term in title)

    return hits * 0.04


def query_terms(question):
    normalized_question = normalize_text(question)
    terms = set(re.findall(r"[a-z0-9]+", normalized_question))

    for keyword, aliases in TITLE_ALIASES.items():
        if keyword in question:
            terms.update(aliases)

    return terms


def normalize_text(text):
    return text.lower().replace("?", "").strip()
