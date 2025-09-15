"""Space model for the Templafy API."""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class Space(BaseModel):
    """A Templafy space (workspace/tenant)."""

    id: str
    name: str
    description: Optional[str] = None
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    model_config = ConfigDict(extra="allow")