"""Folder model for the Templafy API."""

from typing import Optional
from pydantic import BaseModel


class Folder(BaseModel):
    """A Templafy folder."""

    id: str
    name: str
    parent_id: Optional[str] = None
    library_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        """Pydantic configuration."""
        
        extra = "allow"