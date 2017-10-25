#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/version.py
@time: 10/25/17 12:16 AM
"""

from . import SubCommand


def _show_version(args):
    try:
        from pkg.version import VERSION
        for name, value in VERSION.items():
            print(" {0:10s} :\t{1}".format(name, value))
    except ImportError as e:
        print("get version info failed")


VersionCommand = SubCommand(
    name="version", help="show command version", metavar="", func=_show_version)