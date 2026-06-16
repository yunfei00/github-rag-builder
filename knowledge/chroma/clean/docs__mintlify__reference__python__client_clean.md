---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/reference/python/client.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/reference/python/client.mdx
---
---
title: "Client"
---

## Clients

### EphemeralClient

Create an in-memory client for local use.

This client stores all data in memory and does not persist to disk.
It is intended for testing and development.

  Optional settings to override defaults.

  Tenant name to use for requests. Defaults to the default tenant.

  Database name to use for requests. Defaults to the default database.

### PersistentClient

Create a persistent client that stores data on disk.

This client is intended for local development and testing. For production,
prefer a server-backed Chroma instance.

  Directory to store persisted data.

  Optional settings to override defaults.

  Tenant name to use for requests.

  Database name to use for requests.

### HttpClient

Create a client that connects to a Chroma server.

  Hostname of the Chroma server.

  HTTP port of the Chroma server.

  Whether to enable SSL for the connection.

  Optional headers to send with each request.

  Optional settings to override defaults.

  Tenant name to use for requests.

  Database name to use for requests.

### AsyncHttpClient

Create an async client that connects to a Chroma HTTP server.

This supports multiple clients connecting to the same server and is the
recommended production configuration.

  Hostname of the Chroma server.

  HTTP port of the Chroma server.

  Whether to enable SSL for the connection.

  Optional headers to send with each request.

  Optional settings to override defaults.

  Tenant name to use for requests.

  Database name to use for requests.

### CloudClient

Create a client for Chroma Cloud.

If not provided, `tenant`, `database`, and `api_key` will be inferred from the environment variables `CHROMA_TENANT`, `CHROMA_DATABASE`, and `CHROMA_API_KEY`.

  Tenant name to use, or None to infer from credentials.

  Database name to use, or None to infer from credentials.

  API key for Chroma Cloud.

  Optional settings to override defaults.

### AdminClient

Create an admin client for tenant and database management.

---

## Client Methods

### heartbeat

Get the current time in nanoseconds since epoch.

Used to check if the server is alive.

**Returns:** The current time in nanoseconds since epoch

### list_collections

List all collections.

  The maximum number of entries to return. Defaults to None.

  The number of entries to skip before returning. Defaults to None.

**Returns:** A list of collections

### count_collections

Count the number of collections.

**Returns:** The number of collections.

### create_collection

Create a new collection with the given name and metadata.

  The name of the collection to create.

  Optional metadata to associate with the collection.

  Optional function to use to embed documents.
Uses the default embedding function if not provided.

  Optional function to use to load records (documents, images, etc.)

  If True, return the existing collection if it exists.

**Returns:** The newly created collection.

**Raises:**

- ValueError: If the collection already exists and get_or_create is False.
- ValueError: If the collection name is invalid.

### get_collection

Get a collection with the given name.

  The name of the collection to get

  Optional function to use to embed documents.
Uses the default embedding function if not provided.

  Optional function to use to load records (documents, images, etc.)

**Returns:** The collection

**Raises:**

- ValueError: If the collection does not exist

### get_or_create_collection

Get or create a collection with the given name and metadata.

Args:
    name: The name of the collection to get or create
    metadata: Optional metadata to associate with the collection. If
    the collection already exists, the metadata provided is ignored.
    If the collection does not exist, the new collection will be created
    with the provided metadata.
    embedding_function: Optional function to use to embed documents
    data_loader: Optional function to use to load records (documents, images, etc.)

Returns:
    The collection

Examples:
    ```python
    client.get_or_create_collection("my_collection")
    # collection(name="my_collection", metadata={})
    ```

### delete_collection

Delete a collection with the given name.

  The name of the collection to delete.

**Raises:**

- ValueError: If the collection does not exist.

### reset

Resets the database. This will delete all collections and entries.

**Returns:** True if the database was reset successfully.

### get_version

Get the version of Chroma.

**Returns:** The version of Chroma

### get_settings

Get the settings used to initialize.

**Returns:** The settings used to initialize.

### get_max_batch_size

Return the maximum number of records that can be created or mutated in a single call.

---

## Admin Client Methods

### create_tenant

Create a new tenant. Raises an error if the tenant already exists.

### get_tenant

Get a tenant. Raises an error if the tenant does not exist.

### create_database

Create a new database. Raises an error if the database already exists.

### get_database

Get a database. Raises an error if the database does not exist.

  The tenant of the database to get.

### delete_database

Delete a database. Raises an error if the database does not exist.

  The tenant of the database to delete.

### list_databases

List all databases for a tenant. Raises an error if the tenant does not exist.

  The tenant to list databases for.
