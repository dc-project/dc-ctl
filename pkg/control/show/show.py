0#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: /show.py
@time: 17-11-26 下午11:19
"""

import psutil
from pkg.utils.utils import pprint_ntuple

class ShowSM(object):

    #def __init__(self, *args, **kwargs):
    #    pass


    def _show_network(self):
        print("\tip:{}".format("127.0.0.1"))


    def _show_dns(self):
        print("\tdns:{}".format("8.8.8.8"))


    def _show_hostname(self):
        print("\thostname:{}".format("ysbot"))

    def _show_mem(self):
        print("\tMEMORY\n\t------")
        pprint_ntuple(psutil.virtual_memory())
        print("\t\n\tSWAP\n\t------")
        pprint_ntuple(psutil.swap_memory())


    def show(self):
        print("")
        self._show_network()
        self._show_dns()
        self._show_hostname()
        self._show_mem()
        print("")