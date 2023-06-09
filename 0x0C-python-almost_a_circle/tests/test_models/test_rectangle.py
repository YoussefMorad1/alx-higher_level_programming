#!/usr/bin/python
"""Module to test Rectangle Class"""
import unittest
from models.rectangle import Rectangle


class Test(unittest.TestCase):
    def test_good_values(self):
        rec1 = Rectangle(2, 5, 1, 3, 7)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 5)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 3)
        self.assertEqual(rec1.id, 7)

        rec1 = Rectangle(2, 5, id=8)
        self.assertEqual(rec1.id, 8)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)

        rec1 = Rectangle(2, 4, id=9, x=1)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 0)

        rec1 = Rectangle(2, 4, 0, 0, 10)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)

    def test_auto_id(self):
        rec1 = Rectangle(2, 5, 1, 3)
        rec2 = Rectangle(2, 5)
        self.assertTrue(rec2.id > rec1.id)

    def test_bad_values_width_height(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle('hello', 2)
        with self.assertRaises(TypeError):
            rec1 = Rectangle(2, 'hello')

        with self.assertRaises(ValueError):
            rec1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rec1 = Rectangle(2, 0)

        with self.assertRaises(ValueError):
            rec1 = Rectangle(-2, 2)
        with self.assertRaises(ValueError):
            rec1 = Rectangle(2, -5)

    def test_bad_values_x_y(self):
        with self.assertRaises(TypeError):
            rec1 = Rectangle(2, 2, 'hi', 3)
        with self.assertRaises(TypeError):
            rec1 = Rectangle(2, 2, 3, 'hi')

        with self.assertRaises(ValueError):
            rec1 = Rectangle(0, 2, -1, 2)
        with self.assertRaises(ValueError):
            rec1 = Rectangle(2, 0, 2, -1)

    def test_area(self):
        self.assertEqual(50, Rectangle(5, 10, 0, 0, 7).area())
        self.assertEqual(2, Rectangle(2, 1, 4, 5).area())
        self.assertEqual(49, Rectangle(7, 7, 4).area())
        self.assertEqual(44, Rectangle(4, 11).area())

    def test_str(self):
        self.assertEqual('[Rectangle] (12) 2/1 - 4/6',
                         Rectangle(4, 6, 2, 1, 12).__str__())

        rec1 = Rectangle(5, 5, 1)
        self.assertEqual(f'[Rectangle] ({rec1.id}) 1/0 - 5/5', rec1.__str__())

    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)

        rep = r1.__str__()
        r1.update()
        self.assertEqual(rep, r1.__str__())

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_upddate_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(id=1)
        self.assertEqual(r1.id, 1)
        
        r1.update(width=12)
        self.assertEqual(r1.width, 12)

        r1.update(height=12)
        self.assertEqual(r1.height, 12)
        
        r1.update(x=12)
        self.assertEqual(r1.x, 12)

        r1.update(y=12)
        self.assertEqual(r1.y, 12)

        r1.update(id=2, width=3, x=5)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.x, 5)

    def test_update_wrong_input(self):
        r1 = Rectangle(89, 2, 3, 4, 5)
        
        with self.assertRaises(TypeError):
            r1.update(89, 2, 'height')
        with self.assertRaises(TypeError):
            r1.update(89, 'width')
        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, 'x')
        with self.assertRaises(TypeError):
            r1.update(89, 2, 3, 0, 'y')


        with self.assertRaises(TypeError):
            r1.update(height='height')
        with self.assertRaises(TypeError):
            r1.update(width='width')
        with self.assertRaises(TypeError):
            r1.update(x='x')
        with self.assertRaises(TypeError):
            r1.update(y='y')

        with self.assertRaises(ValueError):
            r1.update(98, -1)
        with self.assertRaises(ValueError):
            r1.update(98, 2, -1)
        with self.assertRaises(ValueError):
            r1.update(98, 2, 3, -1)
        with self.assertRaises(ValueError):
            r1.update(98, 2, 3, 4, -1)


        with self.assertRaises(ValueError):
            r1.update(width=-1)
        with self.assertRaises(ValueError):
            r1.update(height=-1)
        with self.assertRaises(ValueError):
            r1.update(x=-1)
        with self.assertRaises(ValueError):
            r1.update(y=-1)

    def test_to_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(sorted(r1.to_dictionary()), sorted({'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}))
