#!/usr/bin/python3
"""Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor
        """
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        attributes = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in attributes:
                    setattr(self, key, val)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'


    def to_dictionary(self):
        attributes = ['id', 'size', 'x', 'y']
        dic = {}
        for att in attributes:
            dic[att] = getattr(self, att)
        return dic
