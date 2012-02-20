#!/usr/bin/env python

from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = 'bottle-hotqueue',
    version = '0.1.2',
    url = 'https://github.com/waawal/bottle_hotqueue',
    description = 'FIFO Queue for Bottle built upon redis',
    author = 'Daniel Waardal',
    author_email = 'daniel.waardal@vodial.com',
    license = 'MIT',
    platforms = 'any',
    py_modules = [
        'bottle_hotqueue'
    ],
    requires = [
        'bottle (>=0.9)',
        'redis (>=2.0)',
        'hotqueue',
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
