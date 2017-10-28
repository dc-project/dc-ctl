#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/dns.py 
@time: 2017/10/27 10:46
"""

from . import SubCommand


def _show_dns(args):
    print('dns null')

DNSCommand = SubCommand(
    name='dns',
    help='help your dns',
    metavar='',
    func=_show_dns
)
