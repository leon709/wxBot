#!/usr/bin/env python
# coding: utf-8

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d][%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='test.log',
                    filemode='a')
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d][%(levelname)s] %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(sh)
logger.setLevel(20)

if __name__ == '__main__':
    logger.debug('debug message: %s', 233)
    logger.info('info message')
#     logger.warning('warning message')
#     logger.error('error message')
#     logger.critical('critical message')
