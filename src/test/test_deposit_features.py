import unittest
from features.deposit import deposit_money
from accounts.account import set_balance, get_balance

class TestDeposit(unittest.TestCase):
    def setUp(self):
        # Initialize account balance to a known value before each test
        set_balance(4000)

    def test_deposit_valid(self):
        new_balance = deposit_money(get_balance())
        self.assertEqual(new_balance, 1100)

    def test_deposit_invalid(self):
        new_balance = deposit_money(get_balance())  # Invalid (negative deposit)
        self.assertEqual(new_balance, 1000)

if __name__ == "__main__":
    unittest.main()
