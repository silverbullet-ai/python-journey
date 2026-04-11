# test_calculator.py

import unittest
from calculator import add, divide


class TestCalculator(unittest.TestCase):

    # Normal case
    def test_add_normal(self):
        self.assertEqual(add(2, 3), 5)

    # Edge case: adding zero
    def test_add_with_zero(self):
        self.assertEqual(add(0, 5), 5)

    # Normal division
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    # Edge case: dividing zero
    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    # Negative test: division by zero
    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
