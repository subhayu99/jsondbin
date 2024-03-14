import os
from enum import Enum

class EnvVar:
    API_KEY = "JSONBIN_API_KEY"
    BASE_URL = "JSONBIN_BASE_URL"

BASE_URL = os.getenv(EnvVar.BASE_URL, "https://api.jsonbin.io/v3")
BASE_URL = BASE_URL.strip("/")

API_KEY = os.getenv(EnvVar.API_KEY)
# if not API_KEY:
#     raise RuntimeError("'JSONBIN_API_KEY' environment variable is not set")

class HeaderKey(str, Enum):
    API_KEY = "X-Master-Key"
    
    COLLECTION_ID = "X-Collection-Id"
    COLLECTION_NAME = "X-Collection-Name"
    COLLECTION_SORT_ORDER = "X-Sort-Order"
    
    SCHEMA_DOC_ID = "X-Schema-Doc-Id"
    
    DOC_PRIVATE = "X-Bin-Private"
    DOC_NAME = "X-Bin-Name"
    DOC_VERSIONING = "X-Bin-Versioning"
    DOC_JSON_PATH = "X-JSON-Path"
    DOC_METADATA = "X-Bin-Meta"

    CONTENT_TYPE = "Content-Type"