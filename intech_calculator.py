import tkinter as tk
import math

number1 = number2 = operator = None

def get_digit(digit):
    current = result_label["text"]
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text=" ")
    equation_label.config(text=" ")


def get_operator(op):
    global number1, operator
    number1 = int(result_label["text"])
    operator = op
    result_label.config(text="")
    equation_label.config(text=f"{number1} {operator}")


def calculate_sin():
    try:
        global number1, operator
        number1 = int(result_label["text"])
        angle_radians = math.radians(number1)
        result = math.sin(angle_radians)
        result_label.config(text=f"Sine: {result:.4f}")
        equation_label.config(text=f"sin({number1}) =")
    except ValueError:
        result_label.config(text="Invalid input")


def calculate_cos():
    try:
        global number1, operator
        number1 = int(result_label["text"])
        angle_radians = math.radians(number1)
        result = math.cos(angle_radians)
        result_label.config(text=f"Cosine: {result:.4f}")
        equation_label.config(text=f"cos({number1}) =")
    except ValueError:
        result_label.config(text="Invalid input")


def get_result():
    global number1, number2, operator

    if operator == " √ ":
        try:
            root_square = round(math.sqrt(number1), 5)
            result_label.config(text=str(root_square))
            equation_label.config(text=f"√({number1}) =")
        except ValueError:
            result_label.config(text="Error")
            equation_label.config(text="")

    elif operator == "+":
        number2 = int(result_label["text"])
        result_label.config(text=str(number1 + number2))
        equation_label.config(text=f"{number1} + {number2} =")

    elif operator == "-":
        number2 = int(result_label["text"])
        result_label.config(text=str(number1 - number2))
        equation_label.config(text=f"{number1} - {number2} =")

    elif operator == "*":
        number2 = int(result_label["text"])
        result_label.config(text=str(number1 * number2))
        equation_label.config(text=f"{number1} * {number2} =")

    elif operator == "x^y":
        number2 = int(result_label["text"])
        result_label.config(text=str(number1 ** number2))
        equation_label.config(text=f"{number1} ^ {number2} =")

    else:
        number2 = int(result_label["text"])
        if number2 == 0:
            result_label.config(text="Error")
            equation_label.config(text="")
        else:
            result_label.config(text=str(round(number1 / number2, 5)))
            equation_label.config(text=f"{number1} / {number2} =")


win = tk.Tk()
win.geometry("300x485")
win.resizable(0, 0)
win.title("in-tech Calculator")
win.configure(background="teal")

border_frame = tk.Frame(win, borderwidth=2, relief=tk.GROOVE, background="maroon")
border_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

result_label = tk.Label(border_frame, text="", bg="maroon", fg="white")
result_label.grid(row=1, column=0, columnspan=10, pady=(50, 25), sticky="w")
result_label.config(font=("verdana", 20, "bold"))

equation_label = tk.Label(border_frame, text="", bg="maroon", fg="white")
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

btn_clear = tk.Button(border_frame, text="C", fg="Black", bg="crimson", width=5, height=2, cursor="hand2", command=lambda: clear())
btn_clear.grid(row=6, column=0, columnspan=1)
btn_clear.config(font=("verdana", 14))

btn_0 = tk.Button(border_frame, text="0", fg="Black", bg="Skyblue", width=5, height=2, cursor="hand2", command=lambda: get_digit(0))
btn_0.grid(row=5, column=1)
btn_0.config(font=("verdana", 14))

btn_equal = tk.Button(border_frame, text="=", fg="Black", bg="violet", width=5, height=2, cursor="hand2", command=get_result)
btn_equal.grid(row=6, column=3, columnspan=1)
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
btn_sin.grid(row=6, column=1, columnspan=1, padx=1, pady=1)
btn_sin.config(font=("verdana", 14))

btn_cos = tk.Button(border_frame, text="cos", fg="Black", bg="lightgray", width=5, height=2, cursor="hand2", command=calculate_cos)
btn_cos.grid(row=6, column=2, columnspan=1, padx=1, pady=1)
btn_cos.config(font=("verdana", 14))

border_frame.mainloop()
