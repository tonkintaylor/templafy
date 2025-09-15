"""A Python client for the Templafy API."""

__version__ = "0.1.0"

# For now, defer imports that have external dependencies to avoid issues
# during development where dependencies may not be installed
def __getattr__(name: str):
    """Lazy imports for components with external dependencies."""
    if name == "Client":
        from .client import Client
        return Client
    elif name == "AuthenticatedClient":
        from .client import AuthenticatedClient
        return AuthenticatedClient
    elif name == "api":
        from . import api
        return api
    elif name in ["TemplafyError", "AuthenticationError", "AuthorizationError", 
                  "NotFoundError", "ValidationError", "RateLimitError", 
                  "ServerError", "UnexpectedStatus"]:
        from .errors import (
            TemplafyError, AuthenticationError, AuthorizationError,
            NotFoundError, ValidationError, RateLimitError,
            ServerError, UnexpectedStatus
        )
        return locals()[name]
    else:
        error_message = f"module '{__name__}' has no attribute '{name}'"
        raise AttributeError(error_message)

# Export models (these have no external dependencies)
from .models import (
    Space,
    Document,
    Library,
    Folder,
    Image,
    Slide,
    Spreadsheet,
    Link,
)

__all__ = [
    # Client classes
    "Client",
    "AuthenticatedClient",
    # Models
    "Space",
    "Document",
    "Library",
    "Folder",
    "Image",
    "Slide",
    "Spreadsheet",
    "Link",
    # Errors
    "TemplafyError",
    "AuthenticationError",
    "AuthorizationError",
    "NotFoundError",
    "ValidationError",
    "RateLimitError",
    "ServerError",
    "UnexpectedStatus",
    # API modules
    "api",
]
