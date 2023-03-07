from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

if not os.getenv('LOAD_ENV', 'False') == "True":
    print("Please create .env file first.")
    raise FileNotFoundError('No .env file found.')

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == "True"
ROOT_URLCONF = 'web_app.urls'
WSGI_APPLICATION = 'web_app.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'