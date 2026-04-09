# Day 78 — test_calculator.py
# Focus: assertion quality and edge cases

import unittest
from code.calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add_basic(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_with_negative(self):
        self.assertEqual(add(-2, 3), 1)

    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_divide_returns_float(self):
        result = divide(5, 2)
        self.assertEqual(result, 2.5)
        self.assertIsInstance(result, float)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()

