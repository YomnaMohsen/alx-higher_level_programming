#!/usr/bin/python3
"""Rectangle class Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes rectangle class
            Args:
            width :int
            height: int
            x, y, id:all are integers
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return width"""
        return self.__width

    @property
    def height(self):
        """Return height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x"""
        return self.__x

    @property
    def y(self):
        """Return y"""
        return self.__y

    @x.setter
    def x(self, value):
        """Set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.width * self.height

    def display(self):
        """display rectangle of #"""
        if self.height == 0 or self.width == 0:
            return ""
        s = (self.y * "\n") + (self.height) * (self.x * " " +
                                               "#" * self.width + "\n")
        print(s, end="")

    def __str__(self):
        """custom str fn"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height)

    def to_dictionary(self):
        """Return dictionary rep. of rectangle object"""
        dict = {
            "id": self.id, "width": self.width,
            "height": self.height, "x": self.x,
            "y": self.y
             }
        return dict

    def update(self, *args):
        """Updates rectangle attributes"""
        if args:
            attr_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(0, len(args)):
                setattr(self, attr_list[i], args[i])
