import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config_loader import load_config, project_path


def main():
    query = " ".join(sys.argv[1:]).strip()

    if not query:
        print("Usage: python scripts/search_vector.py <question>")
        sys.exit(1)

    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    embedding_model_path = project_path(cfg["embedding"]["model_path"])
    vector_db_path = project_path(cfg["vector_db"]["path"])
    collection_name = cfg["vector_db"]["collection"]
    top_k = int(cfg["retriever"]["top_k"])

    model = SentenceTransformer(str(embedding_model_path))

    client = chromadb.PersistentClient(path=str(vector_db_path))
    collection = client.get_collection(name=collection_name)

    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    ).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    ids = results["ids"][0]
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    print(f"Query: {query}")

    for index, chunk_id in enumerate(ids):
        metadata = metadatas[index]

        print()
        print("=" * 50)
        print(f"Rank: {index + 1}")
        print(f"Chunk ID: {chunk_id}")
        print(f"Title: {metadata.get('title', '')}")
        print(f"Source: {metadata.get('source', '')}")
        print(f"File: {metadata.get('file', '')}")
        print(f"Distance: {distances[index]}")
        print("-" * 50)
        print("Content preview:")
        print(documents[index][:500])


if __name__ == "__main__":
    main()
