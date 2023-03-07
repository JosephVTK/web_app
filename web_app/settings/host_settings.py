import os

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]