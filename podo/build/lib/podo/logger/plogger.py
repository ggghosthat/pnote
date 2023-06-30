import logging.config
from .ponfig import PONFIG

def get_logger():
    logging.config.dictConfig(PONFIG)
    return logging.getLogger('sqlalchemy.engine')
