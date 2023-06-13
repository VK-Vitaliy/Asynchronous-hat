"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

lst_in = ["attribute", "класс", "функция", "type"]


def find_ascii_or_unicode(lst_in: list):
    res1 = []
    res2 = []
    for i in lst_in:
        try:
            bytes(i, 'ASCII')
            res1.append(i)
        except UnicodeEncodeError:
            res2.append(i)

    return f"можем использовать маркировку b'' к словам {res1} \n" \
           f"не можем использовать маркировку b'' к словам {res2}"


print(find_ascii_or_unicode(lst_in))
