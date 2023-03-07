import os
from .app_settings import INSTALLED_APPS

LOGIN_REDIRECT_URL = "profile_detail"

ADMIN_SITE_HEADER = os.getenv('ADMIN_SITE_HEADER')
ADMIN_SITE_TITLE = os.getenv('ADMIN_SITE_TITLE')
ADMIN_SITE_INDEX_TITLE = os.getenv('ADMIN_SITE_INDEX_TITLE')


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_API = True
USE_SITEMAPS = True
USE_ROBOTS = True

# Sites Framework
SITE_ID = 1
