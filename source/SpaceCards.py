# SpaceCards INDEV 0.2
# Author: Anthony Narlock
# anthonynarlock.com
# github.com/narlock/SpaceCards

# Date: 1/12/2022

import os
from card import Card
from Scraper import Scraper
from tkinter import *
from PIL import Image, ImageTk

class SpaceCards:
        
    def __init__(self):
        #Create welcome window
        self.root = Tk()
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.title("SpaceCards INDEV 0.2")
        self.root.iconbitmap("./assets/icon.ico")
        self.root['background'] = 'light grey'

        #Attributes
        self.deck_choice = ""
        self.cards = [Card("Front","Back")]
        self.current_card = self.cards[0]
        self.current_card_index = 0
        self.current_card_string = ""
        self.deck_choice = "null"
        self.import_deck_url = ""
        self.import_deck_name = ""

        #Creation of Main Window Frame
        self.frame0 = Frame(self.root)
        
        #Welcome Screen
        #Packed by default
        #pack forgotten once Start button is pressed
        logo = PhotoImage(file="./assets/logo.png")
        self.label = Label(self.frame0, image=logo)
        self.label['background'] = 'light grey'
        self.label.pack()
        self.title_label = Label(self.frame0, text="By: Anthony Narlock", padx=20, pady=20, font=("Tahoma",12,'bold'))
        self.title_label['background'] = 'light grey'
        self.title_label['foreground'] = 'black'
        self.title_label.pack()
        self.btn = Button(self.frame0, text="Start", width=8, command=self.start)
        self.btn['background'] = 'light blue'
        self.btn.pack()

        #Study Screen
        #Is packed once Start button is pressed
        #pack forgotten by default
        self.main_menu = Menu(self.root)
        self.root.config(menu = self.main_menu)

        self.current_deck_label = Label(self.frame0, text="No Deck Opened", padx=20, pady=20, font=("Tahoma",12,'bold'))
        self.current_deck_label['background'] = 'light grey'
        self.current_deck_label['foreground'] = 'red'
        self.current_deck_label.pack_forget()

        self.card_label = Button(self.frame0, text="Front", height=10, width=70, padx=20, pady=20, borderwidth=2, relief="solid", font=("Tahoma",12,"bold"), command=self.flip_card)
        self.card_label.pack_forget()

        self.next_btn = Button(self.frame0, text="Next Card", height=2, width=15, font=("Tahoma",12,"bold"), command=self.next)
        self.next_btn['background'] = 'pink'
        self.next_btn.pack_forget()

        self.frame0['background'] = 'light grey'
        self.frame0.pack()

        self.root.mainloop()

    #Starts the program
    def start(self):
        self.root.geometry("800x400")
        self.label.pack_forget()
        self.title_label.pack_forget()
        self.btn.pack_forget()

        self.main_menu.add_command(label="Select Deck", command=self.select_deck)
        self.main_menu.add_command(label="Import Deck", command=self.import_deck)
        self.current_deck_label.pack()
        self.card_label.pack() 
        self.next_btn.pack()

    #Selects the deck
    #Creates a new toplevel window, with options to select deck from list
    def select_deck(self):
        win = Toplevel()
        win.title("Select Deck")
        win.resizable(False, False)
        win.geometry("450x100")
        win.iconbitmap("./assets/icon.ico")
        instructions_label = Label(win, text="Select the Deck you want to study")
        instructions_label.pack()

        decks=os.listdir('./sample-decks')
        variable=StringVar(self.root)
        variable.set(decks[0])
        deck_menu = OptionMenu(win, variable, *decks)

        deck_menu['background'] = 'light blue'
        deck_menu.pack()

        def change_deck_variable():
            self.deck_choice = variable.get()

        import_btn = Button(win, text="Confirm Deck Selection", command=combine_funcs(change_deck_variable, self.change_deck, win.destroy))
        import_btn.pack()

    #Imports a deck from a website
    #Creates a new toplevel window, with options to import and instructions
    def import_deck(self):
        win = Toplevel()
        win.geometry("450x100")
        win.resizable(False, False)
        win.title("Import Deck")
        win.iconbitmap("./assets/icon.ico")
        instructions_label = Label(win, text="Paste Link in first Entry, Enter Name of Deck in second Entry")
        instructions_label.pack()
        import_entry = Entry(win,width=40)
        import_entry.pack()
        name_of_deck = Entry(win,width=40)
        name_of_deck.pack()

        def send_import_deck_information():
            self.import_deck_url = import_entry.get()
            self.import_deck_name = name_of_deck.get()

        import_btn = Button(win, text="Import Deck", command=combine_funcs(send_import_deck_information, self.import_deck_from_quizlet, win.destroy))
        import_btn.pack()

    #Method to use Scrapper
    def import_deck_from_quizlet(self):
        valid = True
        if(valid and len(self.import_deck_name) != 0):
            scraper = Scraper([])
            scraper.ql_to_cards(self.import_deck_url)
            scraper.write_cards_to_file(self.import_deck_name)
            print("Import Successful")
        else:
            print("Import unsuccessful")

    #Flips the card, updates the GUI
    def flip_card(self):
        if(self.current_card_string == self.current_card.back):
            self.card_label["text"] = self.current_card.front
            self.current_card_string = self.current_card.front
            self.spacing()
        else:
            self.card_label["text"] = self.current_card.back
            self.current_card_string = self.current_card.back
            self.spacing()
    
    #Selects the next card, updates the GUI
    def next(self):
        if(self.current_card_index == len(self.cards)-1):
            self.current_card_index = 0
            self.current_card = self.cards[self.current_card_index]
            self.card_label["text"] = self.current_card.front
            self.current_card_string = self.current_card.front
            self.spacing()
        else:
            print("current card index: " + str(self.current_card_index) + "\nlen(self.cards)-1: " + str(len(self.cards) -1))
            self.current_card_index = self.current_card_index + 1
            self.current_card = self.cards[self.current_card_index]
            self.card_label["text"] = self.current_card.front
            self.current_card_string = self.current_card.front
            self.spacing()

    #Changes the Deck
    def change_deck(self):
        #Get deck selection from option page
        print("Deck choice: " + self.deck_choice)
        
        #Set the cards
        opened_deck = open("./sample-decks/" + self.deck_choice, "r")
        self.current_deck_label["text"] = "Current Deck: " + self.deck_choice
        lines = opened_deck.readlines()
        lines = [line.rstrip() for line in lines]
        self.cards = []
        for line in lines:
            x = line.split(",")
            self.cards.append(Card(x[0],x[1]))

        #Init Deck
        self.current_card = self.cards[0]
        self.current_card_index = 0
        self.current_card_string = self.current_card.front
        self.card_label["text"] = self.current_card.front
        self.spacing()

    #Ensures that card spacing fits the label
    def spacing(self):
        if(len(self.card_label["text"]) > 80):
            #Split the label to fit the screen
            print("Resizing text")
            line = self.card_label["text"]
            self.card_label["text"] = ""
            n = 80
            lines = [line[i:i+n] for i in range(0, len(line), n)]
            for line in lines:
                if(line == lines[-1]):
                    self.card_label["text"] += line
                else:
                    self.card_label["text"] += line + "-\n"

#Main Function
def main():
    SpaceCards()

#Combine_funcs
#Allows for multiple functions to be enabled by GUI components
def combine_funcs(*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

if __name__ == "__main__":
    main()