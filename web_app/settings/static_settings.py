import os
from .operations import BASE_DIR, resolve

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

FILE_ROOT = resolve('FILE_ROOT', default=BASE_DIR)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATIC_ROOT = os.path.join(FILE_ROOT, 'static-files/static/')
MEDIA_ROOT = os.path.join(FILE_ROOT, 'static-files/media/')

