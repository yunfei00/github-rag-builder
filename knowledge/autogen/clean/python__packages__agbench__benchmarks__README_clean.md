---
source: autogen
owner: microsoft
repo: autogen
path: python/packages/agbench/benchmarks/README.md
url: https://github.com/microsoft/autogen/blob/main/python/packages/agbench/benchmarks/README.md
---
# Benchmarking Agents

This directory provides ability to benchmarks agents (e.g., built using Autogen) using AgBench. Use the instructions below to prepare your environment for benchmarking. Once done, proceed to relevant benchmarks directory (e.g., `benchmarks/GAIA`) for further scenario-specific instructions.

## Setup on WSL

1. Install Docker Desktop. After installation, restart is needed, then open Docker Desktop, in Settings, Ressources, WSL Integration, Enable integration with additional distros – Ubuntu
2. Clone autogen and export `AUTOGEN_REPO_BASE`. This environment variable enables the Docker containers to use the correct version agents.
    ```bash
    git clone git@github.com:microsoft/autogen.git
    export AUTOGEN_REPO_BASE=
    ```
3. Install `agbench`. AgBench is currently a tool in the Autogen repo.

    ```bash
    cd autogen/python/packages/agbench
    pip install -e .
    ```
