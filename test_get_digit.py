import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_get_digit(self):
        self.calculator = Calculator()
        self.calculator.win.withdraw()
        self.calculator.get_digit("1")
        self.assertEqual(self.calculator.result_label["text"], "1")
        self.calculator.get_digit("2")
        self.assertEqual(self.calculator.result_label["text"], "12")
        self.calculator.get_digit(".")
        self.assertEqual(self.calculator.result_label["text"], "12.")
        self.calculator.get_digit("5")
        self.assertEqual(self.calculator.result_label["text"], "12.5")

if __name__ == "__main__":
    unittest.main()

