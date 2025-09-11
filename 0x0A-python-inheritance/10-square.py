#!/usr/bin/python3
"""Square class module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The Square class that inherits Recatangle"""

    def __init__(self, size):
        """Initializes square class
            Args:
            size :int
            self.__size = size
        """
        # here I can't call with super cause it is not in parent
        # we can call it also with base_gemotery.
        
        self.integer_validator("size",  size)
        super().__init__(size, size)
        self.__size = size
        

