#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: /config.py
@time: 17-11-26 下午10:58
"""

class Config(object):

    config = {}

    @classmethod
    def get(cls, key, default=None):
        return cls.config.get(key,default)

    @classmethod
    def set(cls, key, value):
        cls.config[key] = value