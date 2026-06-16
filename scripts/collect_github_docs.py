import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote

import requests


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.config_loader import load_config


GITHUB_API = "https://api.github.com"
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"

ALLOWED_EXTENSIONS = {".md", ".mdx", ".rst", ".txt"}
ALLOWED_README_FILES = {
    "readme.md",
    "readme.zh-cn.md",
    "readme_zh.md",
}
ALLOWED_DOC_DIRS = {
    "docs",
    "doc",
    "documentation",
    "examples",
    "tutorials",
    "guides",
}

SKIP_DIRS = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "dist",
    "build",
    "target",
    "__pycache__",
    "db",
    "models",
}
SKIP_DIR_PREFIXES = {
    ".github/workflows",
    "data/raw",
    "data/processed",
}
SKIP_EXTENSIONS = {
    ".sqlite",
    ".db",
    ".pt",
    ".pth",
    ".onnx",
    ".bin",
    ".safetensors",
    ".zip",
    ".tar",
    ".gz",
    ".png",
    ".jpg",
    ".jpeg",
    ".mp4",
    ".pdf",
    ".docx",
}
SKIP_FILENAMES = {
    ".env",
}
SENSITIVE_NAME_PARTS = {
    "secret",
    "secrets",
    "credential",
    "credentials",
}
MAX_WORKERS = 8


def github_headers():
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def github_get_json(url):
    response = requests.get(url, headers=github_headers(), timeout=30)
    response.raise_for_status()
    return response.json()


def repo_configs(cfg):
    github_repos = cfg.get("github_repos", {})

    for group_name in ("user_repos", "external_repos"):
        for repo in github_repos.get(group_name, []):
            yield repo


def is_public_repo(owner, repo):
    repo_url = f"{GITHUB_API}/repos/{owner}/{repo}"
    repo_info = github_get_json(repo_url)

    return not repo_info.get("private", True), repo_info


def repo_tree(owner, repo, branch):
    tree_url = (
        f"{GITHUB_API}/repos/{owner}/{repo}/git/trees/"
        f"{quote(branch, safe='')}?recursive=1"
    )
    return github_get_json(tree_url)


def should_skip_path(path):
    normalized = path.replace("\\", "/")
    lower_path = normalized.lower()
    parts = lower_path.split("/")
    filename = parts[-1]
    suffix = Path(filename).suffix.lower()

    if filename in SKIP_FILENAMES:
        return True

    if suffix in SKIP_EXTENSIONS:
        return True

    if any(part in SKIP_DIRS for part in parts[:-1]):
        return True

    if any(
        lower_path == prefix or lower_path.startswith(prefix + "/")
        for prefix in SKIP_DIR_PREFIXES
    ):
        return True

    if any(part in filename for part in SENSITIVE_NAME_PARTS):
        return True

    return False


def is_allowed_document(path):
    normalized = path.replace("\\", "/")
    lower_path = normalized.lower()
    parts = lower_path.split("/")
    filename = parts[-1]
    suffix = Path(filename).suffix.lower()

    if suffix not in ALLOWED_EXTENSIONS:
        return False

    if filename in ALLOWED_README_FILES:
        return True

    if parts[0] in ALLOWED_DOC_DIRS:
        return True

    return False


def safe_file_name(path):
    return path.replace("\\", "/").replace("/", "__")


def github_blob_url(owner, repo, branch, path):
    encoded_path = quote(path, safe="/")
    return f"https://github.com/{owner}/{repo}/blob/{branch}/{encoded_path}"


def raw_url(owner, repo, branch, path):
    encoded_path = quote(path, safe="/")
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{encoded_path}"


def metadata_header(source, owner, repo, path, url):
    return (
        "---\n"
        f"source: {source}\n"
        f"owner: {owner}\n"
        f"repo: {repo}\n"
        f"path: {path}\n"
        f"url: {url}\n"
        "---\n\n"
    )


def collect_repo(repo_cfg):
    owner = repo_cfg["owner"]
    repo = repo_cfg["repo"]
    source = repo_cfg["source"]

    print(f"Collecting {owner}/{repo} -> {source}", flush=True)

    try:
        public, repo_info = is_public_repo(owner, repo)
    except requests.HTTPError as exc:
        print(f"Skip {owner}/{repo}: {exc}", flush=True)
        return 0

    if not public:
        print(f"Skip private repo: {owner}/{repo}", flush=True)
        return 0

    branch = repo_info["default_branch"]
    tree = repo_tree(owner, repo, branch)

    if tree.get("truncated"):
        print(f"Warning: tree truncated for {owner}/{repo}", flush=True)

    raw_dir = KNOWLEDGE_DIR / source / "raw"
    if raw_dir.exists():
        shutil.rmtree(raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)

    candidates = []

    for item in tree.get("tree", []):
        if item.get("type") != "blob":
            continue

        path = item["path"]

        if should_skip_path(path):
            continue

        if not is_allowed_document(path):
            continue

        candidates.append(path)

    saved_count = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [
            executor.submit(download_document, owner, repo, source, branch, path, raw_dir)
            for path in candidates
        ]

        for future in as_completed(futures):
            try:
                saved = future.result()
            except requests.RequestException as exc:
                print(f"Download failed: {exc}", flush=True)
                continue

            if saved:
                saved_count += 1

    print(f"{source}: {saved_count} files", flush=True)
    return saved_count


def download_document(owner, repo, source, branch, path, raw_dir):
    document_url = raw_url(owner, repo, branch, path)
    response = requests.get(document_url, timeout=30)
    response.raise_for_status()

    blob_url = github_blob_url(owner, repo, branch, path)
    output_file = raw_dir / safe_file_name(path)
    output_file.write_text(
        metadata_header(source, owner, repo, path, blob_url) + response.text,
        encoding="utf-8"
    )

    return True


def main():
    try:
        cfg = load_config()
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    total_repos = 0
    total_files = 0

    for repo_cfg in repo_configs(cfg):
        total_repos += 1
        total_files += collect_repo(repo_cfg)

    print(f"Repos: {total_repos}", flush=True)
    print(f"Files: {total_files}", flush=True)


if __name__ == "__main__":
    main()
