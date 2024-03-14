from .base import BaseClient
from ..config import API_KEY, BASE_URL, HeaderKey as HK
from ..models.document import Document


class DocumentClient(BaseClient):
    """
    DocumentClient
    ==============
    
    Class for managing documents in JSONBin.
    """
    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL):
        super().__init__(api_key=api_key, base_url=base_url)

    def create(
        self,
        doc: dict,
        collection_id: str = None,
        name: str = None,
        private: bool = True,
    ):
        """
        Creates a document with the given parameters.

        Parameters:
            doc (dict): The document to be created.
            collection_id (str, optional): The ID of the collection where the document will be created. Defaults to None.
            name (str, optional): The name of the document. Defaults to None.
            private (bool, optional): Whether the document is private or not. Defaults to True.

        Returns:
            Document: The created document.
        """
        headers = {HK.DOC_PRIVATE: ("false", "true")[private]}
        if name:
            headers[HK.DOC_NAME] = name
        if collection_id:
            headers[HK.COLLECTION_ID] = collection_id
        resp = self.request(f"b", "POST", data=doc, headers=headers)
        return Document(**resp)

    def update(self, doc_id: str, doc: dict, add_version: bool = True):
        """
        Update a document with the given ID using the provided data.

        Parameters:
            doc_id (str): The ID of the document to be updated.
            doc (dict): The updated data for the document.
            add_version (bool, optional): Whether to add a version to the document. Defaults to True.

        Returns:
            Document: The updated document.
        """
        headers = {HK.DOC_VERSIONING: ("false", "true")[add_version]}
        resp = self.request(f"b/{doc_id}", "PUT", data=doc, headers=headers)
        return Document(**resp)

    def get(self, doc_id: str, json_path: str = None, version: str = "latest"):
        """
        Retrieve a document by its ID and return a Document object.

        Parameters:
            doc_id (str): The ID of the document to retrieve.
            json_path (str, optional): The JSON path to retrieve a specific part of the document. Defaults to None.
            version (str, optional): The version of the document to retrieve. Defaults to "latest".

        Returns:
            Document: The retrieved Document object.
        """
        headers = {HK.DOC_METADATA: "true"}
        if json_path:
            headers[HK.DOC_JSON_PATH] = json_path
        resp = self.request(f"b/{doc_id}/{version}", headers=headers)
        return Document(**resp)

    def delete(self, doc_id: str):
        """
        Deletes a document with the given ID.

        Parameters:
            doc_id (str): The ID of the document to be deleted.
        """
        self.request(f"b/{doc_id}", "DELETE")
