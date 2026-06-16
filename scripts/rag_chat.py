import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config_loader import load_config, project_path
from src.knowledge_utils import ask_llm, load_knowledge, source_stats
from src.retrieval_utils import (
    build_query_text,
    candidate_count,
    chunks_from_results,
    rerank_chunks,
)


def retrieve_chunks(question, cfg, model, collection):
    top_k = int(cfg["retriever"]["top_k"])
    query_embedding = model.encode(
        [build_query_text(question)],
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=candidate_count(top_k)
    )

    return rerank_chunks(
        question,
        chunks_from_results(results),
        top_k
    )


def build_prompt(question, chunks):
    context_blocks = []

    for index, chunk in enumerate(chunks, start=1):
        metadata = chunk["metadata"]
        context_blocks.append(
            f"资料{index}:\n"
            f"标题：\n{metadata.get('title', '')}\n"
            f"来源：\n{metadata.get('source', '')}\n"
            f"文件：\n{metadata.get('file', '')}\n"
            f"内容：\n{chunk['document']}"
        )

    context = "\n\n".join(context_blocks)

    return f"""你是知识库助手。

请严格依据以下资料回答问题。

{context}

问题：
{question}

要求：
1. 只能依据资料回答
2. 不允许编造
3. 如果资料不足，请回答“资料中没有足够信息”
4. 最后给出引用来源
"""


def print_retrieved_chunks(chunks):
    print("Retrieved Chunks:")

    for index, chunk in enumerate(chunks, start=1):
        metadata = chunk["metadata"]
        print(
            f"{index}. {metadata.get('title', '')} | "
            f"{metadata.get('source', '')} | "
            f"{metadata.get('file', '')} | "
            f"distance={chunk['distance']}"
        )


def print_sources(cfg):
    items = load_knowledge(cfg)
    print("source\tchunk_count\tfile_count")

    for row in source_stats(items):
        print(f"{row['source']}\t{row['chunk_count']}\t{row['file_count']}")


def answer_question(question, cfg, model, collection):
    chunks = retrieve_chunks(question, cfg, model, collection)
    prompt = build_prompt(question, chunks)
    answer = ask_llm(
        cfg,
        "你是一个严谨的知识库助手，只能依据提供的资料回答。",
        prompt
    )

    print()
    print("Question:")
    print(question)
    print()
    print_retrieved_chunks(chunks)
    print()
    print("Answer:")
    print(answer)
    print()


def main():
    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    embedding_model_path = project_path(cfg["embedding"]["model_path"])
    vector_db_path = project_path(cfg["vector_db"]["path"])
    collection_name = cfg["vector_db"]["collection"]

    model = SentenceTransformer(str(embedding_model_path))
    client = chromadb.PersistentClient(path=str(vector_db_path))
    collection = client.get_collection(name=collection_name)

    while True:
        question = input("Question: ").strip()

        if not question:
            continue

        if question == "/exit":
            print("Bye.")
            break

        if question == "/sources":
            print_sources(cfg)
            continue

        answer_question(question, cfg, model, collection)


if __name__ == "__main__":
    main()
