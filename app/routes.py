from flask import Blueprint, request, jsonify
from app.services.ocr_service import process_image

api = Blueprint('api', __name__)

@api.route('/ocr', methods=['POST'])
def ocr_api():
    """
    API endpoint for OCR processing using Either for error handling.
    """
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    result = process_image(file)
    if result.is_right():
        return jsonify({"text": result.value}), 200
    else:
        return jsonify({"error": str(result)}), 400
