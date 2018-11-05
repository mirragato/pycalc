import unittest
from pycalc import Validator


class TestValidator(unittest.TestCase):

    def test_combine_operator(self):
        self.assertEqual("-1", Validator.combine_operator("------+-1"))
        
    def test_split(self):
        self.assertEqual([4, "-", 4], Validator.split("4-4"))
