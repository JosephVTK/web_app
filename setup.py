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

if __name__ == '__main__':
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]

    # Options
    options = ""

    # Long options
    long_options = ["help", "username=", "host=", "db=", "port=", 'new']

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        username = None
        host = None
        port = None
        password = None
        database = None
        new = False

        # checking each argument
        for key, val in arguments:
            key = key.lower()

            if key in ("-h", "--help"):
                print("""Options:
                --username > ['Username'] REQUIRED
                --host > ['localhost']
                --port > ['8000']
                --db > ['sqlite', 'mysql']

                --new : Will over-write existing environment file.
                """)

            elif key in ("--username"):
                username = val

            elif key in ("--host"):
                host = val

            elif key in ("--port"):
                if val.isdigit() == False:
                    raise getopt.GetoptError('Port must be numerical.')
                port = val

            elif key in ("--db"):
                print(f"Enabling special output mode {val}")

                if val not in ['sqlite', 'mysql']:
                    raise getopt.GetoptError(
                        'Database choices are [sqlite, mysql]')

                database = val

            elif key in ("--new"):
                new = True

        if not username:
            raise getopt.GetoptError('Username required.\n See Help > --help.')

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        sys.exit()

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
