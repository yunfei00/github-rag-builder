---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/reference/typescript/collection.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/reference/typescript/collection.mdx
---
---
title: "Collection"
---

## Collection Methods

### count

Gets the total number of records in the collection

### add

Adds new records to the collection.

### get

Retrieves records from the collection based on filters.

**Returns:** Promise resolving to matching records

### peek

Retrieves a preview of records from the collection.

**Returns:** Promise resolving to a sample of records

### query

Performs similarity search on the collection.

**Returns:** Promise resolving to similar records ranked by distance

### modify

Modifies collection properties like name, metadata, or configuration.

### update

Updates existing records in the collection.

### upsert

Inserts new records or updates existing ones (upsert operation).

### delete

Deletes records from the collection based on filters.

### search

Performs hybrid search on the collection using expression builders.

  Single search payload or array of payloads

**Returns:** Promise resolving to column-major search results

---

## Types

### GetResult

Result class for get operations, containing retrieved records.

Properties

### QueryResult

Result class for query operations, containing search results.

Properties
