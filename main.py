from tkinter import *
from tkinter import messagebox
import base64
import os


def encrypt():
    password = code.get()

    if password == "admin":
        screen1 = Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.configure(bg='black')

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="black", bg='gray').place(x=10, y=0)
        text2 = Text(screen1, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password == '':
        messagebox.showerror("encryption", "Input Secret Key")

    elif password != "admin":
        messagebox.showerror("encryption", "Invalid Secret Key")




def decrypt():
    pass


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry('380x398')

    image_icon = PhotoImage(file="image/lock_and_key.png")
    screen.iconphoto(False, image_icon)

    screen.title("ENCRYPT/DECRYPT")

    def reset():
        code.set('')
        text1.delete(1.0, END)

    Label(text="ENTER TEXT FOR ENCRYPTION AND DECRYPTION", fg="blue", font=("Times new roman", 11)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=360, height=100)

    Label(text="ENTER SECRET KEY", fg="red", font=("Times new roman", 11)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=20, bd=0, font=('arial', 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height='2', width=23, bg='white', fg='black', bd=0, command=encrypt).place(x=10, y=253)
    Button(text="DECRYPT", height='2', width=23, bg="black", fg='white', bd=0, command=decrypt).place(x=200, y=253)
    Button(text="RESET", height='2', width=50, bg='grey', fg='black', bd=1, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
