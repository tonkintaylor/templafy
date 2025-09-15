"""Common type definitions for the Templafy API client."""

from typing import Any, Dict, List, Literal, Optional, Union
from typing_extensions import TypeAlias

# Response types
Response: TypeAlias = Dict[str, Any]
ResponseList: TypeAlias = List[Dict[str, Any]]

# HTTP methods
HTTPMethod: TypeAlias = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]

# File types for upload/download
FileType: TypeAlias = Union[bytes, str]
FileDict: TypeAlias = Dict[str, Any]

# Common query parameters
QueryParams: TypeAlias = Optional[Dict[str, Union[str, int, bool, List[str]]]]

# Headers
Headers: TypeAlias = Dict[str, str]

# JSON data
JSONType: TypeAlias = Union[Dict[str, Any], List[Any], str, int, float, bool, None]