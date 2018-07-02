#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests import BaseTestCase
from app.scripts import Exec
import os


class PreCommitTestCase(BaseTestCase):

    def test_add_precommit_successfully(self):
        action = Exec.add_pre_commit("/tmp/precommit-hook-tests")
        self.assertTrue(action)

    def test_add_precommit_successfully_2(self):
        action = Exec.add_pre_commit("/tmp/precommit-hook-tests")
        self.assertTrue(action)
        self.assertTrue(os.path.isfile("/tmp/precommit-hook-tests/.git/hooks/pre-commit"))
