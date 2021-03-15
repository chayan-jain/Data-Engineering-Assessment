import argparse
import logging
import sys

from src.utils.SetUpLogging import setup_logging
from src.init import run

log = logging.getLogger(__name__)

def main():
    try:
        parser = argparse.ArgumentParser(description='Data Adapter main entry point')
        parser.add_argument('--logfile', '-l', type=str, help='log filename, otherwise stream logging')
        parser.add_argument('--verbose', '-v', default=1, action='count', help='increased verbosity')
        args = parser.parse_args()

        setup_logging(verbosity=args.verbose, logfile=args.logfile)

        if args.logfile:
            sys.stderr.write('logging to %s\n' % (args.logfile,))

        run()
    except Exception as exc:
        log.error(exc)


if __name__ == '__main__':
    main()
