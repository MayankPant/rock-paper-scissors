from tkinter import *
import random

window = Tk()
player1 = StringVar()
player1.set("Player1")
player2 = StringVar()
player2.set("Player2")
title_frame = Frame(window, padx=5, pady=5)
body_frame = Frame(window, padx=5, pady=5)
player1_frame = Frame(window, padx=5, pady=5)
player2_frame = Frame(window, padx=5, pady=5)
title_label = Label(title_frame, text="ROCK PAPER SCISSORS", foreground="Orange", height=3, font=("Bold", 20, ""))

player_label1 = Label(body_frame, textvariable=player1, foreground="Orange", height=3, font=("Bold", 20, ""))
player_label2 = Label(body_frame, textvariable=player2, foreground="Orange", height=3, font=("Bold", 20, ""))

title_label.grid(row=0, column=0)
title_frame.grid(row=0, column=0)
body_frame.grid(row=1, column=0)
player_label1.grid(row=0, columnspan=3, column=0)
player_label2.grid(row=0, columnspan=3, column=8)
player1_frame.grid(row=1, column=0, columnspan=6)
player2_frame.grid(row=1, column=6, columnspan=6)

player_label1.grid()
window.mainloop()
