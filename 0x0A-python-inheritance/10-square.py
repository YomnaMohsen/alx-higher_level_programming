#!/usr/bin/python3
"""Square class module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The Square class that inherits Recatangle"""

    def __init__(self, size):
        """Initializes square class
            Args:
            size :int
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
