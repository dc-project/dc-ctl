#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/dns.py 
@time: 2017/10/27 10:46
"""

from pkg.control.dns.dns import DnsController

from . import BaseFlag, SubCommand


def _dns(args):
    dns = DnsController()
    return dns.get_local_dns()

DNSCommand = SubCommand(
    name='dns',
    help='help your dns',
    metavar='<domain resolution>',
    flags=[],
    subcmds=[
        SubCommand(name="local",usage="local dns",
                   flags=[],
                   func=_dns),
        SubCommand(name="ali",usage="domain resolution",
                   flags=[
                       BaseFlag('list', metavar='list domain', nargs='?')

                   ],
                   func=_dns),
    ]
)
