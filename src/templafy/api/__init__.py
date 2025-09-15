"""API endpoint modules for the Templafy API."""

# Re-export all API modules for easy importing
from . import spaces
from . import documents
from . import libraries
from . import folders
from . import images
from . import slides
from . import spreadsheets
from . import links

__all__ = [
    "spaces",
    "documents",
    "libraries", 
    "folders",
    "images",
    "slides",
    "spreadsheets",
    "links",
]