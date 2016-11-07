"""
Feed it with a configuration template and a file with
parameters, and it will give you a configuration file in return.
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
    config_params = dict([line.split() for line in params_file])

    with open(config_new, 'w') as config:
        for line in file:
            template = Template(line)
            if line in file:
                config.write(template.render(config_params) + '\n')
            else:
                config.write(line + '\n')
        print('Wrote configuration file at %s.' % (os.getcwd()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Creates a configuration based on a file with parameters.')
    parser.add_argument('config_template', type=open, help='Configuration Template')
    parser.add_argument('params_file', type=open, help='Parameter file location')
    parser.add_argument('config_new', type=str, help='Name of output file')
    args = parser.parse_args()
    file_input(args.config_file, args.params_file, args.config_new)
    