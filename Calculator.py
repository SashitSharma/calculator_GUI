import tkinter as tk
import math
import winsound


class Calculator:
    def __init__(self, result_label=None):
        self.fNumber1 = None
        self.fNumber2 = None
        self.operator = None

        self.win = tk.Tk()
        self.win.geometry("380x485")
        self.win.resizable(0, 0)
        self.win.title("in-tech Calculator")
        self.win.configure(background="Black")

        if result_label is not None:
            self.result_label = result_label

        self.border_frame = tk.Frame(self.win, borderwidth=2, background="white")
        self.border_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.result_label = tk.Label(self.border_frame, text="", bg="white", fg="Black")
        self.result_label.grid(row=1, column=0, columnspan=10, pady=(50, 25), sticky="w")
        self.result_label.config(font=("verdana", 20, "bold"))

        self.equation_label = tk.Label(self.border_frame, text="", bg="white", fg="purple")
        self.equation_label.grid(row=0, column=0, columnspan=10, pady=(0, 5), sticky="w")
        self.equation_label.config(font=("Arial", 12))

        btn_7 = self.create_button("7", 2, 0, 5)
        btn_8 = self.create_button("8", 2, 1, 5)
        btn_9 = self.create_button("9", 2, 2, 5)
        btn_add = self.create_button("+", 2, 3, 5)
        btn_4 = self.create_button("4", 3, 0, 5)
        btn_5 = self.create_button("5", 3, 1, 5)
        btn_6 = self.create_button("6", 3, 2, 5)
        btn_minus = self.create_button("-", 3, 3, 5)
        btn_1 = self.create_button("1", 4, 0, 5)
        btn_2 = self.create_button("2", 4, 1, 5)
        btn_3 = self.create_button("3", 4, 2, 5)
        btn_multiply = self.create_button("*", 4, 3, 5)
        btn_clear = self.create_button("C", 6, 1, 10,  columnspan=2)
        btn_0 = self.create_button("0", 5, 1, 5)
        btn_equal = self.create_button("=", 6, 3, 10,  columnspan=2)
        btn_divide = self.create_button("/", 5, 3, 5)
        btn_root = self.create_button("√", 5, 0, 5, 1, 1,)
        btn_exponent = self.create_button("x^y", 5, 2, 5, 1, 1)
        btn_sin = self.create_button("sin", 3, 4, 5, 1, 1)
        btn_cos = self.create_button("cos", 4, 4, 5, 1, 1)
        btn_backspace = self.create_button("⌫", 2, 4, 5)
        btn_decimal = self.create_button(".", 5, 4, 5)
        btn_cuberoot = self.create_button("∛", 6, 0, 5, 1, 1)

    def create_button(self, text, row, column, width,  rowspan=1, columnspan=1):
        btn = tk.Button(self.border_frame, text=text, fg="Black", bg="LightGray", width=width, height=2, cursor="hand2")
        btn.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=1, pady=1)
        btn.config(font=("verdana", 14))

        if text.isdigit() or text == ".":
            btn.config(command=lambda: self.get_digit(text))
        elif text in ("+", "-", "*", "/", "x^y"):
            btn.config(command=lambda op=text: self.get_operator(op))
        elif text == "⌫":
            btn.config(command=self.backspace)
        elif text == "C":
            btn.config(command=self.clear)
        elif text == "=":
            btn.config(command=self.get_result)
        elif text == "√":
            btn.config(command=lambda: self.get_operator("√"))
        elif text == "∛":
            btn.config(command=lambda: self.get_operator("∛"))
        elif text == "sin":
            btn.config(command=self.calculate_sin)
        elif text == "cos":
            btn.config(command=self.calculate_cos)

        return btn

    def get_digit(self, digit):
        current = self.result_label["text"]
        if "." in current and digit == ".":
            return
        new = current + str(digit)
        self.result_label.config(text=new)

    def backspace(self):
        current = self.result_label["text"]
        new = current[:-1]
        self.result_label.config(text=new)

    def clear(self):
        self.result_label.config(text=" ")
        self.equation_label.config(text=" ")

    def get_operator(self, op):
        if op == "-" and self.result_label["text"] == "":
            self.result_label.config(text="-")
        else:
            self.fNumber1 = float(self.result_label["text"])
            self.operator = op
            self.result_label.config(text="")
            self.equation_label.config(text=f"{self.fNumber1} {self.operator}")
    def calculate_sin(self):
        try:
            self.fNumber1 = float(self.result_label["text"])
            angle_radians = math.radians(self.fNumber1)
            result = math.sin(angle_radians)
            self.result_label.config(text=f"Sine: {result:.4f}")
            self.equation_label.config(text=f"sin({self.fNumber1}) =")
        except ValueError:
            self.result_label.config(text="Invalid Input")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    def calculate_cos(self):
        try:
            self.fNumber1 = float(self.result_label["text"])
            angle_radians = math.radians(self.fNumber1)
            result = math.cos(angle_radians)
            self.result_label.config(text=f"Cosine: {result:.4f}")
            self.equation_label.config(text=f"cos({self.fNumber1}) =")
        except ValueError:
            self.result_label.config(text="Invalid Input")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    def get_result(self):
        if self.operator == "√":
            try:
                root_square = round(math.sqrt(self.fNumber1), 5)
                self.result_label.config(text=str(root_square))
                self.equation_label.config(text=f"√({self.fNumber1}) =")
            except ValueError:
                self.result_label.config(text="Error")
                self.equation_label.config(text="")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

        elif self.operator == "∛":
            try:
                root_cube = round(self.fNumber1 ** (1 / 3), 5)
                self.result_label.config(text=str(root_cube))
                self.equation_label.config(text=f"∛({self.fNumber1}) =")
            except ValueError:
                self.result_label.config(text="Error")
                self.equation_label.config(text="")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

        elif self.operator == "+":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 + self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} + {self.fNumber2} =")

        elif self.operator == "-":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 - self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} - {self.fNumber2} =")

        elif self.operator == "*":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 * self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} * {self.fNumber2} =")

        elif self.operator == "x^y"::   #the error is here
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 ** self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} ^ {self.fNumber2} =")

        else:
            self.fNumber2 = float(self.result_label["text"])
            if self.fNumber2 == 0:
                self.result_label.config(text="Error")
                self.equation_label.config(text="")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            else:
                self.result_label.config(text=str(round(self.fNumber1 / self.fNumber2, 5)))
                self.equation_label.config(text=f"{self.fNumber1} / {self.fNumber2} =")

        self.operator = None

    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
