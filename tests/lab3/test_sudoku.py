import unittest
from src.lab3.sudoku import *
class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1,2,3,4,5,6], 2), [[1,2], [3,4], [5,6]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6], 1), [[1], [2], [3], [4], [5], [6]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8], 4), [[1, 2, 3, 4], [5, 6, 7, 8]])