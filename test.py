import os
from unittest import TestCase
from app import Token


class TestToken(TestCase):
    def setUp(self) -> None:
        os.environ['SECRET'] = "SECRET"

    def test_create_token(self):
        token = Token()
        new_token = token.create_token(data={"test_data": 1})
        self.assertIsInstance(new_token, str)

    def test_decode_token(self):
        token = Token()
        new_token = token.create_token(data={"data": 1})
        decoded_token = token.decode_token(token=new_token)
        self.assertIsInstance(decoded_token, dict)
        self.assertEqual(decoded_token['data'], 1)
