import os
from pathlib import Path
from django.core.management.utils import get_random_secret_key
from pprint import pprint

from ..utils import BACK, get_from_options, get_string

_settings = [
    ("SECRET_KEY", get_random_secret_key),
    ("DEBUG", 'True'),
]

base_settings = {
    "Base Settings": {key: os.getenv(key, default() if callable(default) else default) for key, default in _settings}
}

def base_config():
    while True:
        pprint(base_settings, indent=4)
        option = get_from_options(["Debug"])

        if option == BACK:
            return

        elif option == 'Debug':
            debug = get_from_options([
                'True',
                'False'
            ], default=base_settings['Base Settings']['DEBUG'])
            if debug == BACK:
                return
            else:
                base_settings['Base Settings']['DEBUG'] = debug
