#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python packaging."""
import os

from setuptools import setup, find_packages

#: Absolute path to directory containing setup.py file.
here = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(here, 'README.md')).read()
VERSION = '0.0.0.a'

if __name__ == '__main__':  # Do not run setup() when we import this module.
    setup(
        name='poc_ml_versioning',
        version=VERSION,
        description='A POC to link them all.',
        long_description=README,
        classifiers=[
            "Programming Language :: Python :: 3",
        ],
        keywords='peopledoc',
        author='Peopledoc',
        author_email='sarah.diot-girard@people-doc.com',
        url='http://github.com/peopledoc/',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=True,
        # install_requires=parse_requirements('requirements.yml'),
    )