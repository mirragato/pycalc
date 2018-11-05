import unittest
from pycalc import Calc
from math import *


class TestCalc(unittest.TestCase):
    def test_plus(self):
        result = Calc.calculate("1+1")
        self.assertEqual(result, 2)

    def test_simple(self):
        self.assertEqual(-13, Calc.calculate("-13"))
        self.assertEqual(19, Calc.calculate("6-(-13)"))
        self.assertEqual(0, Calc.calculate("1---1"))
        self.assertEqual(-1, Calc.calculate("-+---+-1"))

    def test_priority(self):
        self.assertEqual(5, Calc.calculate("1+2*2"))
        self.assertEqual(25, Calc.calculate("1+(2+3*2)*3"))
        self.assertEqual(30, Calc.calculate("10*(2+1)"))
        self.assertEqual(1000, Calc.calculate("10^(2+1)"))
        self.assertEqual(100 / 3 ** 2, Calc.calculate("100/3^2"))
        self.assertEqual(100 / 3 % 2 ** 2, Calc.calculate("100/3%2^2"))

    def test_one_arg(self):
        self.assertEqual(pi + e, Calc.calculate("pi+e"))
        self.assertEqual(1, Calc.calculate("log(e)"))
        self.assertEqual(1, Calc.calculate("sin(pi/2)"))
        self.assertEqual(2, Calc.calculate("log10(100)"))
        self.assertEqual(sin(pi / 2), Calc.calculate("sin(pi/2)"))
        self.assertEqual(2, Calc.calculate("2*sin(pi/2)"))
        self.assertEqual(102 % 12 % 7, Calc.calculate("102%12%7"))
        self.assertEqual(100 / 4 / 3, Calc.calculate("100/4/3"))
        self.assertEqual(2 ** 3 ** 4, Calc.calculate("2^3^4"))

    def test_comparison(self):
        self.assertEqual(1 + 2 * 3 == 1 + 2 * 3, Calc.calculate("1+2*3==1+2*3"))
        self.assertEqual(e ** 5 >= e ** 5 + 1, Calc.calculate("e^5>=e^5+1"))
        self.assertEqual(1 + 2 * 4 // 3 + 1 != 1 + 2 * 4 // 3 + 2, Calc.calculate("1+24/3+1!=1+24/3+2"))

    def test_common_tests(self):
        self.assertEqual(100, Calc.calculate("(100)"))
        self.assertEqual(666, Calc.calculate("666"))
        self.assertEqual(120, Calc.calculate("10(2+1)4"))
        self.assertEqual(-0.1, Calc.calculate("-.1"))
        self.assertEqual(1. / 3, Calc.calculate("1/3"))
        self.assertEqual(1.0 / 3.0, Calc.calculate("1.0/3.0"))
        self.assertEqual(.1 * 2.0 ** 56.0, Calc.calculate(".1 * 2.0^56.0"))
        self.assertEqual(e ** 34, Calc.calculate("e^34"))
        self.assertEqual((2.0 ** (pi / pi + e / e + 2.0 ** 0.0)), Calc.calculate("(2.0^(pi/pi+e/e+2.0^0.0))"))
        self.assertEqual((2.0 ** (pi / pi + 5)) ** (1.0 / 3.0), Calc.calculate("(2.0^(pi/pi+5))^(1.0/3.0)"))
        self.assertEqual(sin(cos(log10(43.0)))), Calc.calculate("sin(cos(log10(43.0))))")
        self.assertEqual(2.0 ** (2.0 ** 2.0 * 2.0 ** 2.0), Calc.calculate("2.0^(2.0^2.0*2.0^2.0)"))
