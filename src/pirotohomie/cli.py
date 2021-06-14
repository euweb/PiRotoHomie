import os
from signal import pause
from pirotohomie.logging import setup_logging

import click
import yaml

def get_config_form_file(filename='config.yaml'):
    if not os.path.isfile(filename):
        raise ValueError('Config file %r does not exist!' % filename)
    with open(filename, 'r') as f:
        return yaml.safe_load(f.read())


@click.command()
@click.option('--log', '-l', type=str, help=u'log config')
@click.argument('config', type=click.Path(exists=True))
def main(config, log):
    setup_logging(log)

    config = get_config_form_file(config)

    pause()

    # except (KeyboardInterrupt, SystemExit):
    #    print("Quitting.")
