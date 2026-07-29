import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "diagram_ai_secret")

    UPLOAD_FOLDER = "uploads"

    GENERATED_FOLDER = "static/generated"

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    ALLOWED_EXTENSIONS = {
        "pdf",
        "docx",
        "txt",
        "pptx",
        "xlsx",
        "csv"
    }

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")