"""Simple space model for the Templafy API (no external dependencies)."""

from typing import Optional


class Space:
    """A Templafy space (workspace/tenant)."""

    def __init__(
        self,
        id: str,
        name: str,
        description: Optional[str] = None,
        is_active: bool = True,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        **kwargs
    ) -> None:
        """Initialize a Space.
        
        Args:
            id: Space ID
            name: Space name
            description: Space description
            is_active: Whether the space is active
            created_at: Creation timestamp
            updated_at: Update timestamp
            **kwargs: Additional fields
        """
        self.id = id
        self.name = name
        self.description = description
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        
        # Store additional fields
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self) -> str:
        """Return string representation."""
        return f"Space(id='{self.id}', name='{self.name}')"