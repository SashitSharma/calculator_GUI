
import tkinter as tk
import math
import numpy as np
import winsound

fNumber1 = fNumber2 = None


def get_digit(digit):
    current = result_label["text"]
    if "." in current and digit == ".":
        return
    new = current + str(digit)
    result_label.config(text=new)
    winsound.Beep(300, 100)


def backspace():
    current = result_label["text"]
    new = current[:-1]
    result_label.config(text=new)
    winsound.Beep(500, 100)


def clear():
    result_label.config(text=" ")
    equation_label.config(text=" ")
    winsound.Beep(500, 100)


def get_operator(op):
    global fNumber1, operator
    fNumber1 = float(result_label["text"])
    operator = op
    result_label.config(text="")
    equation_label.config(text=f"{fNumber1} {operator}")
    winsound.Beep(500, 100)


def calculate_sin():
    try:
        global fNumber1, operator
        fNumber1 = float(result_label["text"])
        angle_radians = math.radians(fNumber1)
        result = math.sin(angle_radians)
        result_label.config(text=f"Sine: {result:.4f}")
        equation_label.config(text=f"sin({fNumber1}) =")
        winsound.Beep(500, 100)
    except ValueError:
        result_label.config(text="Invalid input")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)


def calculate_cos():
    try:
        global fNumber1, operator
        fNumber1 = float(result_label["text"])
        angle_radians = math.radians(fNumber1)
        result = math.cos(angle_radians)
        result_label.config(text=f"Cosine: {result:.4f}")
        equation_label.config(text=f"cos({fNumber1}) =")
        winsound.Beep(500, 100)
    except ValueError:
        result_label.config(text="Invalid input")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)


def get_result():
    global fNumber1, fNumber2, operator

    if operator == " √ ":
        try:
            root_square = round(math.sqrt(fNumber1), 5)
            result_label.config(text=str(root_square))
            equation_label.config(text=f"√({fNumber1}) =")
            winsound.Beep(500, 100)
        except ValueError:
            result_label.config(text="Error")
            equation_label.config(text="")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    elif operator == " ∛ ":
        try:
            root_cube = round(np.cbrt(fNumber1), 5)
            result_label.config(text=str(root_cube))
            equation_label.config(text=f"∛({fNumber1}) =")
            winsound.Beep(500, 100)
        except ValueError:
            result_label.config(text="Error")
            equation_label.config(text="")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    elif operator == "+":
        fNumber2 = float(result_label["text"])
        result_label.config(text=str(fNumber1 + fNumber2))
        equation_label.config(text=f"{fNumber1} + {fNumber2} =")
        winsound.Beep(500, 100)

    elif operator == "-":
        fNumber2 = float(result_label["text"])
        result_label.config(text=str(fNumber1 - fNumber2))
        equation_label.config(text=f"{fNumber1} - {fNumber2} =")
        winsound.Beep(500, 100)

    elif operator == "*":
        fNumber2 = float(result_label["text"])
        result_label.config(text=str(fNumber1 * fNumber2))
        equation_label.config(text=f"{fNumber1} * {fNumber2} =")
        winsound.Beep(500, 100)

    elif operator == "x^y":
        fNumber2 = float(result_label["text"])
        result_label.config(text=str(fNumber1 ** fNumber2))
        equation_label.config(text=f"{fNumber1} ^ {fNumber2} =")
        winsound.Beep(500, 100)

    else:
        fNumber2 = float(result_label["text"])
        if fNumber2 == 0:
            result_label.config(text="Error")
            equation_label.config(text="")
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        else:
            result_label.config(text=str(round(fNumber1 / fNumber2, 5)))
            equation_label.config(text=f"{fNumber1} / {fNumber2} =")
            winsound.Beep(500, 100)

win = tk.Tk()
win.geometry("380x485")
win.resizable(0, 0)
win.title("in-tech Calculator")
win.configure(background="Black")

border_frame = tk.Frame(win, borderwidth=2, relief=tk.GROOVE, background="Black")
border_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

result_label = tk.Label(border_frame, text="", bg="Black", fg="white")
result_label.grid(row=1, column=0, columnspan=10, pady=(50, 25), sticky="w")
result_label.config(font=("verdana", 20, "bold"))

equation_label = tk.Label(border_frame, text="", bg="Black", fg="turquoise1")
equation_label.grid(row=0, column=0, columnspan=10, pady=(0, 5), sticky="w")
equation_label.config(font=("Arial", 12))

btn_7 = tk.Button(border_frame, text="7", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(7))
btn_7.grid(row=2, column=0)
btn_7.config(font=("verdana", 14))

btn_8 = tk.Button(border_frame, text="8", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(8))
btn_8.grid(row=2, column=1)
btn_8.config(font=("verdana", 14))

btn_9 = tk.Button(border_frame, text="9", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(9))
btn_9.grid(row=2, column=2)
btn_9.config(font=("verdana", 14))

btn_add = tk.Button(border_frame, text="+", fg="Black", bg="lightgreen", width=5, height=2, cursor="hand2", command=lambda: get_operator("+"))
btn_add.grid(row=2, column=3)
btn_add.config(font=("verdana", 14))

btn_4 = tk.Button(border_frame, text="4", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(4))
btn_4.grid(row=3, column=0)
btn_4.config(font=("verdana", 14))

btn_5 = tk.Button(border_frame, text="5", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(5))
btn_5.grid(row=3, column=1)
btn_5.config(font=("verdana", 14))

btn_6 = tk.Button(border_frame, text="6", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(6))
btn_6.grid(row=3, column=2)
btn_6.config(font=("verdana", 14))

btn_minus = tk.Button(border_frame, text="-", fg="Black", bg="lightGreen", width=5, height=2, cursor="hand2", command=lambda: get_operator("-"))
btn_minus.grid(row=3, column=3)
btn_minus.config(font=("verdana", 14))

btn_1 = tk.Button(border_frame, text="1", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(1))
btn_1.grid(row=4, column=0)
btn_1.config(font=("verdana", 14))

btn_2 = tk.Button(border_frame, text="2", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(2))
btn_2.grid(row=4, column=1)
btn_2.config(font=("verdana", 14))

btn_3 = tk.Button(border_frame, text="3", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(3))
btn_3.grid(row=4, column=2)
btn_3.config(font=("verdana", 14))

btn_multiply = tk.Button(border_frame, text="*", fg="Black", bg="lightGreen", width=5, height=2, cursor="hand2", command=lambda: get_operator("*"))
btn_multiply.grid(row=4, column=3)
btn_multiply.config(font=("verdana", 14))

btn_clear = tk.Button(border_frame, text="C", fg="Black", bg="crimson", width=11, height=2, cursor="hand2", command=lambda: clear())
btn_clear.grid(row=6, column=1, columnspan=2)
btn_clear.config(font=("verdana", 14))

btn_0 = tk.Button(border_frame, text="0", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(0))
btn_0.grid(row=5, column=1)
btn_0.config(font=("verdana", 14))

btn_equal = tk.Button(border_frame, text="=", fg="Black", bg="violet", width=11, height=2, cursor="hand2", command=get_result)
btn_equal.grid(row=6, column=3, columnspan=2)
btn_equal.config(font=("verdana", 14))

btn_divide = tk.Button(border_frame, text="/", fg="Black", bg="lightGreen", width=5, height=2, cursor="hand2", command=lambda: get_operator("/"))
btn_divide.grid(row=5, column=3)
btn_divide.config(font=("verdana", 14))

btn_root = tk.Button(border_frame, text=" √ ", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2", command=lambda: get_operator(" √ "))
btn_root.grid(row=5, column=0, columnspan=1, padx=1, pady=1)
btn_root.config(font=("verdana", 14))

btn_exponent = tk.Button(border_frame, text="x^y", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2", command=lambda: get_operator("x^y"))
btn_exponent.grid(row=5, column=2, columnspan=1, padx=1, pady=1)
btn_exponent.config(font=("verdana", 14))

btn_sin = tk.Button(border_frame, text="sin", fg="Black", bg="lightgray", width=5, height=2, cursor="hand2", command=calculate_sin)
btn_sin.grid(row=3, column=4, columnspan=1, padx=1, pady=1)
btn_sin.config(font=("verdana", 14))

btn_cos = tk.Button(border_frame, text="cos", fg="Black", bg="lightgray", width=5, height=2, cursor="hand2", command=calculate_cos)
btn_cos.grid(row=4, column=4, columnspan=1, padx=1, pady=1)
btn_cos.config(font=("verdana", 14))

btn_backspace = tk.Button(border_frame, text="⌫", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2", command=backspace)
btn_backspace.grid(row=2, column=4)
btn_backspace.config(font=("verdana", 14))

btn_decimal = tk.Button(border_frame, text=".", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit("."))
btn_decimal.grid(row=5, column=4)
btn_decimal.config(font=("verdana", 14))

btn_cuberoot = tk.Button(border_frame, text=" ∛ ", fg="Black", bg="lightblue", width=5, height=2, cursor="hand2", command=lambda: get_operator(" ∛ "))
btn_cuberoot.grid(row=6, column=0, columnspan=1, padx=1, pady=1)
btn_cuberoot.config(font=("verdana", 14))

border_frame.mainloop()