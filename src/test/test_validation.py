import unittest
from validation.validation import input_validation


class TestInputValidation(unittest.TestCase):
    def test_valid_choice(self):
        self.assertEqual(input_validation(1), 1)
        self.assertEqual(input_validation(4), 4)

    def test_invalid_choice(self):
        self.assertIsNone(input_validation(5))
        self.assertIsNone(input_validation("abc"))


if __name__ == "__main__":
    unittest.main()
