#!/usr/bin/python3
"""
test the base.py file
"""
import unittest
from models.base import Base


class Test(unittest.TestCase):
    """Test Class for base class"""
    def test_ids(self):
        self.base = Base()
        self.assertEqual(self.base.id, 1)

        self.base2 = Base()
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base.id, 1)

        self.base = Base(3)
        self.assertEqual(self.base.id, 3)

        self.base2 = Base(300)
        self.assertEqual(self.base2.id, 300)

        self.base = Base()
        self.assertEqual(self.base.id, 3)
