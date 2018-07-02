#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
import os


class BaseTestCase(TestCase):

    def setUp(self):
        # create test temporary directory
        os.system("mkdir -p /tmp/precommit-hook-tests && cd /tmp/precommit-hook-tests && git init")  # noqa

    def tearDown(self):
        # remove all test files
        os.system("rm -r /tmp/precommit-hook-tests")  # noqa
