import os
from django.core.management.utils import get_random_secret_key
from pprint import pprint

from ..utils import BACK, get_from_options, get_string

_settings = [
    ("ALLOWED_HOSTS", '127.0.0.1,localhost'),
    ("INTERNAL_IPS", "127.0.0.1")
]

host_settings = {
    "Host Settings" : { key : os.getenv(key, default) for key, default in _settings }
}

def host_config():
    while True:
        pprint(host_settings, indent=4)
        option = get_from_options(["Allowed Hosts", 'Internal IPs'])

        if option == BACK:
            return

        elif option == 'Allowed Hosts':
            host = get_from_options(host_settings['Host Settings']['ALLOWED_HOSTS'].split(',') + [
                'New'
            ], default=host_settings['Host Settings']['ALLOWED_HOSTS'])
            if host == BACK:
                return
            elif host in host_settings['Host Settings']['ALLOWED_HOSTS'].split(','):
                hosts = host_settings['Host Settings']['ALLOWED_HOSTS'].split(',')
                new_host = get_string('Change host or "!" to delete.', default=host)

                if new_host == "!":
                    hosts.remove(host)
                    host_settings['Host Settings']['ALLOWED_HOSTS'] = ",".join(hosts)
                else:
                    hosts.remove(host)
                    hosts.append(new_host)
                    host_settings['Host Settings']['ALLOWED_HOSTS'] = ",".join(hosts)
            elif host == 'New':
                new_host = get_string('Enter host')
                hosts = host_settings['Host Settings']['ALLOWED_HOSTS'].split(',')
                hosts.append(new_host)
                host_settings['Host Settings']['ALLOWED_HOSTS'] = ",".join(hosts)

        elif option == 'Internal IPs':
            ip_address = get_from_options(host_settings['Host Settings']['INTERNAL_IPS'].split(',') + [
                'New'
            ], default=host_settings['Host Settings']['INTERNAL_IPS'])
            if ip_address == BACK:
                return
            elif ip_address in host_settings['Host Settings']['INTERNAL_IPS'].split(','):
                ip_addresses = host_settings['Host Settings']['INTERNAL_IPS'].split(',')
                new_ip = get_string('Change Internal IP or "!" to delete.', default=ip_address)

                if new_ip == "!":
                    ip_addresses.remove(ip_address)
                    host_settings['Host Settings']['INTERNAL_IPS'] = ",".join(ip_addresses)
                else:
                    ip_addresses.remove(ip_address)
                    ip_addresses.append(new_ip)
                    host_settings['Host Settings']['INTERNAL_IPS'] = ",".join(ip_addresses)
            elif ip_address == 'New':
                new_ip = get_string('Enter Internal IPs')
                ip_addresses = host_settings['Host Settings']['INTERNAL_IPS'].split(',')
                ip_addresses.append(new_ip)
                host_settings['Host Settings']['INTERNAL_IPS'] = ",".join(ip_addresses)

