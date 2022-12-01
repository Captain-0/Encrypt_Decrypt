from tkinter import *
from tkinter import messagebox
import base64
import os


def main_screen():
    screen = Tk()
    screen.geometry('380x398')

    image_icon = PhotoImage(file="image/lock_and_key.png")
    screen.iconphoto(False, image_icon)

    screen.title("ENCRYPT/DECRYPT")

    Label(text="ENTER TEXT FOR ENCRYPTION AND DECRYPTION", fg="blue", font=("Times new roman", 11)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=360, height=100)

    Label(text="ENTER SECRET KEY", fg="red", font=("Times new roman", 11)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=20, bd=0, font=('arial', 25), show="*").place(x=10, y=200)

    screen.mainloop()


main_screen()
