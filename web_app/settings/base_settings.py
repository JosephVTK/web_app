from .operations import resolve

# Build paths inside the project like this: BASE_DIR / 'subdir'.

SECRET_KEY = resolve('SECRET_KEY', raise_error=True)
DEBUG = resolve('DEBUG', default=False, var_type=bool, raise_error=True)

ROOT_URLCONF = 'web_app.urls'
WSGI_APPLICATION = 'web_app.wsgi.application'