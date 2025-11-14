import os

# Base directory for relative paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key")
    
    # Database URL (fallback to SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "agrifarma.db")
    )
    
    # SQLAlchemy settings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload folder for product and post images
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
