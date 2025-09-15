"""Spreadsheet model for the Templafy API."""

from typing import Optional, List
from pydantic import BaseModel


class Spreadsheet(BaseModel):
    """A Templafy spreadsheet template."""

    id: str
    name: str
    description: Optional[str] = None
    library_id: Optional[str] = None
    folder_id: Optional[str] = None
    tags: Optional[List[str]] = None
    file_size: Optional[int] = None
    download_url: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        """Pydantic configuration."""
        
        extra = "allow"