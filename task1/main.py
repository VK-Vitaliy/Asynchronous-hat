import csv
import re
from pathlib import Path

import chardet

"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""


def get_data():
    directory = Path.cwd()
    files = Path(directory).glob('*.txt')

    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"],
                 ]

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    max_row = 1

    for file in files:
        with open(f'{file}', 'rb') as fb:
            res = chardet.detect(fb.read())
            with open(f'{file}', 'r', encoding=res['encoding']) as f:
                data = f.read()
                os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
                os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
                os_prod_reg = re.compile(r'Название ОС:\s*[^\n]*')
                os_name_list.append(" ".join(os_prod_reg.findall(data)[0].split()[3:5]))
                os_prod_reg = re.compile(r'Код продукта:\s*\S*')
                os_code_list.append(os_prod_reg.findall(data)[0].split()[2])
                os_prod_reg = re.compile(r'Тип системы:\s*\S*')
                os_type_list.append(os_prod_reg.findall(data)[0].split()[2])
                max_row += 1

    for i in zip(list(range(1, max_row)), os_prod_list, os_name_list, os_code_list, os_type_list):
        main_data.append(list(i))
    return main_data


def write_to_csv(cvt_file: str):
    with open(cvt_file, 'w') as f:
        f_writer = csv.writer(f)
        data = get_data()
        for row in data:
            f_writer.writerow(row)


write_to_csv('data_report.csv')

