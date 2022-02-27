import unittest
from password_check import *


class MyTests(unittest.TestCase):

    def test_check_password(self):
        self.assertEqual(check_password('11A_Good_Password*(_'), True, 'True because spec char, upper case, and '
                                                                       'num in pass.')
        self.assertEqual(check_password('A_Good_Password1234'), True)
        self.assertEqual(check_password('A_Good_Password*(_'), False, 'False because no num')
        self.assertEqual(check_password('aG00dpass'), False, 'False because no spec char')
        self.assertEqual(check_password('this_password_good01'), False, 'False because no upper')
        self.assertEqual(check_password('!isNot7'), False, 'False because not len of > 7')
        self.assertEqual(check_password(''), False, 'False because empty')
        self.assertEqual(check_password('ferbmannnn'), False)
        self.assertEqual(check_password('131619331'), False)
        self.assertEqual(check_password('AGood_P4ss'), True)
        self.assertEqual(check_password('ds'), False)
        self.assertEqual(check_password('000000000000'), False)
        self.assertEqual(check_password('dsa00000'), False)
        self.assertEqual(check_password("aaaaaaaaa‘这时候能与"), False)

    def test_check_requirement(self):
        self.assertEqual(check_requirement_pass('11A_Good_Password*(_'), True)
        self.assertEqual(check_requirement_pass('Sarah 2004 My Password'), True)
        self.assertEqual(check_requirement_pass('this lacks upper 123_'), False)
        self.assertEqual(check_requirement_pass('This lacks numbers_'), False)
        self.assertEqual(check_requirement_pass('This lacks SP3C1AL NUM'), True, 'Because space is spec char')
        self.assertEqual(check_requirement_pass('9D*'), True,
                         'True because special char, num, and upper case is available')
        self.assertEqual(check_requirement_pass('hello'), False, 'Should return True if met requirement')
        self.assertEqual(check_requirement_pass('Hello'), False, 'Should return True if met requirement')
        self.assertEqual(check_requirement_pass('8*'), False, 'Lacks uppercase')
        self.assertEqual(check_requirement_pass('+./?!'), False, 'Should return True if met requirement')
        self.assertEqual(check_requirement_pass('A_Good_Password*(_'), False, 'Lacks numeric')
        self.assertEqual(check_requirement_pass('12345678'), False)

    def test_check_ascii(self):
        self.assertEqual(check_ascii('è'), False, "Is not Ascii")

    def test_check_chars(self):
        self.assertEqual(check_chars('321431'), False, "There are less than 4 alphabets.")
        self.assertEqual(check_chars('asd111'), False, "There are less than 4 alphabets.")
        self.assertEqual(check_chars('eqe3432'), False, "There are less than 4 alphabets.")
        self.assertEqual(check_chars('000000'), False, "There are less than 4 alphabets.")
        self.assertEqual(check_chars('32-4089'), False, "There are less than 4 alphabets.")
        self.assertEqual(check_chars('GoodPassword'), True, "There are more than 4 alphabets.")
        self.assertEqual(check_chars('5chars'), True, "There are more than 4 alphabets.")
        self.assertEqual(check_chars('nothing'), True)
        self.assertEqual(check_chars('almo1234'), True)
        self.assertEqual(check_chars('almo12345'), False)  # This has 5 nums, not allowed.
        self.assertEqual(check_chars('almos123456'), False)
        self.assertEqual(check_chars('73281937164716942'), False)
        self.assertEqual(check_chars('yehe'), True)

    def test_check_requirement_pass(self):
        self.assertEqual(check_requirement_pass('A1_'), True)
        self.assertEqual(check_requirement_pass(' H3'), True)
        self.assertEqual(check_requirement_pass('random'), False)

    def test_check_len(self):
        self.assertEqual(check_len('Password Is 8'), True, 'Should return True if len above 8')
        self.assertEqual(check_len('A' * 6), False, 'Should return False if len below 8')
        self.assertEqual(check_len(''), False, 'Should return False if len below 8')
        self.assertEqual(check_len(' '), False, 'Should return False if len below 8')

    def test_check_spec_char(self):
        self.assertEqual(check_spec_char('*'), True, 'Should return True if has special character')
        self.assertEqual(check_spec_char(' '), True, 'Should return True if has special character')
        self.assertEqual(check_spec_char('h'), False, 'Should return True if has special character')
