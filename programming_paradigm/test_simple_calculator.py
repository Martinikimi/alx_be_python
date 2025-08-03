
import unittest
from programming_paradigm.simple_calculator import add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

if __name__ == "__main__":
    unittest.main()

