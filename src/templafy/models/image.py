"""Image model for the Templafy API."""

from typing import Optional, List
from pydantic import BaseModel


class Image(BaseModel):
    """A Templafy image asset."""

    id: str
    name: str
    description: Optional[str] = None
    library_id: Optional[str] = None
    folder_id: Optional[str] = None
    tags: Optional[List[str]] = None
    file_size: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    format: Optional[str] = None
    download_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        """Pydantic configuration."""
        
        extra = "allow"