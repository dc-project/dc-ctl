#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: /base.py
@time: 17-11-29 上午12:13
"""

import datetime
import os
import psutil
import time
import uuid



class MachineStatus(object):

    def __init__(self):
        self.MAC = None
        self.IP = None
        self.HOSTNAME = None
        self.cpu = {}
        self.mem = {}
        self.network = {}



