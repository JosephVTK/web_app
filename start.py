import os

command_list = [
    'python manage.py migrate',
    'python manage.py collectstatic'
]

for command in command_list:
    os.system(command)