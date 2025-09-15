"""Folders API endpoints for the Templafy API."""

from typing import List, Union

from ..client import Client, AuthenticatedClient
from ..models.folder import Folder
from ..errors import get_error_from_response


def get_folders(
    *,
    client: Union[Client, AuthenticatedClient],
) -> List[Folder]:
    """List folders.
    
    Args:
        client: The API client to use
        
    Returns:
        List of folders
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/folders"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return [Folder(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error