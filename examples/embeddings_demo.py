"""
Toy embeddings demo.

This file shows:
- how to create a very simple vector representation from text
- how to compute cosine similarity between sentences

Този файл показва:
- как да създадем много проста векторна репрезентация от текст
- как да изчислим косинусна близост между изречения
"""

from collections import Counter
from math import sqrt
from typing import Dict, List


def bag_of_words_embedding(text: str) -> Dict[str, float]:
    """
    Create a simple bag-of-words embedding: word -> frequency.
    Създава проста BoW репрезентация: дума -> честота.
    """
    tokens = text.lower().split()
    counts = Counter(tokens)
    total = sum(counts.values()) or 1
    return {word: count / total for word, count in counts.items()}


def cosine_similarity(vec1: Dict[str, float], vec2: Dict[str, float]) -> float:
    """
    Compute cosine similarity between two sparse vectors.
    Изчислява косинусна близост между два спарс вектора.
    """
    common_keys = set(vec1.keys()) & set(vec2.keys())
    dot = sum(vec1[k] * vec2[k] for k in common_keys)

    norm1 = sqrt(sum(v * v for v in vec1.values()))
    norm2 = sqrt(sum(v * v for v in vec2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot / (norm1 * norm2)


def compare_sentences(sentences: List[str]) -> None:
    """
    Print pairwise cosine similarities between sentences.
    Принтира косинусна близост между всички двойки изречения.
    """
    embeddings = [bag_of_words_embedding(s) for s in sentences]

    n = len(sentences)
    for i in range(n):
        for j in range(i + 1, n):
            sim = cosine_similarity(embeddings[i], embeddings[j])
            print(f"[{i}] vs [{j}] → similarity = {sim:.3f}")
            print(f"  {i}: {sentences[i]}")
            print(f"  {j}: {sentences[j]}")
            print()


if __name__ == "__main__":
    sentences = [
        "AI helps automate boring tasks.",
        "Artificial intelligence makes repetitive work easier.",
        "I like to eat pizza in the evening.",
        "Изкуственият интелект автоматизира повтаряща се работа."
    ]

    compare_sentences(sentences)
