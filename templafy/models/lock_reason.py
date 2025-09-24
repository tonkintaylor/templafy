from enum import Enum


class LockReason(str, Enum):
    HARDDEPENDENCY = "hardDependency"
    RESTRICTEDACCESS = "restrictedAccess"

    def __str__(self) -> str:
        return str(self.value)
