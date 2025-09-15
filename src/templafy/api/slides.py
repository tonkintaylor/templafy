"""Slides API endpoints for the Templafy API."""

from typing import List, Union

from ..client import Client, AuthenticatedClient
from ..models.slide import Slide
from ..errors import get_error_from_response


def get_slides(
    *,
    client: Union[Client, AuthenticatedClient],
) -> List[Slide]:
    """List slides.
    
    Args:
        client: The API client to use
        
    Returns:
        List of slides
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/slides"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return [Slide(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error