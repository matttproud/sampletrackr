#!/usr/bin/python2.4

import mox


class TestBase(mox.MoxTestBase):
  def assertIsNone(self, other):
    self.assertEqual(None, other, 'Expected other to be None.')
