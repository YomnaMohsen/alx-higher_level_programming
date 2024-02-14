#!/usr/bin/python3
"""Unitest module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Rectangle_ِArgs(unittest.TestCase):
    """Defines Rectangle class test cases"""

    def test_args(self):
        """test different cases for args """
        R2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, R2.id)
        with self.assertRaises(AttributeError):
            print(R2.__width)        

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

        with self.assertRaises(ValueError):
            Rectangle(0, 10)       
       
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

        with self.assertRaises(ValueError):
            Rectangle(11, 0)      

        
    def test_x(self):
        """Tests x attribute"""
        R = Rectangle(10, 11, 12, 13)
        self.assertEqual(R.x, 12)

        R.x = 9
        self.assertEqual(R.x, 9)

        with self.assertRaises(TypeError):
            R1 = Rectangle(10, 11, "y", 13)

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

class Test_Rectangle_methods(unittest.TestCase):
    def test_area(self):
        R = Rectangle(10, 20)
        self.assertEqual(R.area(), 200)
        
        with self.assertRaises(ValueError):
            Rectangle(-10, 20).area()


if __name__ == '__main__':
    unittest.main()
