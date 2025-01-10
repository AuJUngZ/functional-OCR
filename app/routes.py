from flask import Blueprint, request, jsonify
from app.services.ocr_service import process_image

api = Blueprint('api', __name__)

@api.route('/ocr', methods=['POST'])
def ocr_api():
    """
    API endpoint for OCR processing.
    """
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    try:
        result = process_image(file)
        return jsonify({"text": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
