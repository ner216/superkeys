#Class for program graphics VERSION 0.1

# Cameron last edited 1/23/25 - added everything you see here. <<< this is for whomever is writing documentation
# please don't delete comments that actually explain stuff, but you can remove the "babyyyyyys" and other poor
# attempts at making programming more fun, if and only if you wish.
"""
TO DO:
1) Shove all these functions into some class "game" or "note_rush" or similar*
* apologies, I still don't really understand classes yet. In due time.
2) Somehow tie the placeholder command to other python logic
3) Add background for main menu, somebody PLEASE FOR THE LOVE OF ALL THAT IS GOOD AND HOLY, DESIGN THIS**
** I am horrible at visual art, but I can help with audio.
** could just be some creative commons image
4) Making rows, columns, and grids prettier <<< might have to switch to .pack instead of .grid
5) Have fun
"""

# importing necessary modules
import tkinter as tk
from tkinter import ttk

# setup for main menu window
main = tk.Tk()
main.title("Note Rush")

# these lines might be Windows OSes only?
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenwidth()

# continuing setup
main.geometry(f"{screen_width}x{screen_height}")
main.maxsize(screen_width, screen_height)

# Game window function, babyyyyyy
# may be smarter to nestle this into a class in the near future
# This function/"future class" will likely end up being the largest chunk, but idk.
def game_window():
    game_menu = tk.Toplevel(main)
    game_menu.title("Note Rush")
    game_menu.geometry(f"{screen_width}x{screen_height}")

    play2_button = ttk.Button(game_menu, text="PLAY", command=loss_window).grid(row=0, column=0)
    quit_button = ttk.Button(game_menu, text="QUIT", command=game_menu.destroy).grid(row=0, column=1)


# Failstate window function, babyyyyyyyy
def loss_window():
    loss_menu = tk.Toplevel(main)
    loss_menu.title("Note Rush")
    loss_menu.geometry(f"{screen_width}x{screen_height}")

    replay_button = ttk.Button(loss_menu, text="PLAY AGAIN?", command=game_window).grid(row=1, column=1, sticky="N")
    ragequit_button = ttk.Button(loss_menu, text="QUIT", command=main.destroy).grid(row=1, column=2, sticky="N")

# A potential quit button function, use in conjunction with command
"""
def quit_button():
    eject_button = ttk.Button(master=None, text="QUIT", command=main.destroy).pack(padx=10, pady=10)
"""

""" It is important to note these functions must be defined PRIOR to using them as
commands in the main menu. It ain't pretty, and it ain't very readable, but that
is not what I do lol"""

# making the main menu pretty
game_title_screen = ttk.Label(main, text="NOTE RUSH").grid(row=0, column=1)
play_button = ttk.Button(main, text="PLAY", command=game_window).grid(row=1, column=1) #.pack(padx=10,pady=10)
kill_button = ttk.Button(main, text="QUIT", command=main.destroy).grid(row=2, column=1)

# ChatGPT's finest below for fullscreen
"""
main.attributes("-fullscreen", True)
def exit_fullscreen(event):
    main.attributes("-fullscreen", False)
main.bind("<Escape>", exit_fullscreen)
I don't trust this code in the slightest lol, but looks like it could be useful eventually
""" 

# method to actually run tkinter programs
main.mainloop()
