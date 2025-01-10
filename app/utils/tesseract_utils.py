import pytesseract
from pathlib import Path
from app.config import get_default_config

def init_tesseract():
    try:
        config = get_default_config()
        tesseract_path = str(Path(config['TESSERACT_PATH']))
        pytesseract.pytesseract.tesseract_cmd = tesseract_path
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Tesseract: {str(e)}")