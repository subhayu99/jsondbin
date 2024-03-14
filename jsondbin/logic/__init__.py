from ..config import API_KEY, BASE_URL
from .document import DocumentClient
from .collection import CollectionClient


class JsonDBin(CollectionClient):
    """
    JsonDBin
    ========
    
    An unified interface for using [jsonbin.io](https://jsonbin.io) as a JSON database.
    
    Note:
        This project is just a fun weekend project and not for production use.
    """
    def __init__(
        self,
        api_key: str = API_KEY,
        collection_name: str = None,
        auto_create: bool = False,
        base_url: str = BASE_URL,
    ):
        """
        Initialize the JsonDBin with the provided API key, collection name, auto_create flag, and base URL.

        Parameters:
            api_key (str): The API key to authenticate requests.
            collection_name (str): The name of the collection to work with. If None, all the documents will set to `"uncategorized"` collection.
            auto_create (bool): Flag indicating whether to automatically create the collection if it does not exist.
            base_url (str): The base URL for API requests.

        Returns:
            None
        """
        super().__init__(
            api_key=api_key,
            base_url=base_url,
            collection_name=collection_name,
            auto_create=auto_create,
        )


__all__ = [
    "JsonDBin",
    "CollectionClient",
    "DocumentClient",
]
