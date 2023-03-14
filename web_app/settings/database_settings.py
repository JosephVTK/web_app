from .operations import BASE_DIR, resolve

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration Settings
USING_DB = resolve('USING_DB', default='sqlite')

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
    for key_value_pair in resolve('DATABASE_OPTIONS', default="", var_type=list)
    if key_value_pair.find(':') != -1
    }

DATABASE_NAME = resolve('DATABASE_NAME')
DATABASE_USER = resolve('DATABASE_USER')
DATABASE_PASSWORD = resolve('DATABASE_PASSWORD')
DATABASE_HOST = resolve('DATABASE_HOST')
DATABASE_PORT = resolve('DATABASE_PORT', '')

if USING_DB == 'sqlite':
    DATABASE_ENGINE = resolve('DATABASE_ENGINE', default='django.db.backends.sqlite3')
    DATABASE_NAME = resolve('DATABASE_NAME', default=BASE_DIR / 'db.sqlite3')
else:
    if USING_DB == 'mysql':
        DATABASE_ENGINE = resolve('DATABASE_ENGINE', default='django.db.backends.mysql')
    elif USING_DB == 'postgres':
        DATABASE_ENGINE = resolve('DATABASE_ENGINE', default='django.db.backends.postgresql_psycopg2')

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