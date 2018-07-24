import base64
import logging
from autotest.conf import cal

# logging.basicConfig(level=logging.DEBUG)
from autotest.conf import log2

# logging.basicConfig(filename="a.log", level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')

logger = logging.getLogger()

formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler("./b.log")
fh.setFormatter(formatter)
logger.addHandler(fh)

def test():
    print('111111')

    logging.info('hello....')
    logging.warning("wain")

    logging.error('error...')

    log2.a()


test()
cal.add(1, 2)



