"""A Python client for the Templafy API."""

# Trigger CI/CD to verify fixes

from typing import Any

__version__ = "0.1.0"

# Type stubs for lazy-loaded items to satisfy pyright
# These will be overridden by __getattr__ at runtime
if False:  # pragma: no cover
    from .client import AuthenticatedClient, Client
    from .errors import (
        AuthenticationError,
        AuthorizationError,
        NotFoundError,
        RateLimitError,
        ServerError,
        TemplafyError,
        UnexpectedStatus,
        ValidationError,
    )
    from . import api

# For now, defer imports that have external dependencies to avoid issues
# during development where dependencies may not be installed
def __getattr__(name: str) -> Any:  # noqa: PLC0415
    """Lazy imports for components with external dependencies."""
    if name == "Client":
        from .client import Client  # noqa: PLC0415
        return Client
    elif name == "AuthenticatedClient":
        from .client import AuthenticatedClient  # noqa: PLC0415
        return AuthenticatedClient
    elif name == "api":
        from . import api  # noqa: PLC0415
        return api
    elif name in ["TemplafyError", "AuthenticationError", "AuthorizationError",
                  "NotFoundError", "ValidationError", "RateLimitError",
                  "ServerError", "UnexpectedStatus"]:
        from .errors import (  # noqa: PLC0415
            AuthenticationError,  # noqa: F401
            AuthorizationError,  # noqa: F401
            NotFoundError,  # noqa: F401
            RateLimitError,  # noqa: F401
            ServerError,  # noqa: F401
            TemplafyError,  # noqa: F401
            UnexpectedStatus,  # noqa: F401
            ValidationError,  # noqa: F401
        )
        return locals()[name]
    else:
        error_message = f"module '{__name__}' has no attribute '{name}'"
        raise AttributeError(error_message)

# Export models (these have no external dependencies)
from .models import (  # noqa: E402
    Document,
    Folder,
    Image,
    Library,
    Link,
    Slide,
    Space,
    Spreadsheet,
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
