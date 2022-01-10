# SpaceCards
# Author: Anthony Narlock

import os
from tkinter import *
from PIL import Image, ImageTk

def make_label(parent, img):
    label = Label(parent, image=img)
    label.pack()

def run():

    #Set Up Window
    root = Tk()
    root.title("SpaceCards")
    root.resizable(False, False)

    #Image row
    frame0 = Frame(root, width=600, height=600)
    logo = PhotoImage(file="./assets/logo.png")
    make_label(frame0, logo)
    title_label = Label(frame0, text="By: Anthony Narlock", font="Tahoma").pack()
    frame0.pack()

    #Line row
    frame_line1 = Frame(root)
    line = Label(frame_line1, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n").pack()
    frame_line1.pack()

    #Instruction row
    frame1 = Frame(root)
    instructions = Label(frame1, text="Select a deck you wish to study", font="Tahoma").pack()
    
    decks = os.listdir('./sample-decks')
    variable = StringVar(root)
    variable.set(decks[0])
    w = OptionMenu(frame1, variable, *decks).pack()
    frame1.pack()

    #Line row2
    frame_line2 = Frame(root)
    line = Label(frame_line2, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n").pack()
    frame_line2.pack()

    #todo
    #Make new frame for current deck
    #allow for functionality to look through deck
    #next card, previous card, random card
    #flip card button

    root.eval('tk::PlaceWindow . center')
    root.mainloop()

def main():
    run()

if __name__ == "__main__":
    main()