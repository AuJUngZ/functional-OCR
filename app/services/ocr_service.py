from app.utils.file_utils import cleanup_file_either, save_image_either
import pytesseract
from PIL import Image
from pymonad.either import Either, Left, Right

def perform_ocr_either(image_path: str) -> Either:
    """
    Perform OCR on the given image and return the cleaned text wrapped in an Either.
    The returned text is sanitized and formatted for display in an HTML tag.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='tha+eng', config='--psm 6')
        
        return Right(text)
    except Exception as e:
        return Left(f"Error performing OCR: {str(e)}")


def process_image(file) -> Either:
    """
    Process the uploaded image, perform OCR, and cleanup using Either.
    """
    def ocr_and_cleanup(image_path: str) -> Either:
        ocr_result = perform_ocr_either(image_path)
        cleanup_file_either(image_path)
        return ocr_result
        
    return save_image_either(file).bind(ocr_and_cleanup)
