"""
textlines.

Usage:
  textlines [options] <source>

  textlines -h | --help

Options:
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
    print(textlines.text_lines(open(arguments['<source>']).read()))
