#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        # ---- boundary / valid ----
        def test_valid_1_1 (self):
                self.assertEqual (1, calc(1,1))

        def test_valid_1_999 (self):
                self.assertEqual (999, calc(1,999))

        def test_valid_999_1 (self):
                self.assertEqual (999, calc(999,1))

        def test_valid_999_999 (self):
                self.assertEqual (998001, calc(999,999))

        # ---- boundary / invalid range ----
        def test_invalid_0_1 (self):
                self.assertEqual (-1, calc(0,1))

        def test_invalid_1_0 (self):
                self.assertEqual (-1, calc(1,0))

        def test_invalid_1000_1 (self):
                self.assertEqual (-1, calc(1000,1))

        def test_invalid_1_1000 (self):
                self.assertEqual (-1, calc(1,1000))

        # ---- invalid type (non-integer) ----
        def test_invalid_1_float (self):
                self.assertEqual (-1, calc(1,0.1))

        def test_invalid_strnum_2 (self):
                self.assertEqual (-1, calc("1",2))

        def test_invalid_2_strnum (self):
                self.assertEqual (-1, calc(2,"1"))

