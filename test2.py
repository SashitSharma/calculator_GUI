import tkinter as tk
import math
import winsound

class Calculator:
    def __init__(self):
        self.fNumber1 = None
        self.fNumber2 = None
        self.operator = None

        self.win = tk.Tk()
        self.win.geometry("380x485")
        self.win.resizable(1, 0)
        self.win.title("in-tech Calculator")
        self.win.configure(background="Black")

        self.border_frame = tk.Frame(self.win, borderwidth=2, relief=tk.GROOVE, background="Black")
        self.border_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.result_label = tk.Label(self.border_frame, text="", bg="Black", fg="white")
        self.result_label.grid(row=1, column=0, columnspan=10, pady=(50, 25), sticky="w")
        self.result_label.config(font=("verdana", 20, "bold"))

        self.equation_label = tk.Label(self.border_frame, text="", bg="Black", fg="turquoise1")
        self.equation_label.grid(row=0, column=0, columnspan=10, pady=(0, 5), sticky="w")
        self.equation_label.config(font=("Arial", 12))

        btn_7 = self.create_button(2, 0, "7", 5, 2, self.get_digit, 7)
        btn_8 = self.create_button(2, 1, "8", 5, 2, self.get_digit, 8)
        btn_9 = self.create_button(2, 2, "9", 5, 2, self.get_digit, 9)
        btn_add = self.create_button(2, 3, "+", 5, 2, self.get_operator, "+")

        btn_4 = self.create_button(3, 0, "4", 5, 2, self.get_digit, 4)
        btn_5 = self.create_button(3, 1, "5", 5, 2, self.get_digit, 5)
        btn_6 = self.create_button(3, 2, "6", 5, 2, self.get_digit, 6)
        btn_minus = self.create_button(3, 3, "-", 5, 2, self.get_operator, "-")

        btn_1 = self.create_button(4, 0, "1", 5, 2, self.get_digit, 1)
        btn_2 = self.create_button(4, 1, "2", 5, 2, self.get_digit, 2)
        btn_3 = self.create_button(4, 2, "3", 5, 2, self.get_digit, 3)
        btn_multiply = self.create_button(4, 3, "*", 5, 2, self.get_operator, "*")

        btn_clear = self.create_button(6, 1, "C", 11, 2, self.clear, "")
        btn_0 = self.create_button(5, 1, "0", 5, 2, self.get_digit, 0)
        btn_equal = self.create_button(6, 3, "=", 11, 2, self.get_result)

        btn_divide = self.create_button(5, 3, "/", 5, 2, self.get_operator, "/")
        btn_root = self.create_button(5, 0, "√", 5, 2, self.get_operator, "√")
        btn_exponent = self.create_button(5, 2, "x^y", 5, 2, self.get_operator, "x^y")

        btn_sin = self.create_button(3, 4, "sin", 5, 2, self.calculate_sin)
        btn_cos = self.create_button(4, 4, "cos", 5, 2, self.calculate_cos)
        btn_cuberoot = self.create_button(6, 0, "∛", 5, 2, self.get_operator, "∛")
        btn_decimal = self.create_button(5, 4, ".", 5, 2, self.get_digit, ".")

    def create_button(self, row, col, text, width, height, command, *args):
        btn = tk.Button(self.border_frame, text=text, fg="Black", bg="Skyblue", width=width, height=height,
                        cursor="hand2", command=lambda: command(*args))
        btn.grid(row=row, column=col, padx=1, pady=1)
        btn.config(font=("verdana", 14))
        return btn

    def get_digit(self, digit):
        current = self.result_label["text"]
        if "." in current and digit == ".":
            return
        new = current + str(digit)
        self.result_label.config(text=new)
        winsound.Beep(300, 100)

    def backspace(self):
        current = self.result_label["text"]
        new = current[:-1]
        self.result_label.config(text=new)
        winsound.Beep(500, 100)

    def clear(self):
        self.result_label.config(text=" ")
        self.equation_label.config(text=" ")
        winsound.Beep(500, 100)

    def get_operator(self, op):
        if self.result_label["text"]:
            self.fNumber1 = float(self.result_label["text"])
            self.operator = op
            self.result_label.config(text="")
            self.equation_label.config(text=f"{self.fNumber1} {self.operator}")
            winsound.Beep(500, 100)

    def calculate_sin(self):
        try:
            self.fNumber1 = float(self.result_label["text"])
            angle_radians = math.radians(self.fNumber1)
            result = math.sin(angle_radians)
            self.result_label.config(text=f"Sine: {result:.4f}")
            self.equation_label.config(text=f"sin({self.fNumber1}) =")
            winsound.Beep(500, 100)
        except ValueError:
            self.result_label.config(text="Invalid input")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    def calculate_cos(self):
        try:
            self.fNumber1 = float(self.result_label["text"])
            angle_radians = math.radians(self.fNumber1)
            result = math.cos(angle_radians)
            self.result_label.config(text=f"Cosine: {result:.4f}")
            self.equation_label.config(text=f"cos({self.fNumber1}) =")
            winsound.Beep(500, 100)
        except ValueError:
            self.result_label.config(text="Invalid input")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    def get_result(self):
        if self.operator == "√":
            try:
                self.fNumber1 = float(self.result_label["text"])
                root_square = round(math.sqrt(self.fNumber1), 5)
                self.result_label.config(text=str(root_square))
                self.equation_label.config(text=f"√({self.fNumber1}) =")
                winsound.Beep(500, 100)
            except ValueError:
                self.result_label.config(text="Error")
                self.equation_label.config(text="")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

        elif self.operator == "∛":
            try:
                self.fNumber1 = float(self.result_label["text"])
                root_cube = round(math.pow(self.fNumber1, 1 / 3), 5)
                self.result_label.config(text=str(root_cube))
                self.equation_label.config(text=f"∛({self.fNumber1}) =")
                winsound.Beep(500, 100)
            except ValueError:
                self.result_label.config(text="Error")
                self.equation_label.config(text="")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        elif self.operator == "+":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 + self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} + {self.fNumber2} =")
            winsound.Beep(500, 100)

        elif self.operator == "-":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 - self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} - {self.fNumber2} =")
            winsound.Beep(500, 100)

        elif self.operator == "*":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 * self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} * {self.fNumber2} =")
            winsound.Beep(500, 100)

        elif self.operator == "x^y":
            self.fNumber2 = float(self.result_label["text"])
            self.result_label.config(text=str(self.fNumber1 ** self.fNumber2))
            self.equation_label.config(text=f"{self.fNumber1} ^ {self.fNumber2} =")
            winsound.Beep(500, 100)

        else:
            self.fNumber2 = float(self.result_label["text"])
            if self.fNumber2 == 0:
                self.result_label.config(text="Error")
                self.equation_label.config(text="")
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            else:
                self.result_label.config(text=str(round(self.fNumber1 / self.fNumber2, 5)))
                self.equation_label.config(text=f"{self.fNumber1} / {self.fNumber2} =")
                winsound.Beep(500, 100)

            self.operator = None

    def create_button(self, row, col, text, width, height, command, *args):
        btn = tk.Button(self.border_frame, text=text, fg="Black", bg="Skyblue", width=width, height=height,
                        cursor="hand2", command=lambda: command(*args))
        btn.grid(row=row, column=col, padx=1, pady=1)
        btn.config(font=("verdana", 14))
        return btn

    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
