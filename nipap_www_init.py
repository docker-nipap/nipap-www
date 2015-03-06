'''This will generate a base nipap-www configuration based on vars within env

Will default to reasonable values where possible
'''

import os
from ConfigParser import SafeConfigParser


def setup_environment():

    default_environment = {
        'NIPAPD': 'nipapd',
        'NIPAPD_USER': '',
        'NIPAPD_PASS': '',
        'NIPAPD_AUTH': 'local',
        'WELCOME_MSG': 'NIPAP Docker Container',
        'DEBUG': 'false',
        'EMAIL_TO': 'you@yourdomain.com',
        'SMTP_SERVER': 'localhost',
        'EMAIL_FROM': 'nipap@localhost',
        }

    environment = {}
    for var, default in default_environment.iteritems():
        try:
            environment.update({var: os.environ[var]})
        except KeyError:
            # Allows for blank defaults to be ignored
            if default:
                environment.update({var: default})

    # Set it all back into the environment
    for key, val in environment.iteritems():
        os.environ[key] = val

    return environment


def format_configs(environment):

    # Removed due to moving to parsing existing nipap.conf and adjusting as
    # necessary with ConfigParser.
    # conf_template = open('/resources/nipap-www.conf').read()
    ini_template = open('/resources/nipap-www.ini').read()
    return {
            # '/etc/nipap/nipap-www.conf': conf_template.format(**environment),
            '/etc/nipap/nipap-www.ini': ini_template.format(**environment),
            }


def write_config(configs):
    '''Expect configs to be a dict of filepath to contents'''

    for file_path, contents in configs.iteritems():
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as config_file:
                config_file.write(contents)


def modify_main_conf(environment):
    '''Checks for [www] section in main config. Add/Modify as needed'''

    file_path = '/etc/nipap/nipap.conf'
    parser = SafeConfigParser()
    parser.read(file_path)
    if 'www' not in parser.sections():
        parser.add_section('www')
    parser.set(
        'www',
        'xmlrpc_uri',
        'http://{NIPAPD_USER}@{NIPAPD_AUTH}:{NIPAPD_PASS}@{NIPAPD}:1337'.\
                format(**environment)
        )
    parser.set('www',
               'welcome_message',
               '{WELCOME_MSG}'.format(**environment)
               )
    with open(file_path, 'w') as f:
        parser.write(f)


def main():

    environment = setup_environment()
    configs = format_configs(environment)
    write_config(configs)
    modify_main_conf(environment)


if __name__ == '__main__':
    main()
