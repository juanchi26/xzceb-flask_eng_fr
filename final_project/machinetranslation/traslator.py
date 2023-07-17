"""
Módulo de traducción de inglés a francés y de francés a inglés.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Traduce texto de inglés a francés utilizando deep_translator.
    """
    french_text = MyMemoryTranslator(source="en-US", target="fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Traduce texto de francés a inglés utilizando deep_translator.
    """
    english_text = MyMemoryTranslator(source="fr-FR", target="english").translate(french_text)
    return english_text
