from .email import email_config
from .base import base_config
from .host import host_config
from .database import database_config
from .config import config_config

from ..write import write_environment_file

setting_modules = {
    "Base Settings" : base_config,
    "Host Settings" : host_config,
    "App Settings" : None,
    "Middleware Settings" : None,
    "Template Settings" : None,
    "Database Settings" : database_config,
    "Validation Settings" : None,
    "Static Settings" : None,
    "Email Settings" : email_config,
    "API Settings" : None,
    "Security Settings" : None,
    "Config Settings" : config_config,
    "Write Environment File" : write_environment_file
}