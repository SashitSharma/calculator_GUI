import unittest
from Calculator import Calculator
import tkinter as tk


class TestCalcu(unittest.TestCase):
    def test_calculate_addition(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "5"
        calculator.get_operator('+')
        calculator.result_label["text"] = "7"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "12.0")

        calculator.result_label["text"] = "-3"
        calculator.get_operator('+')
        calculator.result_label["text"] = "5"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "2.0")

        calculator.result_label["text"] = "2.5"
        calculator.get_operator('+')
        calculator.result_label["text"] = "1.75"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "4.25")
        root.destroy()

    def test_subtraction(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "7"
        calculator.get_operator('-')
        calculator.result_label["text"] = "5"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "2.0")

        calculator.result_label["text"] = "-3"
        calculator.get_operator('-')
        calculator.result_label["text"] = "5"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "-8.0")

        calculator.result_label["text"] = "2.5"
        calculator.get_operator('-')
        calculator.result_label["text"] = "1.75"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "0.75")
        root.destroy()

    def test_multiplication(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "7"
        calculator.get_operator('*')
        calculator.result_label["text"] = "5"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "35.0")

        calculator.result_label["text"] = "-3"
        calculator.get_operator('*')
        calculator.result_label["text"] = "5"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "-15.0")

        calculator.result_label["text"] = "2.5"
        calculator.get_operator('*')
        calculator.result_label["text"] = "1.75"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "4.375")
        root.destroy()

    def test_divison(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "36"
        calculator.get_operator('/')
        calculator.result_label["text"] = "6"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "6.0")

        calculator.result_label["text"] = "-144"
        calculator.get_operator('/')
        calculator.result_label["text"] = "28"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "-5.14286")

        calculator.result_label["text"] = "-22.5"
        calculator.get_operator('/')
        calculator.result_label["text"] = "0.75"
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "-30.0")
        root.destroy()

    def test_square_root(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "36"
        calculator.get_operator('√')
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "6.0")

        calculator.result_label["text"] = "144"
        calculator.get_operator('√')
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "12.0")

        calculator.result_label["text"] = "63.75"
        calculator.get_operator('√')
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "7.98436")
        root.destroy()

    def test_cube_root(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "27"
        calculator.get_operator('∛')
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "3.0")

        calculator.result_label["text"] = "0.65"
        calculator.get_operator('∛')
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "0.86624")

        calculator.result_label["text"] = "107610"
        calculator.get_operator('∛')
        calculator.get_result()
        result = calculator.result_label["text"]
        self.assertEqual(result, "47.56464")
        root.destroy()


if __name__ == '__main__':
    unittest.main()
