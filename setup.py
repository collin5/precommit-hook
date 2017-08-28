#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.scripts import Post_install
from setuptools import setup

setup(

    # Application name
    name="precommit-hook",

    version="0.1.7",
    author="Collins Abitekaniza",
    author_email="abtcolns@gmail.com",
    packages=['app'],
    include_package_data=True,
    license='MIT',
    url="https://github.com/collin5/precommit-hook",
    description="Auto check quality of python code before shipping",
    long_description="Auto check quality of python code before shipping",
    install_requires=["flake8"],
    scripts=["app/precommit.hook"],
    cmdclass={
            "install": Post_install,
    }
)
