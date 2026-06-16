from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = PROJECT_ROOT / "config" / "config.yaml"
EXAMPLE_CONFIG_FILE = PROJECT_ROOT / "config" / "config.example.yaml"


def load_config():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            "Config file not found. Please copy "
            f"{EXAMPLE_CONFIG_FILE} to {CONFIG_FILE} and edit it."
        )

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def project_path(path_value):
    path = Path(path_value)

    if path.is_absolute():
        return path

    return PROJECT_ROOT / path
