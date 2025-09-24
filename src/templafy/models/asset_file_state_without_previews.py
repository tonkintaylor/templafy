from enum import Enum


class AssetFileStateWithoutPreviews(str, Enum):
    DELETING = "deleting"
    PROCESSING = "processing"
    PROCESSINGFAILED = "processingFailed"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
