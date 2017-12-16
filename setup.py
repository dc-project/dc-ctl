#!/usr/bin/env python3
# coding=utf-8

"""
@version:0.1
@author: ysicing
@file: dc-ctl/setup.py.py 
@time: 2017/12/16 10:46
"""

import sys
from codecs import open

from pkg.version import VERSION
from setuptools import setup, find_packages

if sys.version_info < (2, 7, 14) or (3, 0) <= sys.version_info < (3, 5):
    print("dc-ctl requires at least Python 3.6 to run.")
    sys.exit(1)

with open('README.rst', encoding='utf-8') as f:
    long_desc = f.read()


def get_data_files():
    data_files = [
        ('share/docs/dctl', ['README.rst'])
    ]

    return data_files


def get_install_requires():
    requires = ['psutil>=2.0.0']
    if sys.platform.startswith('win'):
        requires.append('bottle')

    return requires

setup(
    name='dc-ctl',
    version=VERSION['version'],
    description='Oops tools',
    long_description=long_desc,
    url='https://github.com/dc-project/dc-ctl',
    license='LGPLv3',
    author='ysicing',
    author_email='ops.ysicing@gmail.com',
    install_requires=get_install_requires(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['venv', 'docs', 'tests']),
    platforms=["linux", "mac"],
    include_package_data=True,
    data_files=get_data_files(),
    entry_points={
        'console_scripts': ['dc-ctl=dcctl:main'],
    }
)