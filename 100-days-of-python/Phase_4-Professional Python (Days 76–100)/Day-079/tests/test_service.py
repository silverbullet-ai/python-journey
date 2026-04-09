# Day 79 — test_service.py
# Focus: mocking and isolation

import unittest
from unittest.mock import patch
from code import service


class TestService(unittest.TestCase):

    @patch("code.service.fetch_data")
    def test_process_data_uses_mocked_dependency(self, mock_fetch):
        mock_fetch.return_value = "hello"

        result = service.process_data()

        self.assertEqual(result, "HELLO")
        mock_fetch.assert_called_once()


if __name__ == "__main__":
    unittest.main()
