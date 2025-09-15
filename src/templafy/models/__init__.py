"""Models for the Templafy API."""

# For now use simple models without pydantic to avoid dependency issues during development
from .space_simple import Space

# Create simple placeholder classes for other models
class Document:
    """A Templafy document template."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Library:
    """A Templafy library."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Folder:
    """A Templafy folder."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Image:
    """A Templafy image asset."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Slide:
    """A Templafy slide template."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Spreadsheet:
    """A Templafy spreadsheet template."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

class Link:
    """A Templafy link asset."""
    
    def __init__(self, id: str, name: str, **kwargs):
        self.id = id
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

__all__ = [
    "Space",
    "Document", 
    "Library",
    "Folder",
    "Image",
    "Slide", 
    "Spreadsheet",
    "Link",
]