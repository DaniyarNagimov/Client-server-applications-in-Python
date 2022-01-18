"""
Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме с помощью добавления литеры b к текстовому значению,
(т.е. ни в коем случае не используя методы encode и decode) и определить тип, содержимое и длину соответствующих
переменных.
"""

words_list = ['class', 'function', 'method']

for word in words_list:
    byt_word = bytes(word, 'utf-8')
    print(byt_word, type(byt_word), len(byt_word))
