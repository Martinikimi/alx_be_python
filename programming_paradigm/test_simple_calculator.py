# programming_paradigm/test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiplication(self):
        """Test multiplication of two numbers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_division(self):
        """Test division of two numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
