"""
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

dict_to_yaml = {'items': ['computer', 'printer', 'keyboard', 'moise'],
                'quantity': 4,
                'items_price': {'computer': '200€-1000€',
                                'printer': '100€-300€',
                                'keyboard': '10€-20€',
                                'moise': '5€-10€'
                                }
                }


def write_data_to_yaml(data):
    with open('file.yaml', 'w', encoding='UTF-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


write_data_to_yaml(dict_to_yaml)