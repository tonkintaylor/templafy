from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.not_found_problem_details import NotFoundProblemDetails
from ...models.update_color_theme_data_source_item_field_request import UpdateColorThemeDataSourceItemFieldRequest
from ...models.update_font_data_source_item_field_request import UpdateFontDataSourceItemFieldRequest
from ...models.update_image_data_source_item_field_request import UpdateImageDataSourceItemFieldRequest
from ...models.update_number_data_source_item_field_request import UpdateNumberDataSourceItemFieldRequest
from ...models.update_reference_data_source_item_field_request import UpdateReferenceDataSourceItemFieldRequest
from ...models.update_text_data_source_item_field_request import UpdateTextDataSourceItemFieldRequest
from ...models.validation_problem_details import ValidationProblemDetails
from ...types import Response


def _get_kwargs(
    data_source_id: int,
    item_id: int,
    field_id: int,
    *,
    body: Union[
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/data-sources/{data_source_id}/items/{item_id}/fields/{field_id}",
    }

    if isinstance(
        body,
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(
        body,
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(
        body,
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400

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
) -> Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: int,
    item_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ],
) -> Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]:
    """Updates a single field on a data source item.

    Args:
        data_source_id (int):
        item_id (int):
        field_id (int):
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        item_id=item_id,
        field_id=field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: int,
    item_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ],
) -> Optional[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]:
    """Updates a single field on a data source item.

    Args:
        data_source_id (int):
        item_id (int):
        field_id (int):
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        item_id=item_id,
        field_id=field_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_source_id: int,
    item_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ],
) -> Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]:
    """Updates a single field on a data source item.

    Args:
        data_source_id (int):
        item_id (int):
        field_id (int):
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        item_id=item_id,
        field_id=field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: int,
    item_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
        Union[
            "UpdateColorThemeDataSourceItemFieldRequest",
            "UpdateFontDataSourceItemFieldRequest",
            "UpdateImageDataSourceItemFieldRequest",
            "UpdateNumberDataSourceItemFieldRequest",
            "UpdateReferenceDataSourceItemFieldRequest",
            "UpdateTextDataSourceItemFieldRequest",
        ],
    ],
) -> Optional[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]:
    """Updates a single field on a data source item.

    Args:
        data_source_id (int):
        item_id (int):
        field_id (int):
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.
        body (Union['UpdateColorThemeDataSourceItemFieldRequest',
            'UpdateFontDataSourceItemFieldRequest', 'UpdateImageDataSourceItemFieldRequest',
            'UpdateNumberDataSourceItemFieldRequest', 'UpdateReferenceDataSourceItemFieldRequest',
            'UpdateTextDataSourceItemFieldRequest']):  Example: {'type': 'text', 'value': 'An updated
            value'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            item_id=item_id,
            field_id=field_id,
            client=client,
            body=body,
        )
    ).parsed
