import unittest

import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        actual = calculator.add(1, 2, 3, 4, 5)
        expected = 15
        self.assertEqual(actual, expected, f"Should be {expected}")

    def test_subtract(self):
        actual = calculator.subtract(1, 2, 3, 4, 5)
        expected = -13
        self.assertEqual(actual, expected, f"Should be {expected}")

if __name__ == '__main__':
    unittest.main()