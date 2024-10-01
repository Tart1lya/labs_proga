import unittest
from src.lab2.caesar import *
class CalculatorTestCase(unittest.TestCase):

    #Шифрование
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')
        self.assertEqual(encrypt_caesar('python'), 'sbwkrq')
        self.assertEqual(encrypt_caesar('Python3.6'), 'Sbwkrq3.6')
        self.assertEqual(encrypt_caesar(''), '')
    #Расшифровка
    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')
        self.assertEqual(decrypt_caesar('sbwkrq'), 'python')
        self.assertEqual(decrypt_caesar('Sbwkrq3.6'), 'Python3.6')
        self.assertEqual(decrypt_caesar(''), '')

