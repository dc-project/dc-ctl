#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/get.py
@time: 10/28/17 3:25 PM
"""

from . import BaseFlag,SubCommand


def _get_system(args):
    print('666')


GetCommand = SubCommand(
    name="get", help="get the resource", metavar="<resource>",
    flags=[],
    subcmds=[
        SubCommand(
            name="system", usage="get system resource info",
            flags=[
                BaseFlag('name', metavar='system resource type', nargs='?')
            ],
            func=_get_system
        ),
        SubCommand(
            name="services", usage="get services info",
            flags=[

            ],
            func=_get_system
        )
    ]
)


