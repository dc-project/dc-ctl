#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/setup.py.py 
@time: 2017/12/16 10:46
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
from pkg.version import VERSION

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='dc-ctl',
    version=VERSION['version'],
    description='Oops tools',
    long_description=long_desc,
    url='https://github.com/dc-project/dc-ctl',
    author='ysicing',
    author_email='ops.ysicing@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: LGPL License',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['venv', 'docs', 'tests']),
    platforms = ["linux", "mac"]
)