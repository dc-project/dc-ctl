#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/show.py
@time: 10/25/17 12:16 AM
"""

from . import SubCommand
from pkg.control.show.show import ShowSM


def _show(args):
    m = ShowSM()
    m.show()


ShowCommand = SubCommand(
    name="show", help="show info", metavar="", func=_show)