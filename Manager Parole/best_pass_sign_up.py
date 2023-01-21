from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title("Inregistrare utilizator")
window.geometry('925x500+300+200')
window.config(bg='#fff')
window.resizable(False, False)


def signup():
    username = user.get()
    password = code.get()
    c_password = c_code.get()

    if password == c_password:
        try:
            file = open('data_storage.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('data_storage.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Inregistrare', 'Inregistrare cu succes!')
        except:
            file = open('data_storage.txt', 'w')
            pp = str({'Username': 'Password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Invalid', "Ambele parole trebuie sa coincida!")


def sign():
    window.destroy()
img = PhotoImage(file='login.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='white')
frame.place(x=500, y=50)
heading = Label(frame, text='Inregistrare', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)
# --------------------------------------------------------------------------------


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
Frame(frame, width=295, height=2, bg='black').place(x=35, y=107)  # de aici se modifica linia neagra sub user
# --------------------------------------------------------------------------------


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
Frame(frame, width=295, height=2, bg='black').place(x=35, y=177)
# --------------------------------------------------------------------------------


def on_enter(e):
    c_code.delete(0, 'end')


def on_leave(e):
    name = c_code.get()
    if name == '':
        c_code.insert(0, 'Verificare')


c_code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
c_code.place(x=40, y=220)
c_code.insert(0, "Verificare")
c_code.bind('<FocusIn>', on_enter)
c_code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=35, y=247)
# --------------------------------------------------------------------------------

Button(frame, width=39, pady=7, text='Inregistrare', bg='#57a1f8', fg='white', border=0,
       command=signup).place(x=35, y=280)
label = Label(frame, text='Aveti deja un cont?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=10, text='Autentificare', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=sign)
signin.place(x=215, y=341)

window.mainloop()
