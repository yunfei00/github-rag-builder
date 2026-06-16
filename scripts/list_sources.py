import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(errors="replace")

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config_loader import load_config
from src.knowledge_utils import load_knowledge, source_stats


def main():
    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    items = load_knowledge(cfg)

    print("source\tchunk_count\tfile_count")
    for row in source_stats(items):
        print(f"{row['source']}\t{row['chunk_count']}\t{row['file_count']}")


if __name__ == "__main__":
    main()
