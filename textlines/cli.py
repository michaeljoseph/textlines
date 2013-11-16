"""
textlines.

Usage:
  textlines [options] command <param> <another_params>
  textlines [options] another-command <param>

  textlines -h | --help

Options:
  --kw-arg=<kw>         Keyword option description.
  -b --boolean          Boolean option description.
  --debug               Debug.

  -h --help             Show this screen.
"""

from docopt import docopt
import logging

import textlines

log = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=textlines.__version__)
    debug = arguments['--debug']
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)