from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="UpdateFolderRequest")


@_attrs_define
class UpdateFolderRequest:
    """The request model to update the folder

    Attributes:
        name (Union[None, Unset, str]): Display name
        parent_folder_id (Union[None, Unset, int]): The identifier of a folder that current folder should be moved to
    """

    name: Union[None, Unset, str] = UNSET
    parent_folder_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_folder_id: Union[None, Unset, int]
        if isinstance(self.parent_folder_id, Unset):
            parent_folder_id = UNSET
        else:
            parent_folder_id = self.parent_folder_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if parent_folder_id is not UNSET:
            field_dict["parentFolderId"] = parent_folder_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_parent_folder_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_folder_id = _parse_parent_folder_id(d.pop("parentFolderId", UNSET))

        update_folder_request = cls(
            name=name,
            parent_folder_id=parent_folder_id,
        )

        return update_folder_request
