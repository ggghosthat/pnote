PONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'zero_formatter': {
            'format': '[%(levelname)s: %(asctime)s] %(message)s'
        },
    },

    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'zero_formatter',
            'filename': 'crash.log',
            'level': 'ERROR'
        },
        'stdio_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'zero_formatter',
            'level': 'INFO'
        }
    },

    'loggers': {
        'sqlalchemy.engine': {
            'handlers': ['file_handler'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}