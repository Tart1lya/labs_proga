import unittest
from src.lab3.sudoku import *
class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1,2,3,4,5,6], 2), [[1,2], [3,4], [5,6]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6], 1), [[1], [2], [3], [4], [5], [6]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8], 4), [[1, 2, 3, 4], [5, 6, 7, 8]])

    def test_get_row(self):
        self.assertEqual(get_row([['1','2','3'], ['4','5','6']], (0,0)), ['1', '2', '3'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], (2, 0)), ['7', '8', '9'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6']], (1, 0)), ['4', '5', '6'])

    def test_get_col(self):
        self.assertEqual(get_col([['1','2','3'], ['4','5','6']], (0,0)), ['1', '4'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6']], (0, 1)), ['2', '5'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6']], (0, 2)), ['3', '6'])

'''
    def test_get_block(self):
        self.assertEqual(get_block(read_sudoku('src/lab3/puzzle1.txt'), (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
'''
