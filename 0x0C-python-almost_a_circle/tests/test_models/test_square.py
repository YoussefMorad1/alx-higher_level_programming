#!/usr/bin/python3
"""Module Test of Square
"""
from models.square import Square
import unittest

class Test(unittest.TestCase):
    """Test Square Class
    """
    def test_constructor(self):
        """Test constructor of Square and
        check it initalizes its parent
        """
        sq1 = Square(5, 0, 0, 100)
        self.assertEqual(sq1.id, 100)
        self.assertEqual(sq1.width, 5)
        self.assertEqual(sq1.height, 5)
        self.assertEqual(sq1.size, 5)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)
        self.assertEqual(sq1.__str__(), '[Square] (100) 0/0 - 5')
        self.assertEqual(sq1.area(), 25)

        sq1 = Square(7)
        self.assertEqual(sq1.width, 7)
        self.assertEqual(sq1.height, 7)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)

        sq1.size = 8
        self.assertEqual(sq1.size, 8)
        self.assertEqual(sq1.width, 8)
        self.assertEqual(sq1.height, 8)

    
    def test_update_args(self):
        r1 = Square(10, 10, 10, 10)

        rep = r1.__str__()
        r1.update()
        self.assertEqual(rep, r1.__str__())

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)

    def test_upddate_kwargs(self):
        r1 = Square(10, 10, 10, 10)

        r1.update(id=1)
        self.assertEqual(r1.id, 1)
        
        r1.update(size=12)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 12)
        self.assertEqual(r1.size, 12)

        r1.update(x=12)
        self.assertEqual(r1.x, 12)

        r1.update(y=12)
        self.assertEqual(r1.y, 12)
    

    def test_to_dictionary(self):
        r1 = Square(1, 2, 4, 5)
        self.assertEqual(sorted(r1.to_dictionary()), sorted({'id': 5, 'size': 1, 'x': 2, 'y': 4}))
