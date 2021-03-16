#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import check


class Test_modules(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(check.sum(5, 7), 12)


if __name__ == "__main__":
    unittest.main()
