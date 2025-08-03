#!/usr/bin/python3
"""
Unittest module for simple_calculator.py
"""

import unittest
from programming_paradigm.simple_calculator import add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for simple calculator functions"""

    def test_addition(self):
        """Check addition"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtraction(self):
        """Check subtraction"""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 5), 0)

    def test_multiply(self):
        """Check multiplication"""
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 3), -3)

    def test_divide(self):
        """Check division"""
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Check divide by zero raises error"""
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
