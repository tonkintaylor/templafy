from enum import Enum


class SourceEntityType(str, Enum):
    DATASOURCE = "dataSource"
    DATASOURCEITEM = "dataSourceItem"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
