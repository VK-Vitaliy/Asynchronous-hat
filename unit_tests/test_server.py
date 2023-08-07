import time
import unittest

from common.variables import RESPONSE, ERROR, TIME, USER, ACCOUNT_NAME, ACTION
from server import process_client_message


class TestServer(unittest.TestCase):
    ok_dict = {RESPONSE: 200}
    error_dict = {RESPONSE: 400, ERROR: 'Bad request'}

    def test_no_action(self):
        self.assertEqual(process_client_message({TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}
                                                 }), self.error_dict)

    def test_incorrect_action(self):
        self.assertEqual(process_client_message({ACTION: 'incorrect', TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}
                                                 }), self.error_dict)

    def test_no_time(self):
        self.assertEqual(process_client_message({ACTION: 'presence', USER: {ACCOUNT_NAME: 'Guest'}
                                                 }), self.error_dict)

    def test_no_user(self):
        self.assertEqual(process_client_message({ACTION: 'presence', TIME: time.time()}), self.error_dict)

    def test_no_guest_user(self):
        self.assertEqual(process_client_message({ACTION: 'presence', TIME: time.time(),
                                                 USER: {ACCOUNT_NAME: 'no_guest'}}), self.error_dict)

    def test_response_ok(self):
        self.assertEqual(process_client_message({ACTION: 'presence', TIME: time.time(),
                                                 USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()
