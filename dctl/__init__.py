#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/__init__.py
@time: 10/25/17 12:15 AM
"""

import argparse
import sys

from pkg.subcmd import VersionCommand, DNSCommand, GetCommand, ShowCommand


class SubCommands(object):

    @classmethod
    def add(cls, subparsers, *subcmds):
        for subcmd in subcmds:
            p = subparsers.add_parser(subcmd.name, help=subcmd.help)
            for flag in subcmd.flags:
                p.add_argument(*flag.args, **flag.kwargs)
            p.set_defaults(func=subcmd.func, usage=subcmd.usage)
            if subcmd.subcmds:
                cls.add(p.add_subparsers(metavar=subcmd.metavar), *subcmd.subcmds)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(metavar='<subcommand>')
    SubCommands.add(subparsers, VersionCommand, DNSCommand, GetCommand, ShowCommand)
    args = parser.parse_args()

    if hasattr(args, 'func') and args.func is not None:
        return args.func(args)
    else:
        parser.print_help()

