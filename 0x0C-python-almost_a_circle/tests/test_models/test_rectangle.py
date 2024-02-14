#!/usr/bin/python3
"""Unitest module"""

import unittest

from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    """Defines Rectangle class test cases"""

    def test_id(self):
        """test different cases for id """
        R1 = Rectangle(10, 4)
        R2 = Rectangle(10, 2, 0, 0, 12)
        R3 = Rectangle(2, 10)
        self.assertEqual(R3.id, R1.id + 1)
        self.assertEqual(R2.id, 12)

    def test_att(self):
        """Tests diff attributes """
        R = Rectangle(12,10)
        with self.assertRaises(TypeError):
            R_arg = Rectangle()
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__height)               
        R.width = 14    
        self.assertEqual(R.width, 14)    


    def test_types(self):
        """Tests different value types of rect object Args"""
        Rect = Rectangle(10, 6)
        with self.assertRaises(TypeError):
            Rectangle(10,"x")
        
        with self.assertRaises(ValueError):
            Rect.height = 0

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 10)

        with self.assertRaises(TypeError):
            Rect.height = "t"

        with self.assertRaises(TypeError):
            Rectangle(10, 20, None, 5)

        with self.assertRaises(ValueError):
            Rect.x = -1

        with self.assertRaises(TypeError):
            Rect.x = "x"
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "y")

        with self.assertRaises(TypeError):
            Rect.y = "y"    
        with self.assertRaises(ValueError):
            Rect.y = -5     

if __name__ == '__main__':
    unittest.main()
