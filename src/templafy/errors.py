"""Error classes and exceptions for the Templafy API client."""

import httpx


class TemplafyError(Exception):
    """Base exception for Templafy API errors."""

    def __init__(self, message: str, response: httpx.Response | None = None) -> None:
        """Initialize the error.
        
        Args:
            message: Error message
            response: HTTP response that caused the error
        """
        super().__init__(message)
        self.message = message
        self.response = response


class AuthenticationError(TemplafyError):
    """Authentication failed."""



class AuthorizationError(TemplafyError):
    """Authorization failed - insufficient permissions."""



class NotFoundError(TemplafyError):
    """Resource not found."""



class ValidationError(TemplafyError):
    """Request validation failed."""



class RateLimitError(TemplafyError):
    """Rate limit exceeded."""



class ServerError(TemplafyError):
    """Server error (5xx status codes)."""



class UnexpectedStatus(TemplafyError):
    """Unexpected HTTP status code."""

    def __init__(
        self,
        status_code: int,
        content: bytes,
        response: httpx.Response | None = None,
    ) -> None:
        """Initialize unexpected status error.
        
        Args:
            status_code: HTTP status code
            content: Response content
            response: HTTP response
        """
        message = f"Unexpected status code: {status_code}"
        super().__init__(message, response)
        self.status_code = status_code
        self.content = content


def get_error_from_response(response: httpx.Response) -> TemplafyError:
    """Get appropriate error from HTTP response.
    
    Args:
        response: HTTP response
        
    Returns:
        Appropriate error instance
    """
    status_code = response.status_code
    content = response.content

    if status_code == 401:
        return AuthenticationError("Authentication failed", response)
    elif status_code == 403:
        return AuthorizationError("Authorization failed", response)
    elif status_code == 404:
        return NotFoundError("Resource not found", response)
    elif status_code == 422:
        return ValidationError("Request validation failed", response)
    elif status_code == 429:
        return RateLimitError("Rate limit exceeded", response)
    elif status_code >= 500:
        return ServerError(f"Server error: {status_code}", response)
    else:
        return UnexpectedStatus(status_code, content, response)
