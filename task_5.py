import subprocess
import chardet

"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

web_resources = ["yandex.ru", "youtube.com"]


def ping_web_resources(web: str):
    ping = subprocess.Popen(["ping", web], stdout=subprocess.PIPE)
    for line in ping.stdout:
        res = chardet.detect(line)
        print(line.decode(encoding=res["encoding"]))


for i in web_resources:
    ping_web_resources(i)
