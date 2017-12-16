#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/__init__.py
@time: 10/25/17 12:16 AM
"""

class BaseFlag(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class SubCommand(object):

    def __init__(self, name, usage="", help=None, metavar=None, flags=[], subcmds=[], func=None):
        self.name = name
        self.usage = usage
        self.help = help
        self.metavar = metavar
        self.flags = flags
        self.subcmds = subcmds
        self.func = func

from .version import *
from .dns import *
from .get import *
from .show import *