"""Documents API endpoints for the Templafy API."""

from typing import List, Optional, Union
import httpx

from ..client import Client, AuthenticatedClient
from ..models.document import Document
from ..errors import get_error_from_response


def get_documents(
    *,
    client: Union[Client, AuthenticatedClient],
    library_id: Optional[str] = None,
    folder_id: Optional[str] = None,
) -> List[Document]:
    """List documents.
    
    Args:
        client: The API client to use
        library_id: Optional library ID to filter by
        folder_id: Optional folder ID to filter by
        
    Returns:
        List of documents
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/documents"
    
    params = {}
    if library_id:
        params["libraryId"] = library_id
    if folder_id:
        params["folderId"] = folder_id
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return [Document(**item) for item in data]
    else:
        error = get_error_from_response(response)
        raise error


def get_document(
    *,
    client: Union[Client, AuthenticatedClient],
    document_id: str,
) -> Document:
    """Get a specific document.
    
    Args:
        client: The API client to use
        document_id: The ID of the document
        
    Returns:
        The document
        
    Raises:
        TemplafyError: If the API request fails
    """
    url = f"{client.base_url}/documents/{document_id}"
    
    headers = {}
    if isinstance(client, AuthenticatedClient):
        headers = client.get_headers()
    
    response = client._client.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return Document(**data)
    else:
        error = get_error_from_response(response)
        raise error