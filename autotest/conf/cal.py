import logging

logger = logging.getLogger()

def add(x, y):
    logger.warning("add x={} y={}".format(x, y))