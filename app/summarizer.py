from sumy_algorithm import summarize
from tokenizer import tokenize_text  # Пример дополнительного импорта

def summarize_text(text):
    tokens = tokenize_text(text)  # Использование метода из tokenizer.py
    summary = summarize(tokens)  # Использование метода из sumy_algorithm.py
    return summary
