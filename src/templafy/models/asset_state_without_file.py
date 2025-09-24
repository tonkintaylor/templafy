from enum import Enum


class AssetStateWithoutFile(str, Enum):
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
