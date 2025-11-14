"""
Simple rule-based sentiment classification demo (English).
Демо за проста правилна (rule-based) класификация на настроение (английски).
"""

from utils.preprocess import clean_text


POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "awesome", "happy", "love",
    "fantastic", "cool", "positive", "wonderful"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "hate", "horrible", "sad", "angry",
    "negative", "worse", "worst"
}


def classify_sentiment(text: str) -> str:
    """
    Very naive sentiment classifier based on keyword counts.
    Много наивен класификатор на настроение, базиран на ключови думи.
    """
    cleaned = clean_text(text, lang="en")
    tokens = cleaned.split()

    score = 0
    for t in tokens:
        if t in POSITIVE_WORDS:
            score += 1
        if t in NEGATIVE_WORDS:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


if __name__ == "__main__":
    examples = [
        "AI is amazing and super helpful for many tasks.",
        "This model is terrible and I hate the results.",
        "The system works."
    ]

    for text in examples:
        label = classify_sentiment(text)
        print(f"Text: {text}\n → Sentiment: {label}\n")
