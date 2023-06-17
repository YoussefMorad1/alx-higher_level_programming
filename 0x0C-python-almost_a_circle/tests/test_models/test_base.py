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

    def test_to_json_string(self):
        dic = {'hi': 1, 'bye': 'try', '22': 'jo'}
        self.assertEqual(Base.to_json_string([dic]),
                         '[{"hi": 1, "bye": "try", "22": "jo"}]')
        dic = [{'1': '2'}, {'2': '3'}]
        self.assertEqual(Base.to_json_string(dic), '[{"1": "2"}, {"2": "3"}]')
        dic = None
        self.assertEqual(Base.to_json_string(dic), '[]')
        dic = []
        self.assertEqual(Base.to_json_string(dic), '[]')

    def test_save_to_file(self):
        Rectangle = __import__('models').rectangle.Rectangle
        import json
        import os
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.loads(file.read()),
                             json.loads('[{"y": 8, "x": 2, "id": 1 '
                             + ', "width": 10, "height": 7}, {"y": 0, "x": 0, '
                             + '"id": 2, "width": 2, "height": 4}]'))
            os.remove("Rectangle.json")
