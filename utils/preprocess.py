"""
Text preprocessing utilities for PolyglotAI Toolkit.
Подготвящи инструменти за текст за PolyglotAI Toolkit.
"""

import re
from typing import List


EN_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "of", "in", "on", "at", "to", "for",
    "is", "are", "was", "were", "be", "been", "am", "it", "this", "that"
}

BG_STOPWORDS = {
    "и", "в", "на", "за", "с", "по", "от", "до", "е", "са", "беше", "като",
    "това", "този", "тази", "онзи"
}


def normalize_whitespace(text: str) -> str:
    """
    Collapse multiple spaces and newlines into single spaces.
    Нормализира интервалите и новите редове.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return re.sub(r"\s+", " ", text).strip()


def basic_clean(text: str) -> str:
    """
    Lowercase and remove most punctuation (keeps letters and numbers).
    Малки букви и премахване на пунктуация.
    """
    text = normalize_whitespace(text)
    text = text.lower()
    text = re.sub(r"[^0-9a-zа-яёА-ЯЁіїщьъçğşöüЩЪЧчЮюЯя .,!?\-']", " ", text)
    return normalize_whitespace(text)


def tokenize(text: str) -> List[str]:
    """
    Split text into tokens by whitespace.
    Разделя текста на токени по интервали.
    """
    text = normalize_whitespace(text)
    if not text:
        return []
    return text.split(" ")


def remove_stopwords(tokens: List[str], lang: str = "en") -> List[str]:
    """
    Remove stopwords for a given language ('en' or 'bg').
    Премахва стоп думи за даден език ('en' или 'bg').
    """
    if lang == "en":
        stopwords = EN_STOPWORDS
    elif lang == "bg":
        stopwords = BG_STOPWORDS
    else:
        raise ValueError("Unsupported language, use 'en' or 'bg'")

    return [t for t in tokens if t not in stopwords]


def clean_text(text: str, lang: str = "en") -> str:
    """
    Full cleaning pipeline: normalize, lowercase, remove punctuation, remove stopwords.
    Пълен процес: нормализиране, малки букви, без пунктуация, без стоп думи.
    """
    cleaned = basic_clean(text)
    tokens = tokenize(cleaned)
    tokens = remove_stopwords(tokens, lang=lang)
    return " ".join(tokens)
