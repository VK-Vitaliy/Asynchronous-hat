import unittest

from client import create_presence, process_ans
from common.variables import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, RESPONSE, ERROR


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        test_presence = create_presence()
        test_presence[TIME] = 1.1
        self.assertEqual(test_presence, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: "Guest"}})

    def test_process_ans_ok(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200: OK')

    def test_process_ans_error(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad request'}), '400 : Bad request')

    def test_process_ans_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad request'})


if __name__ == '__main__':
    unittest.main()
