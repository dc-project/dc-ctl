#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/__main__.py 
@time: 2017/12/16 16:45
"""

import sys
import dctl

if __name__ == '__main__':
    try:
        sys.exit(dctl.main())
    except KeyboardInterrupt:
        print("exit...")