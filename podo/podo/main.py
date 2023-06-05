from models.dashboard import Dashboard
from datetime import datetime
from base import logger

dash = Dashboard()
logger.debug("Hello Debug")
logger.error("Hello world")
logger.info("New info")
logger.critical('critical error come here right now!')