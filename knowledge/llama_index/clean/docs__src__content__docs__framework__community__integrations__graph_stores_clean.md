---
source: llama_index
owner: run-llama
repo: llama_index
path: docs/src/content/docs/framework/community/integrations/graph_stores.md
url: https://github.com/run-llama/llama_index/blob/main/docs/src/content/docs/framework/community/integrations/graph_stores.md
---
---
title: Using Graph Stores
---

## `Neo4jGraphStore`

`Neo4j` is supported as a graph store integration. You can persist, visualize, and query graphs using LlamaIndex and Neo4j. Furthermore, existing Neo4j graphs are directly supported using `text2cypher` and the `KnowledgeGraphQueryEngine`.

If you've never used Neo4j before, you can download the desktop client here.

Once you open the client, create a new project and install the `apoc` integration. Full instructions here. Just click on your project, select `Plugins` on the left side menu, install APOC and restart your server.

See the example of using the Neo4j Graph Store.

## `NebulaGraphStore`

We support a `NebulaGraphStore` integration, for persisting graphs directly in Nebula! Furthermore, you can generate cypher queries and return natural language responses for your Nebula graphs using the `KnowledgeGraphQueryEngine`.

See the associated guides below:

- Nebula Graph Store
- Knowledge Graph Query Engine

## `FalkorDBGraphStore`

We support a `FalkorDBGraphStore` integration, for persisting graphs directly in FalkorDB! Furthermore, you can generate cypher queries and return natural language responses for your FalkorDB graphs using the `KnowledgeGraphQueryEngine`.

See the associated guides below:

- FalkorDB Graph Store

## `Amazon Neptune Graph Stores`

We support `Amazon Neptune` integrations for both Neptune Database and Neptune Analytics as a graph store integration.

See the associated guides below:

- Amazon Neptune Graph Store.

## `TiDB Graph Store`

We support a `TiDBGraphStore` integration, for persisting graphs directly in TiDB!

See the associated guides below:

- TiDB Graph Store
