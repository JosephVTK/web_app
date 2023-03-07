from .base_settings import BASE_DIR, SECRET_KEY, DEBUG, ROOT_URLCONF, WSGI_APPLICATION, DEFAULT_AUTO_FIELD
from .host_settings import ALLOWED_HOSTS, INTERNAL_IPS
from .app_settings import *

from .middleware_settings import MIDDLEWARE
from .template_settings import TEMPLATES
from .database_settings import DATABASES
from .validation_settings import AUTH_PASSWORD_VALIDATORS
from .static_settings import STATIC_ROOT, STATIC_URL, STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL
from .email_settings import EMAIL_BACKEND, EMAIL_FILE_PATH

from .config import *