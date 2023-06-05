import logging.config
from logger.ponfig import PONFIG

def get_logger():
    logging.config.dictConfig(PONFIG)
    return logging.getLogger('sqlalchemy.engine')
