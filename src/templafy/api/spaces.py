"""Spaces API endpoints for the Templafy API."""

from typing import List, Optional, Union
import httpx

from ..client import Client, AuthenticatedClient
from ..models.space import Space
from ..errors import get_error_from_response
from ..types import Response


def get_spaces(
    *,
    client: Union[Client, AuthenticatedClient],
) -> List[Space]:
    """List all existing active spaces.
    
    Args:
        client: The API client to use
        
    Returns:
        List of spaces
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/spaces"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return [Space(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error


async def get_spaces_async(
    *,
    client: Union[Client, AuthenticatedClient],
) -> List[Space]:
    """List all existing active spaces (async version).
    
    Args:
        client: The API client to use
        
    Returns:
        List of spaces
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/spaces"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    async with httpx.AsyncClient() as async_client:
        response = await async_client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return [Space(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error