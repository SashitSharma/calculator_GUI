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
        self.win.resizable(0, 0)
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



        btn_7 = tk.Button(self.border_frame, text="7", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                      command=lambda: self.get_digit(7))
        btn_7.grid(row=2, column=0)
        btn_7.config(font=("verdana", 14))

        btn_8 = tk.Button(self.border_frame, text="8", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(8))
        btn_8.grid(row=2, column=1)
        btn_8.config(font=("verdana", 14))

        btn_9 = tk.Button(self.border_frame, text="9", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(9))
        btn_9.grid(row=2, column=2)
        btn_9.config(font=("verdana", 14))

        btn_add = tk.Button(self.border_frame, text="+", fg="Black", bg="lightgreen", width=5, height=2, cursor="hand2",
                            command=lambda: self.get_operator("+"))
        btn_add.grid(row=2, column=3)
        btn_add.config(font=("verdana", 14))

        btn_4 = tk.Button(self.border_frame, text="4", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(4))
        btn_4.grid(row=3, column=0)
        btn_4.config(font=("verdana", 14))

        btn_5 = tk.Button(self.border_frame, text="5", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(5))
        btn_5.grid(row=3, column=1)
        btn_5.config(font=("verdana", 14))

        btn_6 = tk.Button(self.border_frame, text="6", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(6))
        btn_6.grid(row=3, column=2)
        btn_6.config(font=("verdana", 14))

        btn_minus = tk.Button(self.border_frame, text="-", fg="Black", bg="lightGreen", width=5, height=2, cursor="hand2",
                              command=lambda: self.get_operator("-"))
        btn_minus.grid(row=3, column=3)
        btn_minus.config(font=("verdana", 14))

        btn_1 = tk.Button(self.border_frame, text="1", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(1))
        btn_1.grid(row=4, column=0)
        btn_1.config(font=("verdana", 14))

        btn_2 = tk.Button(self.border_frame, text="2", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(2))
        btn_2.grid(row=4, column=1)
        btn_2.config(font=("verdana", 14))

        btn_3 = tk.Button(self.border_frame, text="3", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(3))
        btn_3.grid(row=4, column=2)
        btn_3.config(font=("verdana", 14))

        btn_multiply = tk.Button(self.border_frame, text="*", fg="Black", bg="lightGreen", width=5, height=2, cursor="hand2",
                                 command=lambda: self.get_operator("*"))
        btn_multiply.grid(row=4, column=3)
        btn_multiply.config(font=("verdana", 14))

        btn_clear = tk.Button(self.border_frame, text="C", fg="Black", bg="crimson", width=11, height=2, cursor="hand2",
                              command=lambda: self.clear(""))
        btn_clear.grid(row=6, column=1, columnspan=2)
        btn_clear.config(font=("verdana", 14))

        btn_0 = tk.Button(self.border_frame, text="0", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                          command=lambda: self.get_digit(0))
        btn_0.grid(row=5, column=1)
        btn_0.config(font=("verdana", 14))

        btn_equal = tk.Button(self.border_frame, text="=", fg="Black", bg="violet", width=11, height=2, cursor="hand2",
                              command=self.get_result)
        btn_equal.grid(row=6, column=3, columnspan=2)
        btn_equal.config(font=("verdana", 14))

        btn_divide = tk.Button(self.border_frame, text="/", fg="Black", bg="lightGreen", width=5, height=2, cursor="hand2",
                               command=lambda: self.get_operator("/"))
        btn_divide.grid(row=5, column=3)
        btn_divide.config(font=("verdana", 14))

        btn_root = tk.Button(self.border_frame, text=" √ ", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2",
                             command=lambda: self.get_operator(" √ "))
        btn_root.grid(row=5, column=0, columnspan=1, padx=1, pady=1)
        btn_root.config(font=("verdana", 14))

        btn_exponent = tk.Button(self.border_frame, text="x^y", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2",
                                 command=lambda: self.get_operator("x^y"))
        btn_exponent.grid(row=5, column=2, columnspan=1, padx=1, pady=1)
        btn_exponent.config(font=("verdana", 14))

        btn_sin = tk.Button(self.border_frame, text="sin", fg="Black", bg="lightgray", width=5, height=2, cursor="hand2",
                            command=self.calculate_sin)
        btn_sin.grid(row=3, column=4, columnspan=1, padx=1, pady=1)
        btn_sin.config(font=("verdana", 14))

        btn_cos = tk.Button(self.border_frame, text="cos", fg="Black", bg="lightgray", width=5, height=2, cursor="hand2",
                            command=self.calculate_cos)
        btn_cos.grid(row=4, column=4, columnspan=1, padx=1, pady=1)
        btn_cos.config(font=("verdana", 14))

        btn_backspace = tk.Button(self.border_frame, text="⌫", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2",
                                  command=self.backspace)
        btn_backspace.grid(row=2, column=4)
        btn_backspace.config(font=("verdana", 14))

        btn_decimal = tk.Button(self.border_frame, text=".", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2",
                                command=lambda: self.get_digit("."))
        btn_decimal.grid(row=5, column=4)
        btn_decimal.config(font=("verdana", 14))

        btn_cuberoot = tk.Button(self.border_frame, text=" ∛ ", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2",
                                 command=lambda: self.get_operator(" ∛ "))
        btn_cuberoot.grid(row=6, column=0, columnspan=1, padx=1, pady=1)
        btn_cuberoot.config(font=("verdana", 14))


    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()