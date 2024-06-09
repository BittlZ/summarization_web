from sumy_algorithm import summarize_text
from tokenizer import tokenize_text  # Пример дополнительного импорта

def summarize(text):
    tokens = tokenize_text(text)  # Использование метода из tokenizer.py
    summary = summarize_text(tokens)  # Использование метода из sumy_algorithm.py
    return summary
