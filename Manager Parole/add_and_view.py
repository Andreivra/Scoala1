import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title('Adaugare @ Best Pass App')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def add():
    d_name = domain.get()
    u_name = user1.get()
    pwd = pass1.get()
    file = "passwords.txt"
    file_path = os.path.join(os.getcwd(), file)
    with open(file, 'a') as f:
        f.write("Domeniu: " + d_name + " | " + "User: " + u_name + " | " + "Parola: " + pwd + "\n")
    os.system(f'attrib +h {file_path}')
    messagebox.showinfo("Success", "Detaliile au fost salvate cu succes!")


def view():
    with open('passwords.txt', 'r') as f:
        data = f.read()
        messagebox.showinfo("Passwords", data)
        display_data()


def display_data():
    listbox.delete(0, tk.END)
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            d_name, u_name, pwd = line.strip().split("|")
            listbox.insert(tk.END, d_name + ": " + u_name + ": " + pwd)


screen = root  # aici era Toplevel(root)
screen.title('Best pass v.1.5')
screen.geometry('925x500+300+200')
screen.config(bg='white')

heading = Label(screen, text='Va rugam sa introduceti detaliile contului pentru salvare', fg='#69c7ab', bg='white',
                font=('Microsoft YaHei UI Light', 20, 'bold'))
heading.place(x=100, y=5)

img = PhotoImage(file='save_data.png')
Label(root, image=img, bg='white').place(x=680, y=80)
# --------------------------------------------------------------------------------------------------------------

user1 = Entry(screen, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
user1.place(x=80, y=80)
user1.insert(0, "")

user_label = Label(screen, text='Introduceti domeniul', fg='black', bg='white',
                   font=('Microsoft YaHei UI Light', 16, 'bold'))
user_label.place(x=350, y=75)

# --------------------------------------------------------------------------------------------------------------

domain = Entry(screen, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
domain.place(x=80, y=160)
domain.insert(0, "")

domain_label = Label(screen, text='Introduceti nume utilizator', fg='black', bg='white',
                     font=('Microsoft YaHei UI Light', 16, 'bold'))
domain_label.place(x=350, y=155)

# --------------------------------------------------------------------------------------------------------------

pass1 = Entry(screen, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
pass1.place(x=80, y=240)
pass1.insert(0, "")

pass1_label = Label(screen, text='Introduceti parola', fg='black', bg='white',
                    font=('Microsoft YaHei UI Light', 16, 'bold'))
pass1_label.place(x=350, y=235)

# --------------------------------------------------------------------------------------------------------------

Button(screen, width=30, pady=7, text='Salvare', bg='#69c7ab', fg='white', border=0, command=add).place(x=75, y=420)

Button(screen, width=30, pady=7, text='Vizualizare', bg='#69c7ab', fg='white',
       border=0, command=view).place(x=375, y=420)

Button(screen, width=30, pady=7, text='Inchide', bg='#69c7ab', fg='white', border=0,
       command=screen.destroy).place(x=675, y=420)

# --------------------------------------------------------------------------------------------------------------
listbox = tk.Listbox(root)

screen.mainloop()
