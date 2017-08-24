#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.scripts import *
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

setup(

    # Application name
    name="precommit-hook",

    version="0.0.2",
    author="Collins Abitekaniza",
    author_email="abtcolns@gmail.com",
    packages=['app'],
    include_package_data=True,
    license='MIT',
    url="https://github.com/collin5/precommit-hook",
    description="Enforce code quality in python projects",
    install_requires=["flake8"],
    scripts=["app/precommit.hook"],
    cmdclass={
            "install": Post_install,
    }
)
