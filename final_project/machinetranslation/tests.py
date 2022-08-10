from translator import english_to_french,french_to_english

import unittest

class testEnFr(unittest.TestCase):
    def test_Eng_Fr(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('My Dog'),'Mon chien')
        self.assertEqual(english_to_french(' '),'Empty')

class testFrEn(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Mon chien'),'My Dog')
        self.assertEqual(french_to_english(''),'Empty')

unittest.main()