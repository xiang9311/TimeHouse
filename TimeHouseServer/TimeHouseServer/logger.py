__author__ = '祥祥'
import logging

# log
logger = logging.getLogger('django')

def info(content):
    logger.info(content)

def debug(content):
    logger.debug(content)

def warn(content):
    logger.warn(content)

def error(content):
    logger.error(content)