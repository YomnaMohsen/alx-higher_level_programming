#!/usr/bin/python3
"""Square class"""


class Square:
    """This class defines a square shape"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object.
        Args:
            size (int): set square size
            poistion (int, int): poistion of square

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return size"""
        return self.__size

    @property
    def position(self):
        """Return poistion"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """set poistion"""
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(num, int) and num >= 0 for num in value):
                self.__position = value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints square number of size #"""
        if (self.size == 0):
            print("")
            return
        print(("\n" * self.position[1]) +
              ((" " * self.position[0]) +
               ("#" * self.size + "\n")) * self.size, end="")
        [print("") for i in range(self.position[1])]
        for j in range(self.size):
            [print(" ", end="") for k in range(self.position[0])]
            [print("#", end="") for h in range(self.size)]
            print()
s = Square()
print(s.si)
s.size ="a"