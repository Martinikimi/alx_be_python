import unittest                      # ✅ import check
from programming_paradigm.simple_calculator import SimpleCalculator
   # ✅ import check

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):         # ✅ test_addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):      # ✅ test_subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 3), -3)

    def test_multiply(self):         # ✅ test_multiply
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_divide(self):           # ✅ test_divide
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(4, 0)

if __name__ == '__main__':
    unittest.main()
