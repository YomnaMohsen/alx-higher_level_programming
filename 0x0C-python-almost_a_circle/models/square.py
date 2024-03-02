#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that inherits Recatangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square class
            Args:
            size :int
            x :int
            y :int
            id :int
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    def update(self, *args, **kwargs):
        """Updates square attributes"""
        if args and len(args) != 0:
            attr_list = ['id', 'size', 'x', 'y']
            for i in range(0, len(args)):
                setattr(self, attr_list[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary rep. of square object"""
        dict = {
            "id": self.id, "size": self.size,
            "x": self.x, "y": self.y}
        return dict
