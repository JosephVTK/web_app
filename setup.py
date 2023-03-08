from dotenv import load_dotenv

load_dotenv('.env')

from env_setup.utils import get_from_options, BACK
from env_setup.settings.root import setting_modules

if __name__ == '__main__':
    while True:
        option = get_from_options([key for key, val in setting_modules.items() if val is not None])

        if option == BACK:
            quit()
        else:
            func = setting_modules.get(option)
            if func:
                func()