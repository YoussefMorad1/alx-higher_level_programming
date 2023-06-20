#!/usr/bin/python3
"""
test the base.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test(unittest.TestCase):
    """Test Class for base class"""
    def test_ids(self):
#        self.base = Base()
#        self.assertEqual(self.base.id, 1)

#       self.base2 = Base()
#       self.assertEqual(self.base2.id, 2)
#        self.assertEqual(self.base.id, 1)

        self.base = Base(3)
        self.assertEqual(self.base.id, 4)

        self.base2 = Base(300)
        self.assertEqual(self.base2.id, 300)

#        self.base = Base()
#        self.assertEqual(self.base.id, 3)

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
    
    def test_from_json_string(self):
        jsonstr = '[{"hi": 1, "bye": "try", "22": "jo"}]'
        self.assertEqual(Base.from_json_string(jsonstr),
                         [{'hi': 1, 'bye': 'try', '22': 'jo'}])
        jsonstr = '[{"1": "2"}, {"2": "3"}]'
        self.assertEqual(Base.from_json_string(jsonstr),
                         [{'1': '2'}, {'2': '3'}])
        jsonstr = None
        self.assertEqual(Base.from_json_string(jsonstr), [])
        jsonstr = '[]'
        self.assertEqual(Base.from_json_string(jsonstr), [])

    def test_save_to_file(self):
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

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 0)
        self.assertTrue(r1 is not r2)
        self.assertTrue(r1 != r2)


        r1 = Square(5, 0, 2)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.size, 5)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 2)
        self.assertTrue(r1 is not r2)
        self.assertTrue(r1 != r2)

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_rectangles_input[i].__str__(),
                        list_rectangles_output[i].__str__())

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_squares_input[i].__str__(),
                             list_squares_output[i].__str__())

