"""Slide model for the Templafy API."""

from typing import Optional, List
from pydantic import BaseModel


class Slide(BaseModel):
    """A Templafy slide template."""

    id: str
    name: str
    description: Optional[str] = None
    library_id: Optional[str] = None
    folder_id: Optional[str] = None
    tags: Optional[List[str]] = None
    slide_number: Optional[int] = None
    layout_name: Optional[str] = None
    thumbnail_url: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        """Pydantic configuration."""
        
        extra = "allow"