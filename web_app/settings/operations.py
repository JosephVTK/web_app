import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class EnvironmentError(Exception):
    def __init__(self, environment_variable):
        super().__init__(f"Missing or misconfigured environment variable: {environment_variable}\nResponse: [{os.getenv(environment_variable)}]")

def resolve(variable_name, default=None, var_type=str, raise_error=False):
    variable = os.getenv(variable_name, default)

    if raise_error and variable is None:
        raise EnvironmentError(variable_name)
    
    if var_type == bool:
        if variable.lower() in ['false', '0', 'no']:
            variable = False
        elif variable.lower() in ['true', '1', 'yes']:
            variable = True
        else:
            raise EnvironmentError(variable_name)
        
    elif var_type == int:
        try:
            variable = int(variable)
        except:
            raise EnvironmentError(variable_name)
        
    elif var_type == float:
        try:
            variable = float(variable)
        except:
            raise EnvironmentError(variable_name)
        
    elif var_type == list:
        try:
            variable = variable.split(',')
        except:
            raise EnvironmentError(variable_name)

    elif var_type == str:
        pass

    else:
        raise EnvironmentError(variable_name)
    
    return variable