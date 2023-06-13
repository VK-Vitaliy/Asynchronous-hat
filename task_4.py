"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

lst_in = ["разработка", "администрирование", "protocol", "standard"]


def get_bytes_lst(lst_in: list) -> list:
    return [i.encode("UTF-8") for i in lst_in]


def get_str_lst(lst_in: list) -> list:
    return [i.decode('utf-8') for i in lst_in]


res1 = get_bytes_lst(lst_in)
print(res1)
res2 = get_str_lst(res1)
print(res2)
