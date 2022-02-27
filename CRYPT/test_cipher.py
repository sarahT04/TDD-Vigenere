import unittest

from cipher_vigenere import *


class MyTests(unittest.TestCase):

    def test_key_repeater(self):
        self.assertEqual(key_repeater(len('I AM GROOT'), 'KEY'), 'KEYKEYKEYK')
        self.assertEqual(key_repeater(len('THIS IS LEN OF 13'), 'HI'), 'HIHIHIHIHIHIHIHIH')
        self.assertEqual(key_repeater(len(str(2925845)), 'qwerty'), 'qwertyq')
        self.assertEqual(key_repeater(len('smol'), 'SOMEKEY'), 'SOME')

    def test_cipher_text(self):
        key = 'MGS'
        self.assertEqual(cipher_text('I like turtles', key), 'U duqw zmdzdqy')
        self.assertEqual(cipher_text('snake eater', key), 'etswk qglqx')
        self.assertEqual(cipher_text('VHASCOMETO', key), 'HNSEIGYKLA')
        self.assertEqual(cipher_text('wHaT a TrILl', key), 'iNsF s ZjURd')
        self.assertEqual(cipher_text('ThisisR34lPassword_', key), 'FnaeokD2128xVseyoaxv_')
        self.assertEqual(cipher_text('0000+_', 'POPOPO'), '0000+_')

    def test_decipher_text(self):
        key = 'MGS'
        self.assertEqual(decrypt_cipher('FnaeokD282828rHmykiujp', key), 'ThisisR444lPassword')
        self.assertEqual(decrypt_cipher('FnaeokD___rHmykiujp', key), 'ThisisR___lPassword')
        self.assertEqual(decrypt_cipher('.Ysdgz:140028.', key), '.Sarah:2004.')
        self.assertEqual(decrypt_cipher('.Ysdgz:0.', key), '.Sarah:0.')
        self.assertEqual(decrypt_cipher('E7eb', key), 'S1mp')
        self.assertEqual(decrypt_cipher('YgfkFwduk00700700', key), 'ManyZeros00100100')
        self.assertEqual(decrypt_cipher('rkogox5663oilf-+kmjv-7^*56634921', key), 'fewuif89wwfn-+sadd-1^*8973')
        self.assertEqual(decrypt_cipher('M daz al Lkjay mtv Ufqy 070700000700707070000', key),
                         'A lot of Zeros and Ones 010100000100101010000')
