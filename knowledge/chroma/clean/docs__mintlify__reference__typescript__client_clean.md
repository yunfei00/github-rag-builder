---
source: chroma
owner: chroma-core
repo: chroma
path: docs/mintlify/reference/typescript/client.mdx
url: https://github.com/chroma-core/chroma/blob/main/docs/mintlify/reference/typescript/client.mdx
---
---
title: "Client"
---

## Clients

### ChromaClient

Main client class for interacting with ChromaDB.
Provides methods for managing collections and performing operations on them.

  The host address of the Chroma server. Defaults to 'localhost'

  The port number of the Chroma server. Defaults to 8000

  Whether to use SSL/HTTPS for connections. Defaults to false

  The tenant name in the Chroma server to connect to

  The database name to connect to

 | undefined">
  Additional HTTP headers to send with requests

  Additional fetch options for HTTP requests

 | undefined" />

### CloudClient

ChromaDB cloud client for connecting to hosted Chroma instances.
Extends ChromaClient with cloud-specific authentication and configuration.

### AdminClient

Administrative client for managing ChromaDB tenants and databases.
Provides methods for creating, deleting, and listing tenants and databases.

  The host address of the Chroma server

  The port number of the Chroma server

  Whether to use SSL/HTTPS for connections

 | undefined">
  Additional HTTP headers to send with requests

  Additional fetch options for HTTP requests

---

## Client Methods

### heartbeat

Sends a heartbeat request to check server connectivity.

**Returns:** Promise resolving to the server's nanosecond heartbeat timestamp

### listCollections

Lists all collections in the current database.

**Returns:** Promise resolving to an array of Collection instances

### countCollections

Gets the total number of collections in the current database.

**Returns:** Promise resolving to the collection count

### createCollection

Creates a new collection with the specified configuration.

**Returns:** Promise resolving to the created Collection instance

### getCollection

Retrieves an existing collection by name.

**Returns:** Promise resolving to the Collection instance

### getOrCreateCollection

Gets an existing collection or creates it if it doesn't exist.

**Returns:** Promise resolving to the Collection instance

### deleteCollection

Deletes a collection and all its data.

### reset

Resets the entire database, deleting all collections and data.

**Returns:** Promise that resolves when the reset is complete

### version

Gets the version of the Chroma server.

**Returns:** Promise resolving to the server version string

---

## Admin Client Methods

### createTenant

Creates a new tenant.

### getTenant

Retrieves information about a specific tenant.

**Returns:** Promise resolving to the tenant name

### createDatabase

Creates a new database within a tenant.

### getDatabase

Retrieves information about a specific database.

**Returns:** Promise resolving to database information

### deleteDatabase

Deletes a database and all its data.

### listDatabases

Lists all databases within a tenant.

  Listing parameters including tenant and pagination

**Returns:** Promise resolving to an array of database information
