from tkinter import *
from tkinter import messagebox
import random


def move_cancel_button():
    new_x = random.randint(10, 450)
    new_y = random.randint(10, 450)
    no_btn.place(x=new_x, y=new_y)


def show_second_message():
    messagebox.showinfo("message", "agree")


root = Tk()

Label(root, text="Do you agree that you are so stupid?", font=("ariaa", 40)).pack()

yes_btn = Button(
    root,
    text="Yes, i do",
    font=("arial", 20),
    bg="green",
    fg="black",
    command=show_second_message,
)
yes_btn.pack()
no_btn = Button(root, text="No , i don't", font=("arial", 13), bg="#f95678", fg="black")
no_btn.pack()

no_btn.bind("<Enter>", lambda e: move_cancel_button())

root.geometry("500x700")
root.title("Are you dump")
root.mainloop()
