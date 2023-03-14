from .operations import resolve

ALLOWED_HOSTS = resolve('ALLOWED_HOSTS', default="", var_type=list)

INTERNAL_IPS = resolve('INTERNAL_IPS', default="127.0.0.1", var_type=list)