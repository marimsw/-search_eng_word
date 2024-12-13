#pip install nltk
import nltk
from nltk.corpus import words
import string

# Загрузите список английских слов
nltk.download('words')

# Получите список слов
english_words = set(words.words())

def is_english_word(word):
    return word.lower() in english_words

def is_english_letter(char):
    return char in string.ascii_letters

def check_input(text):
    # Разделяем текст на слова, игнорируя пробелы
    words_list = text.split()
    
    # Проверяем каждое слово
    for word in words_list:
        if is_english_word(word):
            print(f"{word} - это английское слово.")
        else:
            print(f"{word} - это не английское слово.")
    
    # Проверяем каждый символ, игнорируя пробелы
    for char in text:
        if char != ' ':  # Игнорируем пробелы
            if is_english_letter(char):
                print(f"{char} - это английская буква.")
            else:
                print(f"{char} - это не английская буква.")

# Пример использования
user_input = input("Введите текст для проверки: ")
check_input(user_input)
