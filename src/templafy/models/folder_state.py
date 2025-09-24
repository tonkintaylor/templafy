from enum import Enum


class FolderState(str, Enum):
    DELETING = "deleting"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
