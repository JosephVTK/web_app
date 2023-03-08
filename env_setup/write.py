from .settings import SETTINGS

def write_environment_file():
    with open ('test.env', 'w') as f:
        f.write('# ENV DYNAMICALLY GENERATED\n')
        f.write('LOAD_ENV=True\n')
        
        for settings in SETTINGS:
            for group_title, group_settings in settings.items():
                f.write(f'\n# {group_title}\n\n')
                for key, val in group_settings.items():
                    if val is not None:
                        f.write(f'{key}={val}\n')
    input('File Saved.')
