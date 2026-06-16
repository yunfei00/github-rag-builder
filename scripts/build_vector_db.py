import json
import sys
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config_loader import load_config, project_path


def collection_exists(client, collection_name):
    return collection_name in [
        getattr(collection, "name", collection)
        for collection in client.list_collections()
    ]


def main():
    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    knowledge_file = project_path(cfg["knowledge"]["file"])
    embedding_model_path = project_path(cfg["embedding"]["model_path"])
    vector_db_path = project_path(cfg["vector_db"]["path"])
    collection_name = cfg["vector_db"]["collection"]

    items = json.loads(knowledge_file.read_text(encoding="utf-8"))

    model = SentenceTransformer(str(embedding_model_path))

    client = chromadb.PersistentClient(path=str(vector_db_path))

    if collection_exists(client, collection_name):
        client.delete_collection(name=collection_name)

    collection = client.create_collection(name=collection_name)

    ids = []
    documents = []
    metadatas = []

    for item in items:
        text = f"{item['title']}\n\n{item['content']}"

        ids.append(item["chunk_id"])
        documents.append(text)
        metadatas.append({
            "source": item["source"],
            "file": item["file"],
            "title": item["title"],
            "chunk_id": item["chunk_id"],
        })

    embeddings = model.encode(
        documents,
        normalize_embeddings=True
    ).tolist()

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    print(f"Vector DB built successfully: {len(ids)} chunks")


if __name__ == "__main__":
    main()
