import os
from werkzeug.utils import secure_filename

def save_image(file, upload_folder='./uploads') -> str:
    """
    Save the uploaded file to the upload folder.
    """
    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return filepath

def cleanup_file(filepath: str) -> None:
    """
    Delete the temporary file.
    """
    if os.path.exists(filepath):
        os.remove(filepath)
