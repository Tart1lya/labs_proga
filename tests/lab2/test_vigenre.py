import unittest
from src.lab2.vigenre import *
class VigenreTestCase(unittest.TestCase):

    #Шифрование
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(encrypt_vigenere('python', 'a'), 'python')
        self.assertEqual(encrypt_vigenere('ATTACKATDAWN', 'LEMON'), 'LXFOPVEFRNHR')
    #Расшифровка
    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(decrypt_vigenere('python', 'a'), 'python')
        self.assertEqual(decrypt_vigenere('LXFOPVEFRNHR', 'LEMON'), 'ATTACKATDAWN')
