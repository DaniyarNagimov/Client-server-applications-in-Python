"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

words_list = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words_list:
    encode_word = word.encode(encoding='utf-8')
    print(f'Слово «{word}» в байтовом представлении: {encode_word}')
    decode_word = encode_word.decode(encoding='utf-8')
    print(f'Слово «{word}» в строковом представлении: {decode_word}')
