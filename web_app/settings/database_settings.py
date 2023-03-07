import os
from .base_settings import BASE_DIR

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration Settings
USING_DB = os.getenv('USING_DB', 'sqlite')

def get_value(value):
	if not value:
		return value
	if value[0] != '^':
		return value
	value = value[1:]
	
	if value.lower() == 'true':
		return True
	if value.lower() == 'false':
		return False
	if value.isdigit():
		return int(value)

DATABASE_OPTIONS = { 
    key_value_pair.split(':')[0] : get_value(key_value_pair.split(':')[1]) 
    for key_value_pair 
    in os.getenv('DATABASE_OPTIONS', "").split(',')
    if key_value_pair.find(':') != -1
    }

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT', '')

if USING_DB == 'sqlite':
    DATABASE_ENGINE = os.getenv('DATABASE_ENGINE', 'django.db.backends.sqlite3')
    DATABASE_NAME = os.getenv('DATABASE_NAME', BASE_DIR / 'db.sqlite3')
else:
    if USING_DB == 'mysql':
        DATABASE_ENGINE = os.getenv('DATABASE_ENGINE', 'django.db.backends.mysql')
    elif USING_DB == 'postgres':
        DATABASE_ENGINE = os.getenv('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2')

# Safety Checks
if not DATABASE_ENGINE:
    raise LookupError(f"No DATABASE_ENGINE detected. Running {USING_DB}.")
if not DATABASE_NAME:
    raise LookupError(f"No DATABASE_NAME detected. Running {USING_DB}.")

if USING_DB != 'sqlite':
    if not DATABASE_USER:
        raise LookupError(f"No DATABASE_USER detected. Running {USING_DB}.")
    if not DATABASE_PASSWORD:
        raise LookupError(f"No DATABASE_PASSWORD detected. Running {USING_DB}.")
    if not DATABASE_HOST:
        raise LookupError(f"No DATABASE_HOST detected. Running {USING_DB}.")

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'OPTIONS': DATABASE_OPTIONS,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
    }
}