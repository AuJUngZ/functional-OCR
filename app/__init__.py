from flask import Flask
from app.config import Config
from app.utils.tesseract_utils import init_tesseract


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_tesseract()

    with app.app_context():
        # Register routes
        from app.routes import api
        app.register_blueprint(api)

    return app
