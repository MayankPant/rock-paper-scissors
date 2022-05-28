from tkinter import *
from tkinter import messagebox
import random

window = Tk()

player1 = StringVar()
player1.set("Player1")
player2 = StringVar()
player2.set("Player2")

score1 = IntVar()
score1.set(0)
score2 = IntVar()
score2.set(0)


def get_details(games = 3, player1_name = "Player 1", player2_name = "Player 2"):
    no_of_games = games
    player1.set(player1_name)
    player2.set(player2_name)
    game_details.destroy()



def configure():
    global game_details
    game_details = Toplevel()
    frame = Frame(game_details, padx=5, pady=5)

    no_of_games = Label(frame, text="Enter No of Games to be played :", font=("helvetica", 10, "bold"),
                        foreground="Orange")
    entry_1 = Entry(frame, width=20)
    player1_label = Label(frame, text="Enter name for player 1", font=("helvetica", 10, "bold"), foreground="Orange")
    entry_2 = Entry(frame, width=20)
    player2_label = Label(frame, text="Enter name for player 2", font=("helvetica", 10, "bold"), foreground="Orange")
    entry_3 = Entry(frame, width=20)

    ok_button = Button(frame, text="OK", foreground="Orange", width=10, padx=2, pady=2,
                       command=lambda: get_details(int(entry_1.get()), entry_2.get(), entry_3.get()))

    frame.pack()
    no_of_games.grid(row=0, column=0,padx=5,pady=10)
    entry_1.grid(row=0, column=1,padx=5,pady=10)
    player1_label.grid(row=1, column=0,padx=5,pady=10)
    entry_2.grid(row=1, column=1,padx=5,pady=10)
    player2_label.grid(row=2, column=0,padx=5,pady=10)
    entry_3.grid(row=2, column=1,padx=5,pady=10)
    ok_button.grid(row=3, column=0, columnspan=2,padx=5,pady=10)

def start_the_game():
    pass

title_frame = Frame(window, padx=5, pady=5)
body_frame = Frame(window, padx=5, pady=5)
player1_frame = Frame(window, padx=5, pady=5)
player2_frame = Frame(window, padx=5, pady=5)
title_label = Label(title_frame, text="ROCK PAPER SCISSORS", foreground="Orange", height=3,
                    font=("helvetica", 20, "bold"))

player_label1 = Label(body_frame, textvariable=player1, foreground="Orange", height=3, font=("helvetica", 20, "bold"))
player_label2 = Label(body_frame, textvariable=player2, foreground="Orange", height=3, font=("helvetica", 20, "bold"))

score_label1 = Label(body_frame, textvariable=score1, foreground="Orange", height=3, font=("helvetica", 20, "bold"))
score_label2 = Label(body_frame, textvariable=score2, foreground="Orange", height=3, font=("helvetica", 20, "bold"))

start_button = Button(body_frame, text="START", foreground="Orange", font=("bold", 15, ""), command=start_the_game)
configure_button = Button(body_frame, text="CONFIG", foreground="Orange", font=("bold", 10, ""), command=configure)

title_label.grid(row=0, column=0)
title_frame.grid(row=0, column=0)
body_frame.grid(row=1, column=0)
player_label1.grid(row=0, columnspan=4, column=1)
player_label2.grid(row=0, columnspan=4, column=8)
player1_frame.grid(row=1, column=0, columnspan=6,rowspan=3)
player2_frame.grid(row=1, column=7, columnspan=6,rowspan=3)
score_label1.grid(row=4, column=4)
score_label2.grid(row=4, column=10)
start_button.grid(row=4, column=6, columnspan=2)
configure_button.grid(row=5,column=12)
player_label1.grid()
window.mainloop()
