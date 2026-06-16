---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/reference/python/collection.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/reference/python/collection.mdx
---
---
title: "Collection"
---

## Collection Methods

### count

Return the number of records in the collection.

### add

Add records to the collection.

  Record IDs to add.

  Embeddings to add. If None, embeddings are computed.

  Optional metadata for each record.

  Optional documents for each record.

  Optional images for each record.

  Optional URIs for loading images.

**Raises:**

- ValueError: If embeddings and documents are both missing.
- ValueError: If embeddings and documents are both provided.
- ValueError: If lengths of provided fields do not match.
- ValueError: If an ID already exists.

### get

Retrieve records from the collection.

If no filters are provided, returns records up to ``limit`` starting at
``offset``.

  If provided, only return records with these IDs.

  A Where filter used to filter based on metadata values.

  Maximum number of results to return.

  Number of results to skip before returning.

  A WhereDocument filter used to filter based on K.DOCUMENT.

  Fields to include in results. Can contain "embeddings", "metadatas", "documents", "uris". Defaults to "metadatas" and "documents".

**Returns:** Retrieved records and requested fields as a GetResult object.

### peek

Return the first ``limit`` records from the collection.

  Maximum number of records to return.

**Returns:** Retrieved records and requested fields.

### query

Query for the K nearest neighbor records in the collection.

This is a batch query API. Multiple queries can be performed at once
by providing multiple embeddings, texts, or images.

```python
query_1 = [0.1, 0.2, 0.3]
query_2 = [0.4, 0.5, 0.6]
results = collection.query(
    query_embeddings=[query_1, query_2],
    n_results=10,
)
```

If query_texts, query_images, or query_uris are provided, the collection's
embedding function will be used to create embeddings before querying
the API.

The `ids`, `where`, `where_document`, and `include` parameters are applied
to all queries.

  Raw embeddings to query for.

  Documents to embed and query against.

  Images to embed and query against.

  URIs to be loaded and embedded.

  Optional subset of IDs to search within.

  Number of neighbors to return per query.

  Metadata filter.

  Document content filter.

  Fields to include in results. Can contain "embeddings", "metadatas", "documents", "uris", "distances". Defaults to "metadatas", "documents", "distances".

**Returns:** Nearest neighbor results.

**Raises:**

- ValueError: If no query input is provided.
- ValueError: If multiple query input types are provided.

### modify

Update collection name, metadata, or configuration.

  New collection name.

  New metadata for the collection.

  New configuration for the collection.

### update

Update existing records by ID.

Records are provided in columnar format. If provided, the `embeddings`, `metadatas`, `documents`, and `uris` lists must be the same length.
Entries in each list correspond to the same record.

```python
ids = ["id1", "id2", "id3"]
embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
metadatas = [{"key": "value"}, {"key": "value"}, {"key": "value"}]
documents = ["document1", "document2", "document3"]
uris = ["uri1", "uri2", "uri3"]
collection.update(ids, embeddings, metadatas, documents, uris)
```

If `embeddings` are not provided, the embeddings will be computed based on `documents` using the collection's embedding function.

  Record IDs to update.

  Updated embeddings. If None, embeddings are computed.

  Updated metadata.

  Updated documents.

  Updated images.

  Updated URIs for loading images.

### upsert

Create or update records by ID.

  Record IDs to upsert.

  Embeddings to add or update. If None, embeddings are computed.

  Metadata to add or update.

  Documents to add or update.

  Images to add or update.

  URIs for loading images.

### delete

Delete records by ID or filters.

All documents that match the `ids` or `where` and `where_document` filters will be deleted.

  Record IDs to delete.

  Metadata filter.

  Document content filter.

**Raises:**

- ValueError: If no IDs or filters are provided.

---

## Types

### GetResult

Result payload for collection.get() operations.

The returned records are in columnar form. Corresponding entries in each list correspond to the same record.

```python
results = collection.get(ids=["id1", "id2", "id3"])
records = zip(results["ids"], results["documents"], results["metadatas"])
for id, document, metadata in records:
    print(id, document, metadata)
```

GetResult will only include ids and the fields specified in the `include` param
when making the get() operation.

Properties

### QueryResult

Result payload for collection.query() operations.

The returned records are batches of records in columnar form.

```python
results = collection.query(query_embeddings=[batch_1, batch_2, ...])
batches = zip(results["ids"], results["documents"], results["metadatas"])
```

Each batch is a list of records in columnar form.

```python
for batch in batches:
    records = zip(batch["ids"], batch["documents"], batch["metadatas"])
    for id, document, metadata in records:
        print(id, document, metadata)
```

QueryResult will only include ids and the fields specified in the `include` param
when making the query() operation.

Properties
