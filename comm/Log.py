import logging
import os
from conf.config import log
from logging.handlers import TimedRotatingFileHandler
_home_path=os.path.dirname(os.path.dirname(__file__))
_log_level=eval(log['log_level'])
_log_path=log['log_path']
_log_format=log['log_format']

_log_file=os.path.join(_home_path,_log_path,'log.txt')
def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=_log_level)
    formatter = logging.Formatter(_log_format)

    handler = TimedRotatingFileHandler(filename=_log_file, when="D", interval=1, backupCount=7)
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)
log_init()
logger = logging.getLogger('main')
logger.info('log test----------')

