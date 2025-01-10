import os
from pymonad.either import Either, Left, Right
from app.config import get_default_config

def get_upload_path() -> Either:
    """Get upload folder path from config."""
    config = get_default_config()
    return Right(config['UPLOAD_FOLDER']) if 'UPLOAD_FOLDER' in config else Left('UPLOAD_FOLDER not found in config')

def ensure_folder_exists(folder_path: str) -> Either:
    """Create folder if it doesn't exist."""
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return Right(folder_path)
    except Exception as e:
        return Left(f"Failed to create folder: {str(e)}")

def validate_folder(folder_path: str) -> Either:
    """Validate folder exists."""
    return Right(folder_path) if os.path.exists(folder_path) else Left(f"Folder {folder_path} does not exist")

def folder_init() -> None:
    """Initialize upload folder using monadic composition."""
    result = (get_upload_path()
             .then(ensure_folder_exists)
             .then(validate_folder))

    if result.is_left():
        raise RuntimeError(result)