
import unittest
from translator import french_to_english, english_to_french


class TestTranslateEnToFr(unittest.TestCase):
    def test_null(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
    def test_equal(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_noequal(self):
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

class TestTranslateFrToEn(unittest.TestCase):
    def test_null(self):
        with self.assertRaises(ValueError):
            french_to_english(None)
    def test_equal(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_noequal(self):
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")


unittest.main()