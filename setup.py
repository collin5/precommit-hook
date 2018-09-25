#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.scripts import Post_install
from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))
with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the requirements from the requirements.txt file
with codecs.open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read()

# Get the dev requirements from the requirements-dev.txt file
with codecs.open(path.join(here, 'requirements-dev.txt'), encoding='utf-8') as f:
    requirements_dev = f.read()

setup(
    name="precommit-hook",
    version="0.2.1",
    author="Collins Abitekaniza",
    author_email="abtcolns@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    url="https://github.com/collin5/precommit-hook",
    description="Auto check quality of python code before shipping",
    long_description=long_description,
    install_requires=requirements,
    platforms=['any'],
    extras_require={
        'dev': [requirements_dev.split('\n')]
    },
    scripts=["app/precommit.hook"],
    cmdclass={
            "install": Post_install,
    }
)
