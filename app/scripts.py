#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app/scripts.py
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

from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
import os


class Exec:
    @staticmethod
    def add_pre_commit():

        # if .git directory exists
        if os.path.isdir(os.path.join(os.getcwd(), ".git")):
            # make hook directory if not exists
            if not os.path.isdir(os.path.join(os.getcwd(), ".git/hooks")):
                os.system("mkdir -p .git/hooks")

            # finally copy and set permissions
            os.system(
                "cp app/tmp/template.dat .git/hooks/pre-commit && sudo chmod +x .git/hooks/pre-commit")
            print("Precommit added successfully, continuing ...")
        else:
            print(
                "Error installing precommit-hook : .git directory not found in current working path")
        return True


class Post_install(install):

    def run(self):
        install.run(self)
        Exec.add_pre_commit()


class Post_develop(develop):

    def run(self):
        develop.run(self)
        Exec.add_pre_commit()


class Post_egg_info(egg_info):

    def run(self):
        egg_info.run(self)
        Exec.add_pre_commit()
