from traslator import english_to_french
from traslator import french_to_english
import unittest
from deep_translator import MyMemoryTranslator

class TestTraslation(unittest.TestCase):
    def test_englishToFrench(self):
        english_text = "Hello"
        text_expected = "Bonjour"
        text_traslated = english_to_french(english_text)
        self.assertEqual(text_traslated,text_expected)

    def test_englishToFrench2(self):
       english_text = "Thank you"
       text_expected = "Merci"
       text_traslated = english_to_french(english_text)
       self.assertEqual(text_traslated,text_expected)
    
    def test_frenchToEnglish(self):
        french_text = "Bonjour"
        text_expected = "Hello"
        text_traslated = french_to_english(french_text)
        self.assertEqual(text_traslated,text_expected)

    def test_frenchToEnglish2(self):
        french_text = "Merci"
        text_expected = "Thank you"
        text_traslated = french_to_english(french_text)
        self.assertEqual(text_traslated,text_expected)

if __name__ == '__main__':
    unittest.main()