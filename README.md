# JsonDBin: Unified Interface for JSON Database with jsonbin.io

JsonDBin is a Python package that offers a unified interface for leveraging [jsonbin.io](https://jsonbin.io) as a JSON database. It simplifies managing collections and documents within jsonbin.io, providing an easy-to-use API for CRUD operations.

## Features

- **Collection Management**: Create, retrieve, and update collections.
- **Document Management**: Perform CRUD operations on documents within collections.
- **Schema Support**: Attach and remove schemas from collections.
- **Batch Retrieval**: Retrieve documents in batches or all at once.
- **Error Handling**: Graceful handling of HTTP errors with informative exceptions.

## Installation

You can install JsonDBin using pip:

```bash
pip install jsondbin
```

## Getting Started

To start using JsonDBin, instantiate the `JsonDBin` class with your jsonbin.io API key:

```python
from jsondbin import JsonDBin

# Initialize JsonDBin with your API key
db = JsonDBin(api_key="YOUR_JSONBIN_API_KEY", collection_name="my_collection")
```

### Collection Management

```python
# Create a new collection
collection = db.create(name="my_collection")

# Retrieve all collections
collections = db.get_all()

# Rename an existing collection
collection = db.rename(new_name="new_name")
```

### Document Management

```python
# Create a new document in a collection
document = db.create_document(doc={"key": "value"})

# Retrieve a document by ID
document = db.get_document(doc_id="DOCUMENT_ID")

# Update an existing document
updated_document = db.update_document(doc_id="DOCUMENT_ID", doc={"key": "updated_value", "new_key": "new_value"})

# Delete a document by ID
db.delete_document(doc_id="DOCUMENT_ID")
```

### Batch Retrieval

```python
# Retrieve documents in batches of 10
for batch in db.get_pages():
    for document in batch:
        print(document)

# Retrieve all documents in a collection
all_documents = db.get_all_documents()
```

### Schema Management

```python
# Attach a schema document to the collection
schema = db.attach_schema(schema_doc_id="SCHEMA_DOCUMENT_ID")

# Remove the schema attached to the collection
db.remove_schema()
```

## Retrieving API Key

To retrieve your API key or X-Master-Key from JSONBin.io, follow these steps:

1. **Login or Signup to JSONBin.io:** Visit the [JSONBin.io](https://jsonbin.io) website and log in to your account using your preferred authentication method (Google, Twitter, Facebook, or GitHub).
2. **Navigate to Dashboard:** After logging in, navigate to the Dashboard by clicking on the "Dashboard" option in the navigation menu.
3. **Access API Keys Section:** In the Dashboard, locate the "API Keys" section. This section typically contains options related to managing API keys and access permissions.
4. **Retrieve X-Master-Key:** Your X-Master-Key is displayed in the API Keys section. It is a default key generated upon creating your JSONBin.io account. Copy the value of X-Master-Key for accessing API endpoints that require authentication.

   Note: Keep your API key secure and do not share it with unauthorized individuals. The X-Master-Key provides access to all API endpoints on JSONBin.io and should be handled with care.

If you have any issues retrieving your API key or need further assistance, you can reach out to JSONBin.io support for help.

---

JsonDBin is designed for experimental and educational purposes. It is not recommended for production use due to its limitations and the experimental nature of the jsonbin.io service.

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/subhayu99/jsondbin).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
