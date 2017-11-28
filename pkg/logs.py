#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: /logs.py
@time: 17-11-26 下午11:00
"""

import platform
import logging
import logging.config

system = platform.system().lower()

if system == 'darwin':
    LOG_FILE = '/tmp/dc.log'
else:
    LOG_FILE = '/var/log/dc.log'


CONFIG = {
    'version': 1,
    'filters': {},
    'formatters':{
        'standard': {
            'format': "%(asctime)s [%(levelname)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'raw': {
                    'format': "%(message)s"
        }
    },
    'handlers': {
        'dc': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'default': {
            'handlers': ['dc'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

logging.config.dictConfig(CONFIG)

default_logger = logging.getLogger('default')