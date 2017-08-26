#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools.command.install import install
from app.extras import template
import os


class Exec:
    @staticmethod
    def add_pre_commit(path=os.getcwd()):

        # if .git directory exists
        if os.path.isdir(os.path.join(path, ".git")):
            # make hook directory if not exists
            if not os.path.isdir(os.path.join(os.getcwd(), ".git/hooks")):
                os.system("mkdir -p {}/.git/hooks".format(path))
        else:
            os.system("git init {}".format(path))

        # finally copy and set permissions
        with open('{}/.git/hooks/pre-commit'.format(path), 'wb') as f:
            f.write(template.encode())
            os.system("sudo chmod +x {}/.git/hooks/pre-commit".format(path))
        print("Precommit added successfully, continuing ...")
        return True


class Post_install(install):

    def run(self):
        install.run(self)
        Exec.add_pre_commit()
