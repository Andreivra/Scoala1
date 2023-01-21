import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast
import os

root = Tk()
root.title('Login @ Best Pass App')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# ----------------------------------------------------------------------- deschidere pagina adaugare


def signin():
    username = user.get()
    password = code.get()

    file = open('data_storage.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        def add():
            d_name = domain.get()
            u_name = user1.get()
            pwd = pass1.get()
            file1 = "passwords.txt"
            file1_path = os.path.join(os.getcwd(), file1)
            with open(file1, 'a') as f:
                f.write("Domeniu: " + d_name + " | " + "User: " + u_name + " | " + "Parola: " + pwd + "\n")
            os.system(f'attrib +h {file1_path}')
            messagebox.showinfo("Success", "Detaliile au fost salvate cu succes!")

        def view():
            with open('passwords.txt', 'r') as f:
                data = f.read()
                messagebox.showinfo("Detalii parole", data)
                display_data()

        def display_data():
            listbox.delete(0, tk.END)
            with open("passwords.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    d_name, u_name, pwd = line.strip().split("|")
                    listbox.insert(tk.END, d_name + ": " + u_name + ": " + pwd)

        screen = Toplevel(root)
        screen.title('Best pass v.1.5')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')
        screen.resizable(False, False)
        heading1 = Label(screen, text='Va rugam sa introduceti detaliile contului pentru salvare', fg='#69c7ab',
                         bg='white', font=('Microsoft YaHei UI Light', 20, 'bold'))
        heading1.place(x=100, y=5)
        img1 = PhotoImage(file='save_data.png')
        Label(screen, image=img1, bg='white').place(x=680, y=80)
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

        pass1 = Entry(screen, width=30, fg='black', border=1, bg='white', font=('Microsoft YaHei UI Light', 11),
                      show='*')
        pass1.place(x=80, y=240)
        pass1.insert(0, "")
        pass1_label = Label(screen, text='Introduceti parola', fg='black', bg='white',
                            font=('Microsoft YaHei UI Light', 16, 'bold'))
        pass1_label.place(x=350, y=235)

        # --------------------------------------------------------------------------------------------------------------

        Button(screen, width=30, pady=7, text='Salvare', bg='#69c7ab', fg='white', border=0,
               command=add).place(x=75, y=420)
        Button(screen, width=30, pady=7, text='Vizualizare', bg='#69c7ab', fg='white',
               border=0, command=view).place(x=375, y=420)
        Button(screen, width=30, pady=7, text='Inchide', bg='#69c7ab', fg='white', border=0,
               command=lambda: [root.deiconify(), screen.destroy()]).place(x=675, y=420)

        # --------------------------------------------------------------------------------------------------------------

        listbox = Listbox(screen)
        screen.mainloop()
    else:
        messagebox.showerror('Invalid', 'Utilizator sau parola gresita!')

# ------------------------------------------------------------------------------------------------


def sign_up_comand():
    window = Toplevel(root)
    window.title("Inregistrare utilizator")
    window.geometry('925x500+300+200')
    window.config(bg='#fff')
    window.resizable(False, False)

    def signup():
        username = user1.get()
        password = code1.get()
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
                window.destroy()
            except:
                file = open('data_storage.txt', 'w')
                pp = str({'Username': 'Password'})
                file.write(pp)
                file.close()
        else:
            messagebox.showerror('Invalid', "Ambele parole trebuie sa coincida!")

    def sign():
        window.destroy()

    img1 = PhotoImage(file='signup.png')
    Label(window, image=img1, border=0, bg='white').place(x=50, y=50)

    frame1 = Frame(window, width=350, height=390, bg='white')
    frame1.place(x=500, y=50)
    heading1 = Label(frame1, text='Inregistrare', fg='#69c7ab', bg='white',
                     font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading1.place(x=100, y=5)

    # --------------------------------------------------------------------------------

    def on_enter1(e):
        user1.delete(0, 'end')

    def on_leave1(e):
        name = user1.get()
        if name == '':
            user1.insert(0, 'Nume utilizator')

    user1 = Entry(frame1, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    user1.place(x=40, y=80)
    user1.insert(0, "Nume utilizator")
    user1.bind('<FocusIn>', on_enter1)
    user1.bind('<FocusOut>', on_leave1)
    Frame(frame1, width=295, height=2, bg='black').place(x=35, y=107)  # de aici se modifica linia neagra sub user

    # --------------------------------------------------------------------------------

    def on_enter1(e):
        code1.delete(0, 'end')

    def on_leave1(e):
        name = code1.get()
        if name == '':
            code1.insert(0, 'Parola')

    code1 = Entry(frame1, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
    code1.place(x=40, y=150)
    code1.insert(0, "Parola")
    code1.bind('<FocusIn>', on_enter1)
    code1.bind('<FocusOut>', on_leave1)
    Frame(frame1, width=295, height=2, bg='black').place(x=35, y=177)

    # --------------------------------------------------------------------------------

    def on_enter1(e):
        c_code.delete(0, 'end')

    def on_leave1(e):
        name = c_code.get()
        if name == '':
            c_code.insert(0, 'Verificare')

    c_code = Entry(frame1, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
    c_code.place(x=40, y=220)
    c_code.insert(0, "Verificare")
    c_code.bind('<FocusIn>', on_enter1)
    c_code.bind('<FocusOut>', on_leave1)
    Frame(frame1, width=295, height=2, bg='black').place(x=35, y=247)
    # --------------------------------------------------------------------------------

    Button(frame1, width=39, pady=7, text='Inregistrare', bg='#69c7ab', fg='white', border=0,
           command=signup).place(x=35, y=280)
    label1 = Label(frame1, text='Aveti deja un cont?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label1.place(x=90, y=340)

    signin1 = Button(frame1, width=10, text='Autentificare', border=0, bg='white', cursor='hand2', fg='#69c7ab',
                     command=sign)
    signin1.place(x=215, y=341)

    window.mainloop()


img = PhotoImage(file='login1.png')
Label(root, image=img, bg='white').place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=500, y=50)
heading = Label(frame, text='Conectare', fg='#69c7ab', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
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
Frame(frame, width=295, height=2, bg='black').place(x=35, y=107)  # de aici se modifica linia neagra sub user

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
Button(frame, width=39, pady=7, text='Autentificare', bg='#69c7ab', fg='white', border=0,
       command=lambda: [root.withdraw(), signin()]).place(x=45, y=224)
label = Label(frame, text='Nu aveti un cont?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)
sign_up = Button(frame, width=10, text='Inregistrati-va!', border=0, bg='white', cursor='hand2', fg='#69c7ab',
                 command=sign_up_comand)
sign_up.place(x=215, y=271)

close_button = Button(root, width=29, pady=7, text='Inchide aplicatie!', border=0, bg='white',
                      cursor='hand2', fg='black', font=('Microsoft YaHei UI Light', 9), command=root.destroy)
close_button.place(x=155, y=404)

if root.deiconify() == True:
    root.destroy()

root.mainloop()
