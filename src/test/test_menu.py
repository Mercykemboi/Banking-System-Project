#it displays the menu either deposit, withraw
# python built in testing framework unittest
import unittest
# importing my dispay menu function
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