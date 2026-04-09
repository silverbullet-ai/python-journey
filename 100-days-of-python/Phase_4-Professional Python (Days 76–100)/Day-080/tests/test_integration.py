# Day 80 — test_integration.py
# Focus: integration testing (no mocking)

import unittest
from code.service import get_uppercase_user_name


class TestUserIntegration(unittest.TestCase):

    def test_existing_user(self):
        result = get_uppercase_user_name(1)
        self.assertEqual(result, "ALICE")

    def test_non_existing_user(self):
        result = get_uppercase_user_name(99)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
