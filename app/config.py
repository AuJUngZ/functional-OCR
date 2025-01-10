import os

class Config:
    UPLOAD_FOLDER = './uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
