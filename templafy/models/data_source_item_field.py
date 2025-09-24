from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="DataSourceItemField")


@_attrs_define
class DataSourceItemField:
    """
    Attributes:
        type_ (Union[None, str]): Data source item field type.
        data_source_field_id (Union[Unset, int]): Unique data source field identifier.
    """

    type_: Union[None, str]
    data_source_field_id: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: Union[None, str]
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if data_source_field_id is not UNSET:
            field_dict["dataSourceFieldId"] = data_source_field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        type_ = _parse_type_(d.pop("type"))

        data_source_field_id = d.pop("dataSourceFieldId", UNSET)

        data_source_item_field = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
        )

        return data_source_item_field
