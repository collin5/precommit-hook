#!/usr/bin/env python
# -*- coding: utf-8 -*-
# setup.py
# Copyright (c) 2017 Collins Abitekaniza <abtcolns@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from app.scripts import *
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

setup(

    # Application name
    name="precommit-hook",

    version="0.0.1",
    author="Collins Abitekaniza",
    author_email="abtcolns@gmail.com",
    packages=['app'],
    include_package_data=True,
    license='MIT',
    url="https://github.com/collin5/precommit-hook",
    description="Enforce code quality in python projects",
    install_requires=["flake8"],
    cmdclass={
            "install": Post_install,
            "develop": Post_develop,
            "egg_info": Post_egg_info
    }
)
