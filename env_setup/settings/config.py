import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from pprint import pprint

from ..utils import BACK, get_from_options, get_string

_settings = [
    ("ADMIN_SITE_HEADER", None),
    ("ADMIN_SITE_TITLE", None),
    ("ADMIN_SITE_INDEX_TITLE", None),
]

config_settings = {
    "Config Settings" : { key : os.getenv(key, default) for key, default in _settings }
}


def config_config():
    while True:
        pprint(config_settings, indent=4)
        option = get_from_options(["Admin Header", "Admin Title", "Admin Index Title"])

        if option == BACK:
            return

        elif option == "Admin Header":
            response = get_string("Enter new Admin Header.", default=config_settings['Config Settings']['ADMIN_SITE_HEADER'])

            if response != BACK:
                config_settings['Config Settings']['ADMIN_SITE_HEADER'] = response

        elif option == "Admin Title":
            response = get_string("Enter new Admin Header.", default=config_settings['Config Settings']['ADMIN_SITE_TITLE'])

            if response != BACK:
                config_settings['Config Settings']['ADMIN_SITE_TITLE'] = response
                
        elif option == "Admin Index Title":
            response = get_string("Enter new Admin Index Title.", default=config_settings['Config Settings']['ADMIN_SITE_INDEX_TITLE'])

            if response != BACK:
                config_settings['Config Settings']['ADMIN_SITE_INDEX_TITLE'] = response
                
