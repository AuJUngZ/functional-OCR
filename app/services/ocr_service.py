from app.utils.file_utils import save_image, cleanup_file
import pytesseract
from PIL import Image

def perform_ocr(image_path: str) -> str:
    """
    Perform OCR on the given image and return extracted text.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def process_image(file) -> str:
    """
    Process the uploaded image, perform OCR, and cleanup.
    """
    image_path = save_image(file)
    try:
        text = perform_ocr(image_path)
        return text
    finally:
        cleanup_file(image_path)
