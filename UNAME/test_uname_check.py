import unittest
from uname_check import *


class MyTests(unittest.TestCase):
    def test_check_password(self):
        self.assertEqual(check_username('!Good02'), True, 'True because spec char, upper case, and '
                                                          'num in pass.')
        self.assertEqual(check_username('I am (troll)'), False)
        self.assertEqual(check_username(''), False, 'False because not len of > 5')
        self.assertEqual(check_username('troll'), False, 'False because not len of > 5')
        self.assertEqual(check_username('this_username_good01'), False, 'False because no upper')
        self.assertEqual(check_username('01:sarah'), False, 'False because no upper')
        self.assertEqual(check_username('I-Like_Turtles'), False, 'False because no num')
        self.assertEqual(check_username('_Sarah_God:'), False, 'False because no num')
        self.assertEqual(check_username('[Hehehehehe]'), False, 'False because special char invalid')
        self.assertEqual(check_username('{TrollThis}'), False, 'False because special char invalid')
        self.assertEqual(check_username('ThisIsAlsoATroll<>'), False, 'False because special char invalid')
        self.assertEqual(check_username('Escaping is my hobby\\'), False, 'False because special char invalid')

    # def test_check_if_spec_char_dangerous(self):
    #     self.assertEqual(check_if_spec_char_dangerous('Sarah?()'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('?Sarah'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('(A_Good_Password1234)'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('{A_Good_Password1234}'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('[A_Good_Password1234]'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('<A good Password>'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('A_Good_Password1234|'), True)
    #     self.assertEqual(check_if_spec_char_dangerous('Checkout\\'), True)
