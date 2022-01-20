import csv
from chardet import detect
import re

"""
Задание на закрепление знаний по модулю CSV. 
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и 
формирующий новый «отчетный» файл в формате CSV. 
    Для этого:
        Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание 
    данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров 
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в 
    соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, 
    os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — 
    и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», 
    «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл 
    main_data (также для каждого файла);
        Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение 
    данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
        Проверить работу программы через вызов функции write_to_csv().

"""


def get_data():
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod = re.compile(r'^(Изготовитель системы)')
    os_name = re.compile(r'^(Название ОС)')
    os_code = re.compile(r'^(Код продукта)')
    os_type = re.compile(r'^(Тип системы)')
    search_strings_dict = {
        'os_prod_list': [],
        'os_name_list': [],
        'os_code_list': [],
        'os_type_list': []
    }

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file:
            encoding = detect(file.read())['encoding']

        with open(f'info_{i}.txt', encoding=encoding) as file:
            for line in file:
                pairs = line.split(':')
                for pair in pairs:
                    if os_prod.search(pair):
                        search_strings_dict['os_prod_list'].append(pairs[1].strip())
                    elif os_name.search(pair):
                        search_strings_dict['os_name_list'].append(pairs[1].strip())
                    elif os_code.search(pair):
                        search_strings_dict['os_code_list'].append(pairs[1].strip())
                    elif os_type.search(pair):
                        search_strings_dict['os_type_list'].append(pairs[1].strip())

    for key in search_strings_dict.keys():
        for num, v in enumerate(search_strings_dict.get(key)):
            if len(main_data) < len(main_data[0]):
                main_data.insert(num + 1, [v])
            else:
                main_data[num + 1].append(v)

    return main_data


def write_to_csv(my_list):
    with open('main_data.csv', 'w', encoding='utf-8') as file:
        for row in my_list:
            csv.writer(file).writerow(row)


write_to_csv(get_data())
