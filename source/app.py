# SpaceCards GUI
# Author: Anthony Narlock

import os
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#Beginning of interface
root = tk.Tk()
root.title("SpaceCards")
root.resizable(False, False)

#All elements will be inside of this root object

#Canvas
canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=3)

#Logo
logo = Image.open("./assets/logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = tk.Label(root, text="Select a deck you would like to study", font="Tahoma")
instructions.grid(columnspan=3, column=0, row=1)

#List of Decks
decks = os.listdir('./sample-decks')
variable = StringVar(root)
variable.set(decks[0])

w = OptionMenu(root, variable, *decks)
w.grid(column=1, row=3)

start_button = Button(root, text="Begin Study")
start_button.grid(column = 1, row=4)




#Places window in middle of screen
#root.eval('tk::PlaceWindow . center')
#Ending of interface
root.mainloop()