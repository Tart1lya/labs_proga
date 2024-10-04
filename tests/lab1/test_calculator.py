import unittest
from src.lab1.calculator import *
class CalculatorTestCase(unittest.TestCase):

    #Sum test
    def test_sum(self):
        self.assertEqual(make_sum(2, 2), 4)
        self.assertEqual(make_sum(-1, 1), 0)
        self.assertEqual(make_sum(-1, 2), 1)
        self.assertEqual(make_sum(-1, -2), -3)
        self.assertEqual(make_sum(0.5, 2), 2.5)
        self.assertEqual(make_sum(-0.5, -2), -2.5)
        self.assertEqual(make_sum(-0.5, 2), 1.5)

    #Difference test
    def test_difference(self):
        self.assertEqual(make_difference(2, 4), -2)
        self.assertEqual(make_difference(4, 4), 0)
        self.assertEqual(make_difference(5, 4), 1)
        self.assertEqual(make_difference(5, -2), 7)
        self.assertEqual(make_difference(-5, -2), -3)
        self.assertEqual(make_difference(-5.5, -2), -3.5)
        self.assertEqual(make_difference(5.5, -2), 7.5)

    #Product test
    def test_product(self):
        self.assertEqual(make_product(2.5, 2), 5)
        self.assertEqual(make_product(2.5, 3), 7.5)
        self.assertEqual(make_product(5, 5), 25)
        self.assertEqual(make_product(5, 1), 5)
        self.assertEqual(make_product(5, 0), 0)
        self.assertEqual(make_product(0, 0), 0)
        self.assertEqual(make_product(-5, 1), -5)
        self.assertEqual(make_product(-5, -1), 5)
        self.assertEqual(make_product(2.5, -3.5), -8.75)

    #Division test
    def test_quotient(self):
        self.assertEqual(make_quotient(6, 2), 3)
        self.assertEqual(make_quotient(5, 2), 2.5)
        self.assertEqual(make_quotient(5, 5), 1)
        self.assertEqual(make_quotient(-5, 2), -2.5)
        self.assertEqual(make_quotient(-5, -2), 2.5)
        self.assertEqual(make_quotient(5, 2.5), 2)
        self.assertEqual(make_quotient(5, -2), -2.5)

    #Degree test
    def test_pow(self):
        self.assertEqual(make_pow(2, 2), 4)
        self.assertEqual(make_pow(4, 2), 16)
        self.assertEqual(make_pow(-5, 2), 25)
        self.assertEqual(make_pow(-5, -2), 1/25)
        self.assertEqual(make_pow(5, -2), 1/25)
        self.assertEqual(make_pow(3, 1), 3)
        self.assertEqual(make_pow(3, 0), 1)
        self.assertEqual(make_pow(2, 3), 8)
        self.assertEqual(make_pow(-2, 3), -8)
        self.assertEqual(make_pow(-2.5, 2), 6.25)
        self.assertEqual(make_pow(-2.5, -3), -0.064)
        self.assertEqual(make_pow(-2.5, 3), -15.625)