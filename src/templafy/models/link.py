"""Link model for the Templafy API."""

from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class Link(BaseModel):
    """A Templafy link asset."""

    id: str
    name: str
    description: Optional[str] = None
    url: str
    library_id: Optional[str] = None
    folder_id: Optional[str] = None
    tags: Optional[List[str]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    model_config = ConfigDict(extra="allow")