"""
WSGI config for web_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

dotenv.load_dotenv('.env')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')

application = get_wsgi_application()
