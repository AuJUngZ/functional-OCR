from typing import TypedDict, Set

class Config(TypedDict):
    UPLOAD_FOLDER: str
    ALLOWED_EXTENSIONS: Set[str]
    MAX_CONTENT_LENGTH: int
    TESSERACT_PATH: str
    DEBUG: bool