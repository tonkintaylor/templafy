"""Document model for the Templafy API."""

from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class Document(BaseModel):
    """A Templafy document template."""

    id: str
    name: str
    description: Optional[str] = None
    template_type: Optional[str] = None
    library_id: Optional[str] = None
    folder_id: Optional[str] = None
    tags: Optional[List[str]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[int] = None
    download_url: Optional[str] = None

    model_config = ConfigDict(extra="allow")