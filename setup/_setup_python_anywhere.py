from os.path import exists

from django.core.management.utils import get_random_secret_key

def generate_new_env(template, rewrite=False):
    if exists('.env'):
        if rewrite:
            result = input('Rewriting the environment file will cause you to lose the secret key. This may cause database issues. Are you sure you wish to proceed?\n Enter "YES" if you wish to proceed.\n > ')

            if result != 'YES':
                return False
        else:
            print('Environment File Already Exists...')
            return False

    with open('.env', 'w') as f:
        f.write(template)

    return True


def generate_template(template, username, host, port, database):
    template_string = ""
    template_args = {
        '{NEW_SECRET_KEY}': get_random_secret_key(),
        '{USERNAME}': username,
        '{HOST}': host,
        '{PORT-COLON}': f':{port}' if port else None,
        '{PORT}': port,

        '{DATABASE}': database,
    }

    for key, val in template.items(): 
        line = val

        for tag, replacement in template_args.items():
            line = line.replace(tag, replacement if replacement else '')

        template_string += f'{key}={line}\n'

    return template_string


def handle(*args):
    template, username, host, port, password, database, new = args

    if not host:
        host = f"https://{username}.pythonanywhere.com,127.0.0.1"

    if not database:
        database = 'sqlite'

    template['MYSQL_HOST'] = "{USERNAME}.mysql.pythonanywhere-services.com"

    if generate_new_env(generate_template(template=template, username=username, host=host, port=port, database=database), new) == True:
        print("New Environment File Created...")
