# test_bank_account.py

import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Fresh account for every test
        self.account = BankAccount(1000)

    def test_deposit_increases_balance(self):
        self.account.deposit(200)
        self.assertEqual(self.account.balance, 1200)

    def test_withdraw_decreases_balance(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_more_than_balance_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_negative_deposit_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)


if __name__ == "__main__":
    unittest.main()
