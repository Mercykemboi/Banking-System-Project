import unittest
from features.withdraw import withdraw_money
from accounts.account import set_balance, get_balance


class TestWithdraw(unittest.TestCase):
    def setUp(self):
        # Initialize account balance to a known value before each test
        set_balance(9000)

    def test_withdraw_valid(self):
        new_balance = withdraw_money(get_balance())
        self.assertEqual(new_balance, 900)

    def test_withdraw_invalid(self):
        new_balance = withdraw_money(get_balance())  # (more than balance)
        self.assertEqual(new_balance, 1000)


if __name__ == "__main__":
    unittest.main()
