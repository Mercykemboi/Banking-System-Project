
import unittest
from accounts.account import set_balance, get_balance

class TestAccount(unittest.TestCase):
    def setUp(self):
        # Initialize account balance to a known value before each test
        set_balance(1000)

    def test_get_balance(self):
        self.assertEqual(get_balance(), 1000)

    def test_set_balance(self):
        set_balance(1500)
        self.assertEqual(get_balance(), 1500)

if __name__ == "__main__":
    unittest.main()
