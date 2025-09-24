from enum import Enum


class AssetFileStateWithPreviews(str, Enum):
    DELETING = "deleting"
    GENERATINGPREVIEWS = "generatingPreviews"
    GENERATINGPREVIEWSFAILED = "generatingPreviewsFailed"
    PROCESSING = "processing"
    PROCESSINGFAILED = "processingFailed"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
