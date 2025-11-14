<svg width="600" height="180" viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <defs>
    <linearGradient id="bgGradient" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1f2933"></stop>
      <stop offset="100%" stop-color="#111827"></stop>
    </linearGradient>
  </defs>
  <rect width="600" height="180" rx="24" fill="url(#bgGradient)"></rect>

  <!-- Abstract AI nodes -->
  <circle cx="120" cy="60" r="8" fill="#38bdf8"></circle>
  <circle cx="80" cy="120" r="6" fill="#a855f7"></circle>
  <circle cx="160" cy="120" r="6" fill="#f97316"></circle>

  <line x1="120" y1="60" x2="80" y2="120" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" opacity="0.7"></line>
  <line x1="120" y1="60" x2="160" y2="120" stroke="#f97316" stroke-width="2" stroke-linecap="round" opacity="0.7"></line>
  <line x1="80" y1="120" x2="160" y2="120" stroke="#a855f7" stroke-width="2" stroke-linecap="round" opacity="0.7"></line>

  <!-- Main title -->
  <text x="210" y="80" fill="#f9fafb" font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif" font-size="32" font-weight="700">
    PolyglotAI Toolkit
  </text>

  <!-- Subtitle EN -->
  <text x="210" y="110" fill="#e5e7eb" font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif" font-size="14">
    Multilingual AI utilities • English &amp; Bulgarian
  </text>

  <!-- Subtitle BG -->
  <text x="210" y="135" fill="#9ca3af" font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif" font-size="13">
    Многоезични AI инструменти • Английски и Български
  </text>
</svg>

![logo](https://github.com/user-attachments/assets/f4d4796a-7760-4746-a1db-a71683e1c9ee)

A lightweight, e![Uploading logo.svg…]()
xtendable toolkit providing AI-powered utilities and examples, written in **English** and **Bulgarian** to help developers learn, experiment, and prototype small to mid‑scale AI systems quickly.

---

## **📘 Description / Описание**

### **English**

PolyglotAI Toolkit is an educational and practical repository focused on demos, utilities, and starter templates for AI applications. It includes examples for text processing, embeddings, classification, small LLM usage patterns, and more. Ideal for beginners and intermediate developers exploring applied AI.

### **Български**

PolyglotAI Toolkit е образователно и практическо хранилище, съдържащо демо примери, помощни инструменти и стартови шаблони за AI приложения. Включва примери за обработка на текст, ембеддинги, класификация, използване на малки LLM модели и други. Подходящо за начинаещи и средно напреднали разработчици.

---

## **📂 Repository Structure / Структура на хранилището**

```
polyglotai-toolkit/
│
├── README.md
├── examples/
│   ├── text_classification_en.py
│   ├── text_classification_bg.py
│   ├── embeddings_demo.py
│
├── utils/
│   ├── preprocess.py
│   ├── language_detection.py
│
└── data/
    ├── sample_english.txt
    ├── sample_bulgarian.txt
```

---
### **English Version**

Welcome to **PolyglotAI Toolkit**, a dual‑language (EN/BG) educational AI repository. This project contains:

* Text preprocessing utilities
* Simple text classifiers
* Embedding demos
* AI usage examples with multilingual support

### **Bulgarian Version / Българска версия**

Добре дошли в **PolyglotAI Toolkit**, двуезично (EN/BG) образователно AI хранилище. Проектът съдържа:

* Инструменти за предварителна обработка на текст
* Прости текстови класификатори
* Демонстрации с ембеддинги
* AI примери с многоезична поддръжка

---

## **🚀 Example Code (English & Bulgarian)**

### **English: Simple Text Classification**

```python
from utils.preprocess import clean_text

sample = "AI is transforming the future of technology."
cleaned = clean_text(sample)
print(cleaned)
```

### **Български: Класификация на текст**

```python
from utils.preprocess import clean_text

sample = "Изкуственият интелект променя бъдещето на технологиите."
cleaned = clean_text(sample)
print(cleaned)
```
