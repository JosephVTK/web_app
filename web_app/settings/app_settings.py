import os
from importlib import import_module

DEBUG = os.getenv('DEBUG', 'False') == "True"

APP_INDEX = (
    # Name,                                   Production,  Development, Enabled
    ('django.contrib.admin',                  True,        True,        True,        None),
    ('django.contrib.auth',                   True,        True,        True,        None),
    ('django.contrib.contenttypes',           True,        True,        True,        None),
    ('django.contrib.sessions',               True,        True,        True,        None),
    ('django.contrib.messages',               True,        True,        True,        None),
    ('django.contrib.staticfiles',            True,        True,        True,        None),
    ('django.contrib.sites',                  True,        True,        True,        None),
    ('django.contrib.sitemaps',               True,        True,        True,        None),

    ('debug_toolbar',                         False,       True,        True,        None),
    ('corsheaders',                           True,        True,        True,        None),
    ('rest_framework',                        True,        True,        True,        None),

    ('account.apps.AccountConfig',            True,        True,        True,        'account.settings'),
    ('user_profile.apps.UserProfileConfig',   True,        True,        True,        None),
    ('blog.apps.BlogConfig',                  True,        True,        True,        None),
    ('document.apps.DocumentConfig',          True,        True,        True,        None),
    ('core_app.apps.CoreAppConfig',           True,        True,        True,        None),
)

INSTALLED_APPS = [ app for app, production, development, enabled, _ in APP_INDEX if (enabled and ((DEBUG is False and production == True) or (DEBUG is True and development == True))) ]

for _, _, _, _, settings in APP_INDEX:
    if settings is not None:
        locals().update({ key : val for key, val in import_module(settings).__dict__.items() if not key.startswith('_') })
