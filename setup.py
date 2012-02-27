#!/usr/bin/env python

from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = 'bottle-hotqueue',
    version = '0.1.3',
    url = 'https://github.com/waawal/bottle_hotqueue',
    description = 'FIFO Queue for Bottle built upon HotQueue',
    author = 'Waawal',
    author_email = 'waawal@boom.ws',
    license = 'MIT',
    platforms = 'any',
    py_modules = [
        'bottle_hotqueue'
    ],
    requires = [
        'bottle (>=0.9)',
        'hotqueue'
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass = {'build_py': build_py}
)
