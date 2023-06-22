import json
import socket
import sys
import time

from common.utils import send_message, get_message
from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, PRESENCE, ACTION, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR


def create_presence(account_name='Guest'):
    '''
    ФункцияВозвращает сервисное сообщение к серверу о присутствии.
    :param account_name: str
    :return: dict
    '''

    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    '''
    Функция разбирает ответ севера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаем значения по умолчанию
    client.py 192.168.56.1 8079
    server.py -p 8079 -a 192.168.56.1
    :return:
    '''

    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print("В качестве порта может быть только число в диапазоне от 1024 до 65535")
        sys.exit(1)

    # Инициализация сокета и обмен
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print("Не удалось декодировать сообщение от сервера")


if __name__ == '__main__':
    main()
