import os
import sys
from pathlib import Path

import chromadb
from openai import OpenAI
from sentence_transformers import SentenceTransformer


ROOT_DIR = Path(__file__).resolve().parents[1]
DB_DIR = ROOT_DIR / "db" / "chroma"
COLLECTION_NAME = "github_rag_knowledge"
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"
TOP_K = 3


def retrieve_chunks(question):
    if not DB_DIR.exists():
        raise RuntimeError(
            f"Vector DB not found: {DB_DIR}. "
            "Run `python scripts/build_vector_db.py` first."
        )

    model = SentenceTransformer(EMBEDDING_MODEL)

    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_collection(name=COLLECTION_NAME)

    query_embedding = model.encode(
        [question],
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=TOP_K
    )

    ids = results.get("ids", [[]])[0]
    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0]

    chunks = []
    for index, chunk_id in enumerate(ids):
        metadata = metadatas[index] if index < len(metadatas) else {}
        chunks.append({
            "id": chunk_id,
            "document": documents[index] if index < len(documents) else "",
            "metadata": metadata or {},
            "distance": distances[index] if index < len(distances) else None,
        })

    return chunks


def build_prompt(question, chunks):
    context_blocks = []

    for index, chunk in enumerate(chunks, start=1):
        metadata = chunk["metadata"]
        title = metadata.get("title", "")
        source = metadata.get("source", "")
        chunk_id = metadata.get("chunk_id", chunk["id"])

        context_blocks.append(
            f"资料{index}:\n"
            f"标题: {title}\n"
            f"来源: {source}\n"
            f"Chunk ID: {chunk_id}\n\n"
            f"{chunk['document']}"
        )

    context = "\n\n".join(context_blocks)

    return f"""你是知识库助手。

请严格依据以下资料回答问题。

{context}

问题:
{question}

要求：
1. 只能依据资料回答
2. 不允许编造
3. 如果资料不足请明确说明
4. 最后给出引用来源
"""


def print_retrieved_chunks(chunks):
    print("Retrieved Chunks:")

    if not chunks:
        print("(none)")
        return

    for index, chunk in enumerate(chunks, start=1):
        metadata = chunk["metadata"]
        print()
        print("=" * 50)
        print(f"Chunk: {index}")
        print(f"ID: {chunk['id']}")
        if chunk["distance"] is not None:
            print(f"Distance: {chunk['distance']}")
        print(f"Title: {metadata.get('title', '')}")
        print(f"Source: {metadata.get('source', '')}")
        print("-" * 50)
        print(chunk["document"])


def ask_llm(prompt):
    api_key = os.getenv("LLM_API_KEY")
    base_url = os.getenv("LLM_BASE_URL")
    model = os.getenv("LLM_MODEL")

    if not api_key:
        raise RuntimeError("Missing environment variable: LLM_API_KEY")

    if not model:
        raise RuntimeError("Missing environment variable: LLM_MODEL")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content or ""


def main():
    question = input("Question: ").strip()

    if not question:
        print("Question cannot be empty.")
        sys.exit(1)

    try:
        chunks = retrieve_chunks(question)
    except RuntimeError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    prompt = build_prompt(question, chunks)

    print()
    print("Question:")
    print(question)
    print()
    print_retrieved_chunks(chunks)
    print()
    print("Answer:")
    try:
        print(ask_llm(prompt))
    except RuntimeError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
