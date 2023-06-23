import json
import unittest
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from common.utils import send_message, get_message
from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_CONNECTIONS, ACTION, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, ENCODING


class PreConfigServer:
    server_socket = None
    client_socket = None

    test_correct_response = {
        RESPONSE: 200,
        TIME: 1.1,
    }

    def create_sockets(self) -> None:
        """
        Создаем тестовый сокет для сервера и клиента
        :return:
        """
        # Сервер
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.server_socket.listen(MAX_CONNECTIONS)

        # Клиент
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.client, self.client_address = self.server_socket.accept()

    def close_sockets(self) -> None:
        """
        Закрываем сокеты
        :return:
        """
        self.client.close()
        self.client_socket.close()
        self.server_socket.close()


class TestUtils(unittest.TestCase, PreConfigServer):
    def test_get_message_ok(self):
        self.create_sockets()
        message = json.dumps(self.test_correct_response)
        self.client.send(message.encode(ENCODING))

        response = get_message(self.client_socket)
        self.assertEqual(self.test_correct_response, response)
        self.close_sockets()

    def test_get_message_received_not_dict(self):
        self.create_sockets()
        message = json.dumps('not dict')
        self.client.send(message.encode(ENCODING))
        self.assertRaises(ValueError, get_message, self.client_socket)
        self.close_sockets()

    def test_get_message_return_dict(self):
        self.create_sockets()
        message = json.dumps(self.test_correct_response)
        self.client.send(message.encode(ENCODING))
        self.assertIsInstance(get_message(self.client_socket), dict)
        self.close_sockets()


if __name__ == '__main__':
    unittest.main()
