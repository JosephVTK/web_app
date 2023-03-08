from ..utils import BACK, get_from_options, get_string
import os

_settings = [
    ("EMAIL_BACKEND", None),
    ("EMAIL_FILE_PATH", None),
    ("EMAIL_HOST", None),
    ("EMAIL_PORT", None),
    ("EMAIL_HOST_USER", None),
    ("EMAIL_HOST_PASSWORD", None),
    ("EMAIL_USE_TLS", None),
    ("EMAIL_USE_SSL", None),
    ("EMAIL_TIMEOUT", None),
    ("EMAIL_SSL_KEYFILE", None),
    ("EMAIL_SSL_CERTFILE", None),
]

email_settings = {
    "Email Settings" : { key : os.getenv(key, default) for key, default in _settings }
}

def email_config():
    while True:
        options = ["Backend"]

        if email_settings['Email Settings']['EMAIL_BACKEND'] == 'django.core.mail.backends.smtp.EmailBackend':
            options += [
                'Host', 'Port', 'Host User', 'Host Password', 'Use TLS', 'Use SSL', 'Timeout', 'SSL Keyfile', 'SSL Cert'
            ]

        if email_settings['Email Settings']['EMAIL_BACKEND'] == 'django.core.mail.backends.filebased.EmailBackend':
            options.append('File Path')

        option = get_from_options(options)

        if option == BACK:
            return
        
        elif option == 'Backend':
            backend = get_from_options([
                'django.core.mail.backends.console.EmailBackend',
                'django.core.mail.backends.filebased.EmailBackend',
                'django.core.mail.backends.smtp.EmailBackend',
                'django.core.mail.backends.locmem.EmailBackend',
                'django.core.mail.backends.dummy.EmailBackend'
                'Custom'
            ], default=email_settings['Email Settings']['EMAIL_BACKEND'])
            if backend == BACK:
                return
            elif backend == 'Custom':
                email_settings['Email Settings']['EMAIL_BACKEND'] = get_string('Enter your custom backend.')
            else:
                email_settings['Email Settings']['EMAIL_BACKEND'] = backend

        elif option == 'File Path':
            file_path = get_string("New file path.", default=email_settings['Email Settings']['EMAIL_FILE_PATH'])
            if file_path == BACK:
                return
            elif not os.path.exists(file_path):
                print ("File path does not exist.")
            else:
                email_settings['Email Settings']['EMAIL_FILE_PATH'] = file_path

        elif option == 'Host':
            response = get_string(f"Enter new {option}", default=email_settings['Email Settings']['EMAIL_HOST'])
            if response is not BACK:
                email_settings['Email Settings']['EMAIL_HOST'] = response

        elif option == 'Port':
            response = get_string(f"Enter new {option}", default=email_settings['Email Settings']['EMAIL_PORT'])
            if response is not BACK:
                if response.isdigit():
                    email_settings['Email Settings']['EMAIL_PORT'] = response
                else:
                    print ("Port must be digit.")

        elif option == 'Host User':
            response = get_string(f"Enter new {option}", default=email_settings['Email Settings']['EMAIL_HOST_USER'])
            if response is not BACK:
                email_settings['Email Settings']['EMAIL_HOST_USER'] = response

        elif option == 'Host Password':
            response = get_string(f"Enter new {option}", default=email_settings['Email Settings']['EMAIL_HOST_PASSWORD'])
            if response is not BACK:
                email_settings['Email Settings']['EMAIL_HOST_PASSWORD'] = response