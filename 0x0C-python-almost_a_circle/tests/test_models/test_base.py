#!/usr/bin/python3
"""Unitest module"""

import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    """Defines Base class test cases"""

    def test_id(self):
        """test different cases for id """
        B1 = Base()
        B2 = Base()
        B3 = Base(10)
        self.assertEqual(B1.id, 1)
        self.assertEqual(B2.id, 2)
        self.assertEqual(B3.id, 10)

if __name__ == '__main__':
    unittest.main()

