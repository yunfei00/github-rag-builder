import requests
from pathlib import Path

OWNER = "langchain-ai"
REPO = "langchain"

SAVE_DIR = Path("knowledge/langchain")
SAVE_DIR.mkdir(parents=True, exist_ok=True)

url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"

resp = requests.get(url)
resp.raise_for_status()

files = resp.json()

for item in files:
    if item["type"] == "file" and item["name"].endswith(".md"):
        print(f"Downloading {item['name']}")

        md = requests.get(item["download_url"])
        md.raise_for_status()

        (SAVE_DIR / item["name"]).write_text(
            md.text,
            encoding="utf-8"
        )

print("Done")
