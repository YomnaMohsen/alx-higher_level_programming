#!/usr/bin/python3
"""Unitest module"""

import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    """Defines Rectangle class test cases"""

    def test_id(self):
        """test different cases for id """
        R1 = Rectangle(10, 2)
        R2 = Rectangle(10, 2, 0, 0, 12)
        R3 = Rectangle(2, 10)
        R4 = Rectangle(14, 10)
        self.assertEqual(R1.id, 1)
        self.assertEqual(R2.id, 12)
        self.assertEqual(R3.id, 2)
        self.assertEqual(R4.width, 14)
        self.assertEqual(R4.id, 3)

    #def test_att(self):
     #   """Tests diff attributes"""
      #  R = Rectangle(10,2,1,2,0)
       # self.assertEqual(R.x, R.y, R.id, 1, 2, 0) 


    def test_types(self):
        """Tests different value types of rect object Args"""
       
        with self.assertRaises(TypeError):
            Rectangle(10)    
        with self.assertRaises(AttributeError):
            print(Rectangle(10,2).__width)
              

        
         

if __name__ == '__main__':
    unittest.main()

