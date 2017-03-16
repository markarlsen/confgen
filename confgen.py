"""
Feed it with a configuration template and a file with
key/value parameters and it will give you a configuration file in return.
"""
import argparse
import os

from jinja2 import Template

def file_input(config_template, params_file, config_new):
    """
    Creates a file, reads through the configuration template
    and replaces the parameters in the template.
    """
    file = [line for line in config_template]
    config_params = dict([line.rstrip('\n').split(';') for line in params_file])
    with open(config_new, 'w') as config:
        for line in file:
            template = Template(line)
            if line in file:
                config.write(template.render(config_params) + '\n')
            else:
                config.write(line + '\n')
        print('Wrote "%s" at %s' % (config_new, os.getcwd()))

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description='Creates configuration based on template and csv-file')
        parser.add_argument('config_template', type=open,
                            help='Configuration template file')
        parser.add_argument('params_file', type=open,
                            help='CSV-file with key/value pairs')
        parser.add_argument('config_new', type=str,
                            help='Name of output configuration file')
        args = parser.parse_args()
        file_input(args.config_template, args.params_file, args.config_new)
    except FileNotFoundError as err:
        print('File not found: \n' + str(err))