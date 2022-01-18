"""
Определить, какие из слов, поданных на вход программы, невозможно записать в байтовом типе.
Для проверки правильности работы кода используйте значения: «attribute», «класс», «функция», «type»
"""

words_list = ['attribute', 'класс', 'функция', 'type']

for word in words_list:
    byt_word = bytes(word, 'utf-8')
    if len(byt_word) != len(word):
        print(f'Это «{word}» слово невозможно записать в байтовом типе')
