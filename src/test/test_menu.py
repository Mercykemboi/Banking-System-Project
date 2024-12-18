import unittest
from menu.menu import display_menu

class TestMenu(unittest.TestCase):
    def test_display_menu(self):
        # Since display_menu prints to stdout, we can't directly assert it.
        # We can test if it's being called without errors.
        try:
            display_menu()
        except Exception as e:
            self.fail(f"display_menu() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
# 