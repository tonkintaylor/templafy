from enum import Enum


class LibraryType(str, Enum):
    DOCUMENTS = "documents"
    EMAIL_ELEMENTS = "email-elements"
    IMAGES = "images"
    LINKS = "links"
    PDFS = "pdfs"
    PRESENTATIONS = "presentations"
    SLIDES = "slides"
    SLIDE_ELEMENTS = "slide-elements"
    SPREADSHEETS = "spreadsheets"
    TEXT_ELEMENTS = "text-elements"

    def __str__(self) -> str:
        return str(self.value)
