#!/usr/bin/python3
"""test max_integer module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """test max_integer function
    """
    def test_basic(self):
        self.assertEqual(max_integer([5, 2, 1]), 5)
        self.assertEqual(max_integer([1, 2, 5]), 5)
        self.assertEqual(max_integer([1, 5, 2]), 5)
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, 3, -2]), 3)

    def test_wrong_input(self):
        pass
