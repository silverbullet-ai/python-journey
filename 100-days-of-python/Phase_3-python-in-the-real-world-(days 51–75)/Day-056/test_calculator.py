# test_calculator.py

import unittest
from calculator import add, subtract, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
