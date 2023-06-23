import json
from socket import *

from common.variables import MAX_PACKAGE_LENGTH, ENCODING


def get_message(sock: socket):
    '''
    Утилита приема и декодирования сообщения, принимает байты, возвращает словарь или ошибку значения
    :param sock: socket
    :return: dict
    '''
    encoded_response = sock.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock: socket, message: dict):
    '''
    Утилита кодирования и отправки сообщения,
    принимает словарь и отправляет его
    :param sock: socket
    :param message: dict
    :return:
    '''

    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
