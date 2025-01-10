import os
from app.types.config import Config

def get_default_config() -> Config:
    return {
        "UPLOAD_FOLDER": "uploads",
        "ALLOWED_EXTENSIONS": {"png", "jpg", "jpeg", "gif", "tiff", "bmp"},
        "MAX_CONTENT_LENGTH": 16 * 1024 * 1024,
        "TESSERACT_PATH": "C:/Program Files/Tesseract-OCR/tesseract.exe",
        "DEBUG": False
    }
