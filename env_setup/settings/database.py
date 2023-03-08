import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from pprint import pprint

from ..utils import BACK, get_from_options, get_string

_settings = [
    ("USING_DB", 'sqlite'),
    ("DATABASE_NAME", None),
    ("DATABASE_USER", None),
    ("DATABASE_PASSWORD", None),
    ("DATABASE_HOST", None),
    ("DATABASE_PORT", None),
]

database_settings = {
    "Database Settings" : { key : os.getenv(key, default) for key, default in _settings }
}

def database_config():
    while True:
        pprint(database_settings, indent=4)
        options = ["Database Type"]

        if database_settings['Database Settings']['USING_DB'] in ['postgres', 'mysql']:
            options += [
                'Name',
                'Host',
                'Port',
                'User',
                'Password',
                'Options'
            ]

        option = get_from_options(options)

        if option == BACK:
            return

        elif option == 'Database Type':
            database_type = get_from_options([
                'sqlite',
                'mysql',
                'postgres'
            ], default=database_settings['Database Settings']['USING_DB'])

            if database_type == BACK:
                return
            else:
                database_settings['Database Settings']['USING_DB'] = database_type

        elif option in ['Name', 'Host', 'Port', 'User', 'Password']:
            option_set = {
                'Name': "DATABASE_NAME",
                'Host': "DATABASE_HOST",
                'Port': "DATABASE_PORT",
                'User': "DATABASE_USER",
                'Password': "DATABASE_PASSWORD",
            }
            response = get_string(
                f"Enter new {option}", default=database_settings['Database Settings'][option_set[option]])

            if response == BACK:
                return
            else:
                database_settings['Database Settings'][option_set[option]] = response
