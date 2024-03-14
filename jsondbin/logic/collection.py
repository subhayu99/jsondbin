from functools import lru_cache
from itertools import chain

from .base import BaseClient, API_KEY, BASE_URL
from .document import DocumentClient
from ..config import HeaderKey as HK
from ..models.document import DocumentOfList
from ..models.collection import Collection, CollectionCreated, CollectionSchema


class CollectionClient(BaseClient):
    """
    CollectionClient
    ================
    
    Class to manage collections in JSONBin.
    """
    def __init__(
        self,
        api_key: str = API_KEY,
        base_url: str = BASE_URL,
        collection_name: str | None = None,
        auto_create: bool = False,
    ):
        """
        Initialize the class with the provided collection name and auto-create option.

        Parameters:
            api_key (str): API key for the JSONBin account
            base_url (str): Base URL for the JSONBin API
            collection_name (str | None): Name of the collection. `None` if not passed
            auto_create (bool): Flag to automatically create collection if not found

        Returns:
            None
        """
        super().__init__(api_key=api_key, base_url=base_url)
        self.collection_name = collection_name
        """Name of the collection. `None` if not passed"""
        self.collection_id = self.get_collection_id()
        """ID of the collection. `None` if not found"""
        if collection_name is not None and not self.collection_id and auto_create:
            self.collection_id = self.create(self.collection_name).record
        self.document = DocumentClient(api_key=api_key, base_url=base_url)
        """DocumentClient instance. Used to manage documents in the collection"""

    @lru_cache
    def get_collection_id(self):
        """Cached method to get the collection ID"""
        _id = ([x.id for x in self.get_all() if x.name == self.collection_name] or [None])[0]
        return _id

    def get_all(self):
        """Get all collections"""
        collections = self.request("c")
        return [Collection(**x) for x in collections]

    def create(self, name: str):
        """
        Create a new collection with the given name.

        Parameters:
            name (str): The name of the collection.

        Returns:
            Collection: The newly created collection.
        """
        resp = self.request("c", "POST", headers={HK.COLLECTION_NAME: name})
        return Collection.from_created(CollectionCreated(**resp))

    def rename(self, new_name: str):
        """
        Renames a collection with the given ID to the specified name.

        Parameters:
            new_name (str): The new name for the collection.

        Returns:
            Collection: The updated collection.
        """
        if self.collection_id is None:
            raise Exception("You need to create a collection before renaming it")
        resp = self.request(
            f"c/{self.collection_id}/meta/name", "PUT", headers={HK.COLLECTION_NAME: new_name}
        )
        resp = Collection.from_created(CollectionCreated(**resp))
        self.collection_name = resp.name
        return resp
    
    def create_document(self, doc: dict, name: str = None, private: bool = True):
        """
        Create a document using the provided dictionary data.

        Parameters:
            doc (dict): The dictionary data for the document.
            name (str): The name of the document (default is None).
            private (bool): A flag indicating if the document is private (default is True).

        Returns:
            Document: The created document.
        """
        return self.document.create(doc, collection_id=self.collection_id, name=name, private=private)
    
    def update_document(self, doc_id: str, doc: dict, add_version: bool = True):
        """
        Update a document with the given ID using the provided dictionary.
        
        Parameters:
            doc_id (str): The ID of the document to update.
            doc (dict): The dictionary containing the updated document data.
            add_version (bool, optional): Flag indicating whether to add this for versioning. Defaults to True.
        
        Returns:
            Document: The updated document.
        """
        return self.document.update(doc_id, doc, add_version=add_version)
    
    def get_document(self, doc_id: str, json_path: str = None, version: str = "latest"):
        """
        Retrieves a document based on the provided document ID, optional JSON path, and version.

        Parameters:
            doc_id (str): The ID of the document to retrieve.
            json_path (str, optional): The optional JSON path within the document. Defaults to None.
            version (str): The version of the document to retrieve. Defaults to "latest".

        Returns:
            Document: The retrieved document based on the parameters.
        """
        return self.document.get(doc_id, json_path=json_path, version=version)

    def get_documents(
        self,
        last_doc_id: str = None,
        descending: bool = True,
    ):
        """
        Get a list of `10` documents from the specified collection.

        Parameters:
            last_doc_id (str): The last document ID to start retrieving documents from.
            descending (bool): Flag to determine the order of documents retrieval.

        Returns:
            generator[Document]: A generator that yields individual documents retrieved.
        """
        collection_id = self.collection_id if self.collection_id else "uncategorized"
        url_path = f"c/{collection_id}/bins"
        if last_doc_id:
            url_path += f"/{last_doc_id}"
        headers = {HK.COLLECTION_SORT_ORDER: ("ascending", "descending")[descending]}
        resp = self.request(url_path, headers=headers)
        return (self.document.get(DocumentOfList(**x).id) for x in resp)

    def get_pages(self, descending: bool = True):
        """
        Generate the pages of documents received from the source.

        Parameters:
            descending (bool): A flag to indicate whether to retrieve documents in descending order.
        
        Yields:
            list[Document]: A list of documents received in batches of 10.
        """
        docs_received = [None] * 10
        all_docs = []
        last_doc_id = None
        
        while len(docs_received) == 10:
            docs_received = list(self.get_documents(
                last_doc_id=last_doc_id, descending=descending,
            ))
            last_doc_id = docs_received[-1].id
            all_docs.extend(docs_received)
            yield docs_received
            
    def get_all_documents(self, descending: bool = True):
        """
        Get all documents using the specified order and return them as a list.
        
        Parameters:
            descending (bool): A flag to specify the order of documents.
        
        Returns:
            list[Document]: A list of all documents.
        """
        return list(chain(*self.get_pages(descending=descending)))
    
    def delete_document(self, doc_id: str):
        """
        Deletes the document with the given doc_id.

        Parameters:
            doc_id (str): The ID of the document to be deleted.

        Returns:
            None
        """
        self.document.delete(doc_id)

    def add_schema(self, schema_doc_id: str):
        """
        Adds a schema to the collection.

        Args:
            schema_doc_id (str): The ID of the schema document to add.

        Returns:
            CollectionSchema: The added collection schema.
            
        Raises:
            Exception: If the collection is not created yet.
        """
        if self.collection_id is None:
            raise Exception("You need to create a collection before adding a schema")
        resp = self.request(
            f"c/{self.collection_id}/schemadoc/add",
            "PUT",
            headers={HK.SCHEMA_DOC_ID: schema_doc_id},
        )
        return CollectionSchema(**resp)

    def remove_schema(self):
        """
        Removes attached schema from the collection. 
        
        Returns:
            CollectionSchema: A CollectionSchema object.
        
        Raises:
            Exception: If the collection is not created yet.
        """
        if self.collection_id is None:
            raise Exception("You need to create a collection before removing a schema")
        resp = self.request(
            f"c/{self.collection_id}/schemadoc/remove",
            "PUT",
        )
        return CollectionSchema(**resp)
