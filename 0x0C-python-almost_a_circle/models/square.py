#!/usr/bin/python3
"""
square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialising square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """overriding str method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """update attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns a dictionary representation of
        a square
        """
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
