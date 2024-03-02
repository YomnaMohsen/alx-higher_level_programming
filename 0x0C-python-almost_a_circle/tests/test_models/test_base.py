#!/usr/bin/python3
"""Unitest module"""

import json
import unittest
from models.base import Base
from  models.rectangle import Rectangle

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

    def test_json(self):
      """test converting from or to json string"""
      self.assertEqual(Base.to_json_string(None), "[]")
      self.assertEqual(Base.to_json_string([]), "[]")
      self.assertEqual(Base.from_json_string(None), [])
      self.assertEqual(Base.from_json_string("[]"), [])
      self.assertEqual(Base.from_json_string('[{"id" : 89}]'), [{"id" : 89}])
        

if __name__ == '__main__':
    unittest.main()

