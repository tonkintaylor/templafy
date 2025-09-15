"""Images API endpoints for the Templafy API."""

from typing import List, Union

from ..client import Client, AuthenticatedClient
from ..models.image import Image
from ..errors import get_error_from_response


def get_images(
    *,
    client: Union[Client, AuthenticatedClient],
) -> List[Image]:
    """List images.
    
    Args:
        client: The API client to use
        
    Returns:
        List of images
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/images"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return [Image(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error