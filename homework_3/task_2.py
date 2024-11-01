from collections import Counter
import re

def count_words(text):
    # Убираем знаки припинания и переводим в нижний регистр
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

    # Разбиваем текст на слова
    words = cleaned_text.split()
    
    # Используем Counter для подсчета уникальных слов
    word_counts = Counter(words)

    return len(word_counts)

# Пример
text = '''Напишите функцию, которая принимает на вход строку и 
выводит количество уникальных слов в ней, игнорируя знаки препинания и пробелы. 
Используйте модуль collections для этой задач'''

unique_word_count = count_words(text)
print(f"Количество уникальных слов: {unique_word_count}")
