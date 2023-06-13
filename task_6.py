from chardet import detect

lst_in = ["сетевое программирование", "сокет", "декоратор"]

with open('test_file.txt', 'w') as f:
    for i in lst_in:
        f.write(f'{i}\n')

with open('test_file.txt', 'rb') as f:
    detected = detect(f.read())
    print(detected)

with open('test_file.txt', 'r', encoding=detected['encoding']) as f:
    print(f.read())
