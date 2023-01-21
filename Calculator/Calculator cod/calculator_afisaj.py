import tkinter as tk
from tkinter import *

calculation = ""
a = ""


def add_to_calculation(symbol):
    global calculation
    global a
    calculation += str(symbol)
    text_rezults.delete(1.0, END)
    text_rezults.insert(1.0, calculation)
    a = str(calculation)


def evaluate_calculation():
    global calculation
    global text_afs
    global a
    try:
        calculation = str(eval(calculation))
        text_rezults.delete(1.0, END)
        text_rezults.insert('end', f"{a} = \n{float(calculation):.2f}")
        text_afs.insert('end', f"{a} = {float(calculation):.2f}")
        calculation = ""
    except:
        clear_field()
        text_rezults.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_rezults.delete(1.0, END)


root = tk.Tk()
root.geometry("500x290+650+300")
root.title("Calculator")
root.iconbitmap(r'calcicon.ico')
root.resizable(False, False)


text_rezults = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_rezults.grid(columnspan=5)

text_afs = tk.Listbox(root, height=11, width=16, font=('Arial', 16))
text_afs.grid(row=0, column=6, rowspan=8)
clear_field()
btn1 = tk.Button(root, text='1', command=lambda: add_to_calculation(1), width=5, font=('Arial', 14), borderwidth=1)
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text='2', command=lambda: add_to_calculation(2), width=5, font=('Arial', 14), borderwidth=1)
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text='3', command=lambda: add_to_calculation(3), width=5, font=('Arial', 14), borderwidth=1)
btn3.grid(row=2, column=3)
btn4 = tk.Button(root, text='4', command=lambda: add_to_calculation(4), width=5, font=('Arial', 14), borderwidth=1)
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text='5', command=lambda: add_to_calculation(5), width=5, font=('Arial', 14), borderwidth=1)
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text='6', command=lambda: add_to_calculation(6), width=5, font=('Arial', 14), borderwidth=1)
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text='7', command=lambda: add_to_calculation(7), width=5, font=('Arial', 14), borderwidth=1)
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text='8', command=lambda: add_to_calculation(8), width=5, font=('Arial', 14), borderwidth=1)
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text='9', command=lambda: add_to_calculation(9), width=5, font=('Arial', 14), borderwidth=1)
btn9.grid(row=4, column=3)
btn0 = tk.Button(root, text='0', command=lambda: add_to_calculation(0), width=5, font=('Arial', 14), borderwidth=1)
btn0.grid(row=5, column=2)

btn_plus = tk.Button(root, text='+', command=lambda: add_to_calculation('+'), width=5,
                     font=('Arial', 14), borderwidth=1)
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text='-', command=lambda: add_to_calculation('-'), width=5,
                      font=('Arial', 14), borderwidth=1)
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text='*', command=lambda: add_to_calculation('*'), width=5,
                         font=('Arial', 14), borderwidth=1)
btn_multiply.grid(row=4, column=4)
btn_impartire = tk.Button(root, text='/', command=lambda: add_to_calculation('/'), width=5,
                          font=('Arial', 14), borderwidth=1)
btn_impartire.grid(row=5, column=4)

btn_open = tk.Button(root, text='(', command=lambda: add_to_calculation('('), width=5,
                     font=('Arial', 14), borderwidth=1)
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=')', command=lambda: add_to_calculation(')'), width=5,
                      font=('Arial', 14), borderwidth=1)
btn_close.grid(row=5, column=3)

btn_egal = tk.Button(root, text='=', command=evaluate_calculation, width=5, font=('Arial', 14), borderwidth=1)
btn_egal.grid(row=6, column=4)

btn_pct = tk.Button(root, text='.', command=lambda: add_to_calculation('.'), width=5, font=('Arial', 14), borderwidth=1)
btn_pct.grid(row=6, column=3)

btn_clear = tk.Button(root, text='Clr', command=clear_field, width=5, font=('Arial', 14), borderwidth=1)
btn_clear.grid(row=6, column=2)

btn_exit = tk.Button(root, text='Exit', command=root.destroy, width=5, font=('Arial', 14), borderwidth=1)
btn_exit.grid(row=6, column=1)

root.mainloop()
