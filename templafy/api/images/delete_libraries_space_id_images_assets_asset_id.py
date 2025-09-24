from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.not_found_problem_details import NotFoundProblemDetails
from ...types import Response


def _get_kwargs(
    space_id: int,
    asset_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/libraries/{space_id}/images/assets/{asset_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NotFoundProblemDetails]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = NotFoundProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NotFoundProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, NotFoundProblemDetails]]:
    """Deletes the image by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, NotFoundProblemDetails]]:
    """Deletes the image by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails]
    """

    return sync_detailed(
        space_id=space_id,
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, NotFoundProblemDetails]]:
    """Deletes the image by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, NotFoundProblemDetails]]:
    """Deletes the image by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
