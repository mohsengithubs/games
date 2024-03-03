from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")


Round = 0
PlayerTurn = True


def DisableGame():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def ClickBtn(buttons):
    global PlayerTurn, Round, player1_name, player2_name
    if buttons["text"] == "" and PlayerTurn == True:
        buttons["text"] = "X"
        PlayerTurn = False
        CheckWin()
        Round += 1

    elif buttons["text"] == "" and PlayerTurn == False:
        buttons["text"] = "O"
        PlayerTurn = True

        CheckWin()
        Round += 1

    else:
        messagebox.showinfo("Tic-Tac-Toe", " this button already used")


def CheckWin():
    win_conditions = [
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9],
        [button1, button4, button7],
        [button2, button5, button8],
        [button3, button6, button9],
        [button1, button5, button9],
        [button3, button5, button7],
    ]

    for condition in win_conditions:
        if all([btn["text"] == "O" for btn in condition]):
            DisableGame()
            messagebox.showinfo("Tic-Tac-Toe", f"{player2_name.get()} Wins")
        elif all([btn["text"] == "X" for btn in condition]):
            DisableGame()
            messagebox.showinfo("Tic-Tac-Toe", f"{player1_name.get()} Wins")
            return

        if Round == 9:
            messagebox.showinfo("Tic-Tac-Toe", "GAME IS TIE")


label = Label(root, text="Player 1:", font=("arial", 20), bg="#113233")
label.grid(row=0, column=0)

player1_name = Entry(root, width=20, font=("arial", 20))
player1_name.grid(row=0, column=1)

label = Label(root, text="Player 2:", font=("arial", 20), bg="#113233")
label.grid(row=1, column=0)

player2_name = Entry(root, width=20, font=("arial", 20))
player2_name.grid(row=1, column=1)

root.geometry("620x620")

button1 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button1)
)
button1.grid(
    row=2,
    column=0,
    padx=2,
    pady=10,
)

button2 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button2)
)
button2.grid(row=2, column=1, padx=2, pady=10)

button3 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button3)
)
button3.grid(row=2, column=2, padx=2, pady=10)

button4 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button4)
)
button4.grid(row=3, column=0, padx=2, pady=10)

button5 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button5)
)
button5.grid(row=3, column=1, padx=2, pady=10)

button6 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button6)
)
button6.grid(row=3, column=2, padx=2, pady=10)

button7 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button7)
)
button7.grid(row=4, column=0, padx=2, pady=10)

button8 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button8)
)
button8.grid(row=4, column=1, padx=2, pady=10)

button9 = Button(
    root, text="", width=20, height=10, bg="gray", command=lambda: ClickBtn(button9)
)
button9.grid(row=4, column=2, padx=2, pady=10)


root.configure(bg="#113233")
root.resizable(False, False)
root.mainloop()
