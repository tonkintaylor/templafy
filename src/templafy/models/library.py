"""Library model for the Templafy API."""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class Library(BaseModel):
    """A Templafy library."""

    id: str
    name: str
    description: Optional[str] = None
    space_id: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    model_config = ConfigDict(extra="allow")