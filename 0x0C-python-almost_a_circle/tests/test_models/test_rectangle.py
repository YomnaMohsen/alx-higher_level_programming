#!/usr/bin/python3
"""Unitest module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Rectangle_ِArgs(unittest.TestCase):
    """Defines Rectangle class test cases"""

    def test_id(self):
        """test different cases for id """
        R1 = Rectangle(10, 4)
        R2 = Rectangle(1, 2, 3, 4, 5)
        R3 = Rectangle(2, 10)
        self.assertEqual(2, R2.height)
        self.assertEqual(R3.id, R1.id + 1)
        with self.assertRaises(TypeError):
            R_arg = Rectangle()
        with self.assertRaises(AttributeError):
            print(R1.__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__height)        

    def test_width(self):
        """Tests width attribute """
        R = Rectangle(12,10)
        self.assertEqual(R.width, 12)

        R.width = 14    
        self.assertEqual(R.width, 14)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 3)

        with self.assertRaises(TypeError):
            Rectangle("e", 2)   
       
    def test_height(self):
        """Tests height attribute"""
        Rect = Rectangle(10, 6)
        self.assertEqual(Rect.height, 6)

        Rect.height = 8
        self.assertEqual(Rect.height, 8)

        with self.assertRaises(TypeError):
            Rectangle(10,"x")
            
        
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

        
    def test_x(self):
        """Tests x attribute"""
        R = Rectangle(10, 11, 12, 13)
        self.assertEqual(R.x, 12)

        R.x = 9
        self.assertEqual(R.x, 9)

        with self.assertRaises(TypeError):
            R.x = []
        with self.assertRaises(TypeError):
            R1 = Rectangle(10, 11, "y", 13)
        with self.assertRaises(TypeError):
            R2 = Rectangle(10, 11, [1, 2, 3])

        with self.assertRaises(TypeError):
            Rectangle(10, 11, {})
        with self.assertRaises(ValueError):
            Rectangle(10, 11, -2)          

    def test_y(self):
        """Tests y attribute"""
        R = Rectangle(1, 11, 21, 31)
        self.assertEqual(R.y, 31)

        R.y = 19
        self.assertEqual(R.y, 19)

        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "y")
   
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -4)     

if __name__ == '__main__':
    unittest.main()
