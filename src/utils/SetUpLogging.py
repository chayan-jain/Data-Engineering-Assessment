import copy
import logging.config

from twisted.logger import globalLogBeginner, STDLibLogObserver

VERB_DEBUG = 2
VERB_INFO = 1
VERB_WARNING = 0
VERB_ERROR = -1
VERB_CRITICAL = -2
VERBOSITY_TO_LEVEL_MAP = {
    VERB_DEBUG: logging.DEBUG,
    VERB_INFO: logging.INFO,
    VERB_WARNING: logging.WARNING,
    VERB_ERROR: logging.ERROR,
    VERB_CRITICAL: logging.CRITICAL,
}

MINLEVEL = min(VERBOSITY_TO_LEVEL_MAP.keys())
MAXLEVEL = max(VERBOSITY_TO_LEVEL_MAP.keys())


def level_from_verbosity(verbosity=VERB_WARNING):
    if verbosity < MINLEVEL:
        verbosity = MINLEVEL
    elif verbosity > MAXLEVEL:
        verbosity = MAXLEVEL
    return VERBOSITY_TO_LEVEL_MAP[verbosity]


DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'textual': {
            'format': '%(asctime)s %(levelname)s %(name)-12s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/log/cosmos-dao.log',
            'formatter': 'textual',
            'maxBytes': 10e6,
            'backupCount': 10,
        },
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'textual',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'stream'],
            'level': 'INFO',
        },
    }
}


def setup_logging(verbosity=VERB_INFO, logfile=None, logging_settings=None):
    '''
    Application logging setup.
    The basic log settings are captured in DEFAULT_LOGGING per
    logging.config.dictConfig specification.
    Use logfile to specify a RotatingFileHandler, otherwise a streamhandler is used
    If additional logging_settings are included, logging.config.dictConfig
    is called a second time with those logging_settings.
    :param verbosity: control the overall logging level
    :param logfile: specify a logfile for RotatingFileHandler
    :param logging_settings: additional logging.config.dictConfig
    '''
    base_settings = copy.deepcopy(DEFAULT_LOGGING)
    level = level_from_verbosity(verbosity)

    if logfile:
        base_settings['handlers'].pop('stream')
        base_settings['loggers']['']['handlers'].remove('stream')
        if logfile != base_settings['handlers']['file']['filename']:
            base_settings['handlers']['file']['filename'] = logfile
    else:
        base_settings['handlers'].pop('file')
        base_settings['loggers']['']['handlers'].remove('file')

    if level != logging.INFO:
        base_settings['loggers']['']['level'] = level

    logging.config.dictConfig(base_settings)
    globalLogBeginner.beginLoggingTo([STDLibLogObserver()], redirectStandardIO=False)

    if logging_settings:
        logging.config.dictConfig(logging_settings)

    logging.info('first line of log stream')
