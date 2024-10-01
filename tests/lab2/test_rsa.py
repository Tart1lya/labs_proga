import unittest
from src.lab2.rsa import *


class CalculatorTestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(8), False)

