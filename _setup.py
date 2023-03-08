import sys
import getopt
from pprint import pformat

import setup._setup_python_anywhere as _setup_python_anywhere

env_template ={
    "LOAD_ENV":"True",
    "DEBUG":"True",
    "SECRET_KEY":"{NEW_SECRET_KEY}",
    "ALLOWED_HOSTS":"{HOST}",
    "CORS_ALLOWED_ORIGINS":"{HOST}{PORT-COLON}",
    "CSRF_TRUSTED_ORIGINS":"{HOST}{PORT-COLON}",

    # Options are 'sqlite' and 'mysql'
    "USING_DB":"{DATABASE}",

    "MYSQL_NAME":"{USERNAME}$default",
    "MYSQL_USER":"{USERNAME}",
    "MYSQL_HOST":"{USERNAME}",

    # Make sure to change this password for the MYSQL database
    "MYSQL_PASSWORD":"PASSWORD ",

    "ADMIN_SITE_HEADER" : "Admin Console",
    "ADMIN_SITE_TITLE" : "Admin Console Controls",
    "ADMIN_SITE_INDEX_TITLE" : "The Control Console",
}

def gather_input(input_str, default=None, options=None):
    while True:
        if options != None:
            print (f'Options = [{str(options)}]')
        if default != None:
            print (f'Default = [{str(default)}]')
        g_input = input(input_str + " > ").strip()

        if g_input == '':
            if default is not None:
                g_input = default
            else:
                print ("-- Not valid input.")
                continue

        if options and g_input not in options:
            print ("-- Not a valid option")
            continue

        result = input(f"Is [{g_input}] correct? (y/n)").strip().lower()

        if result in ['', 'y']:
            if result == '' and default == None:
                continue
            break

    return g_input

if __name__ == '__main__':
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]

    username = gather_input('What is your username?', '')
    host = gather_input('Host Name?', '')
    port = gather_input('Port?', '')
    password = gather_input('Password?', '')
    database = gather_input('Database?', 'sqlite', ['sqlite', 'mysql', 'postgres'])
    new = False if gather_input('Overwrite existing database?', 'false', ['true', 'false']) == 'false' else True


    setup_options = {
        1 : ('Python Anywhere', _setup_python_anywhere.handle )
    }

    input_char = None

    while True:
        input_char = input (pformat([ f'{x}: {y}' for x, (y, z) in setup_options.items()], indent=4) + '\n (Q) for Quit > ')
        if not input_char:
            print ('No Value Found')
            continue

        input_char = input_char[0]

        if input_char.lower() == 'q':
            break

        try:
            input_char = int(input_char)
        except ValueError:
            print ('Value Error')
            continue

        _, func = setup_options.get(input_char, (None, None))
        if not func:
            print ('Incorrect Option')
            continue

        func(env_template, username, host, port, password, database, new)
        break
