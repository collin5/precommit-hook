#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools.command.install import install
from app.extras import template
import os
import sys


class Exec:
    @staticmethod
    def add_pre_commit(path=os.environ["PWD"]):
        # if .git directory exists
        if not os.path.isdir(os.path.join(path, ".git/hooks")):
            message = '*****************************************************************\n'
            message += '* Oops, this hook can only be installed on a local GIT repository\n'
            message += '* Please, make sure to do a "git init" on this folder.'
            print(message)
            sys.exit(1)

        # Ok, it is a GIT repository...
        with open('{}/.git/hooks/pre-commit'.format(path), 'wb') as f:
            f.write(template.encode())
            os.system("chmod +x {}/.git/hooks/pre-commit".format(path))
        print("Precommit script added successfully, continuing ...")
        return True


class Post_install(install):
    def run(self):
        install.run(self)
        Exec.add_pre_commit()
