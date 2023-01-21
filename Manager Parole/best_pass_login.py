from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Login @ Best Pass App')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    file = open('data_storage.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        screen = Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello World', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()

    else:
        messagebox.showerror('Invalid', 'Utilizator sau parola gresita!')


img = PhotoImage(file='login1.png')
Label(root, image=img, bg='white').place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=500, y=50)
heading = Label(frame, text='Conectare', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# --------------------------------------------


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Nume utilizator')


user = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=40, y=80)
user.insert(0, "Nume utilizator")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=35, y=107)

# -------------------------------------------


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Parola')


code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
code.place(x=40, y=150)
code.insert(0, "Parola")
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=35, y=177)  # de aici se modifica linia neagra sub parola

# --------------------------------------------
Button(frame, width=39, pady=7, text='Autentificare', bg='#57a1f8', fg='white', border=0,
       command=signin).place(x=45, y=224)
label = Label(frame, text='Nu aveti un cont?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=10, text='Inregistrati-va!', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=271)

root.mainloop()
