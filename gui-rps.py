from tkinter import *
import random


window = Tk()
title_frame = Frame(window, padx=5, pady = 5)
body_frame = Frame(window, padx = 5, pady=5)
title_label = Label(title_frame, text="ROCK PAPER SCISSORS", foreground="Orange", height=3, font = ("Bold",20,""))


title_label.grid(row=0, column=0)
title_frame.grid(row=0, column=0)
body_frame.grid(row=1, column=0)
window.mainloop()