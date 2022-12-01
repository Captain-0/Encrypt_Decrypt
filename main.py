from tkinter import *
from tkinter import messagebox
import base64
import os


def main_screen():
    screen = Tk()
    screen.geometry('375x398')

    image_icon = PhotoImage(file="image/lock_and_key.png")
    screen.iconphoto(False, image_icon)

    screen.title("ENCRYPT/DECRYPT")
    screen.mainloop()


main_screen()
