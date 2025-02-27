import os
from werkzeug.utils import secure_filename
from pymonad.either import Either, Right, Left

def save_image_either(file, upload_folder='./uploads') -> Either:
    """
    Save the uploaded file to the upload folder, returning an Either.
    """
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        
        file.save(filepath)
        return Right(filepath)
    except Exception as e:
        return Left(f"Error saving file: {str(e)}")

def cleanup_file_either(filepath: str) -> Either:
    """
    Delete the temporary file, returning an Either.
    """
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
        return Right(f'File {filepath} deleted')
    except Exception as e:
        return Left(f"Error cleaning up file: {str(e)}")
