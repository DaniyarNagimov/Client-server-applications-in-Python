import json
from chardet import detect

"""
Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
    Для этого:
        Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
    цена (price), покупатель (buyer), дата (date). В это словаре параметров обязательно должны присутствовать
    юникод-символы, отсутствующие в кодировке ASCII.
        Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать
    величину отступа в 4 пробельных символа;
        Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;
        Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого 
    параметра.
"""


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'rb') as file:
        encoding = detect(file.read())['encoding']

    with open('orders.json', encoding=encoding) as file:
        data = json.load(file)

    with open('orders.json', 'w', encoding=encoding) as to_file:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, to_file, indent=4, ensure_ascii=False)


write_order_to_json('Робот', 4, 5699, 'Иванов И.И.', '19.02.2022')

