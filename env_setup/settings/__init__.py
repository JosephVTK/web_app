from .base import base_settings
from .email import email_settings
from .host import host_settings
from .database import database_settings
from .config import config_settings

SETTINGS = [base_settings, host_settings, database_settings, email_settings, config_settings]