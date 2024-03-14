import requests
from ..config import BASE_URL, API_KEY, HeaderKey as HK, EnvVar


class BaseClient:
    """
    BaseClient
    ==========
    
    Base class for all JSONBin clients.
    """
    def __init__(self, api_key: str = API_KEY, base_url: str = BASE_URL) -> None:
        """
        Initialize the API client with the provided API key and base URL.
        
        Parameters:
            api_key (str): The API key to be used for authentication. Defaults to the value of API_KEY.
            base_url (str): The base URL of the API. Defaults to the value of BASE_URL.
        
        Returns:
            None
        """
        self.base_url = base_url.strip("/")
        self.api_key = api_key
        self.base_headers = {
            HK.CONTENT_TYPE: 'application/json',
            HK.API_KEY: self.api_key,
        }
    
    def request(self, url_path: str, method: str = 'GET', data: dict|list = None, headers: dict = None) -> dict|list:
        """
        A function to make an HTTP request to a specified URL with optional method, data, and headers.
        
        Parameters:
            url_path (str): The path of the URL to make the request to.
            method (str): The HTTP method to use for the request. Defaults to 'GET'.
            data (dict|list): The data to be sent with the request. Defaults to None.
            headers (dict): The headers to include in the request. Defaults to None.
        
        Returns:
            dict|list: The JSON response from the request.
        """
        url = f"{self.base_url}/{url_path}"
        headers = (headers or {}) | self.base_headers
        response = requests.request(method, url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Status Code: {response.status_code}. Response: {response.text}")
        