#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines max_int fn test cases"""

    def test_args(self):
        """test arg passed to max_int fn"""
        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer([4]), 4)

        self.assertEqual(max_integer([5, 2, 4, 6]), 6)

        self.assertEqual(max_integer([7, 2, 4, 6]), 7)

        self.assertEqual(max_integer([5, 10, 4, 6]), 10)

        self.assertEqual(max_integer([5, 2, 4, -6]), 5)

        self.assertEqual(max_integer([-5, -2, -4, -6]), -2)

