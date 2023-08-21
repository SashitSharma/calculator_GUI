import unittest
from Calculator import Calculator
import tkinter as tk


class TestFunctions(unittest.TestCase):
    def test_calculate_sin(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "30"
        calculator.calculate_sin()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Sine: 0.5000")

        calculator.result_label["text"] = "0"
        calculator.calculate_sin()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Sine: 0.0000")

        calculator.result_label["text"] = "0-"
        calculator.calculate_sin()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Invalid Input")

        calculator.result_label["text"] = "-60"
        calculator.calculate_sin()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Sine: -0.8660")


    def test_calculate_cos(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)

        calculator.result_label["text"] = "60"
        calculator.calculate_cos()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Cosine: 0.5000")

        calculator.result_label["text"] = "90"
        calculator.calculate_cos()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Cosine: 0.0000")

        calculator.result_label["text"] = "65*"
        calculator.calculate_cos()
        result = calculator.result_label["text"]
        self.assertEqual(result, "Invalid Input")

    def test_clear(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)
        calculator.result_label["text"] = "C"
        calculator.clear()
        result = calculator.result_label["text"]
        self.assertEqual(result, " ")

    def test_backspace(self):
        root = tk.Tk()
        result_label = tk.Label(root)
        calculator = Calculator(result_label=result_label)
        calculator.result_label["text"] = "⌫"
        calculator.backspace()
        current = calculator.result_label["text"]
        result = current[:-1]
        self.assertEqual(result, result)


if __name__ == "__main__":
    unittest.main()

