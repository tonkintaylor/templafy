"""Libraries API endpoints for the Templafy API."""

from typing import List, Union

from ..client import Client, AuthenticatedClient
from ..models.library import Library
from ..errors import get_error_from_response


def get_libraries(
    *,
    client: Union[Client, AuthenticatedClient],
) -> List[Library]:
    """List libraries.
    
    Args:
        client: The API client to use
        
    Returns:
        List of libraries
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/libraries"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return [Library(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error