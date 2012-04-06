#!/usr/bin/env python

from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

with open('README.md') as file:
    long_description = file.read()

setup(
    name = 'bottle-hotqueue',
    version = '0.2.0',
    url = 'https://github.com/waawal/bottle_hotqueue',
    description = 'FIFO Queue for Bottle built upon HotQueue',
    long_description = long_description,
    author = 'Waawal',
    author_email = 'waawal@boom.ws',
    license = 'MIT',
    platforms = 'any',
    py_modules = [
        'bottlehotqueue'
    ],
    requires = [
        'bottle (>=0.9)',
        'hotqueue'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
