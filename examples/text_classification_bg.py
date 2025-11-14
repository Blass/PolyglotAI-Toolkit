"""
Проста правилна (rule-based) класификация на настроение на български.
Simple rule-based sentiment classification demo (Bulgarian).
"""

from utils.preprocess import clean_text


POSITIVE_WORDS_BG = {
    "добър", "страхотен", "чудесен", "прекрасен", "щастлив", "обичам",
    "фантастичен", "готин", "позитивен"
}

NEGATIVE_WORDS_BG = {
    "лош", "ужасен", "отвратителен", "мразя", "тъжен", "ядосан",
    "негативен", "по-лош", "най-лош"
}


def classify_sentiment_bg(text: str) -> str:
    """
    Много наивен класификатор на настроение, базиран на ключови думи.
    Very naive sentiment classifier based on keyword counts.
    """
    cleaned = clean_text(text, lang="bg")
    tokens = cleaned.split()

    score = 0
    for t in tokens:
        if t in POSITIVE_WORDS_BG:
            score += 1
        if t in NEGATIVE_WORDS_BG:
            score -= 1

    if score > 0:
        return "позитивно"
    elif score < 0:
        return "негативно"
    else:
        return "неутрално"


if __name__ == "__main__":
    examples = [
        "Изкуственият интелект е страхотен и много полезен.",
        "Този модел е ужасен и мразя резултатите.",
        "Системата работи."
    ]

    for text in examples:
        label = classify_sentiment_bg(text)
        print(f"Текст: {text}\n → Настроение: {label}\n")
