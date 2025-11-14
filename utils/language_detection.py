"""
Very simple heuristic-based language detection for English vs Bulgarian.
Много проста детекция на език между английски и български.
"""

from typing import Literal


LanguageCode = Literal["en", "bg"]


def detect_language(text: str) -> LanguageCode:
    """
    Detect language based on presence of Cyrillic vs Latin characters
    and a few keywords. Not production ready, just a demo.

    Открива езика според наличие на кирилица или латиница и няколко ключови думи.
    Не е за продукция, само демо.
    """
    if not text:
        return "en"

    has_cyrillic = any("а" <= ch.lower() <= "я" for ch in text if ch.isalpha())
    has_latin = any("a" <= ch.lower() <= "z" for ch in text if ch.isalpha())

    if has_cyrillic and not has_latin:
        return "bg"
    if has_latin and not has_cyrillic:
        return "en"

    # Mixed: use small keyword-based heuristic
    bg_keywords = {"здравей", "изкуствен", "интелект", "технологии", "бъдеще"}
    en_keywords = {"hello", "ai", "intelligence", "technology", "future"}

    text_low = text.lower()
    if any(k in text_low for k in bg_keywords):
        return "bg"
    if any(k in text_low for k in en_keywords):
        return "en"

    # Fallback
    return "en"
