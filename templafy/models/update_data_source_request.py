from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="UpdateDataSourceRequest")


@_attrs_define
class UpdateDataSourceRequest:
    """
    Example:
        {'description': 'This is an updated description'}

    Attributes:
        description (Union[None, Unset, str]): Data source description. If null, description will be removed.
    """

    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        update_data_source_request = cls(
            description=description,
        )

        return update_data_source_request
