# SpaceCards INDEV 0.2.1
# Author: Anthony Narlock
# anthonynarlock.com
# github.com/narlock/SpaceCards

# Date: 1/17/2022

import os
import random
from unittest.mock import sentinel
from card import Card
from Scraper import Scraper
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

class SpaceCards:
        
    def __init__(self):
        #Create welcome window
        self.root = Tk()
        self.root.geometry("400x385")
        self.root.resizable(False, False)
        self.root.title("SpaceCards INDEV 0.2.1")
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
        
        self.filename = ""
        self.profile_attributes = []
        self.profile_name = ""

        self.random_index = 0
        self.deck_size = 0
        self.remaining_cards = 0
        self.seen_cards = []

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
        self.btn = Button(self.frame0, text="Start", width=8,command=self.start)
        self.btn['background'] = 'light blue'
        self.btn.pack()
        self.create_profile_btn = Button(self.frame0, text="Create Profile", width=10,command=self.create_profile)
        self.create_profile_btn['background'] = 'light blue'
        self.create_profile_btn.pack()

        #Study Screen
        #Is packed once Start button is pressed
        #pack forgotten by default
        self.main_menu = Menu(self.root)
        self.root.config(menu = self.main_menu)

        self.profile_name_label = Label(self.frame0, text="",font=("Tahoma",10))
        self.profile_name_label['background'] = 'light grey'
        self.profile_name_label['foreground'] = 'black'
        self.profile_name_label.pack_forget()

        self.current_deck_label = Label(self.frame0, text="No Deck Opened", padx=20, pady=20, font=("Tahoma",12,'bold'))
        self.current_deck_label['background'] = 'light grey'
        self.current_deck_label['foreground'] = 'purple'
        self.current_deck_label.pack_forget()

        self.card_label = Button(self.frame0, text="Front", height=10, width=70, padx=20, pady=20, borderwidth=2, relief="solid", font=("Tahoma",12), command=self.flip_card)
        self.card_label.pack_forget()

        self.next_btn = Button(self.frame0, text="Next Card", height=2, width=15, font=("Tahoma",12,"bold"), command=self.next)
        self.next_btn['background'] = 'pink'
        self.next_btn.pack_forget()

        self.random_btn = Button(self.frame0, text="Random Card", height=2, width=15, font=("Tahoma",12,"bold"), command=self.random_card)
        self.random_btn['background'] = 'pink'
        self.random_btn.pack_forget()

        self.space_mode = Button(self.frame0, text="Space Mode", height=2, width=15, font=("Tahoma",12,"bold"), command=self.set_space_mode)
        self.space_mode['background'] = 'pink'
        self.space_mode.pack_forget()

        self.learn_mode = Button(self.frame0, text="Learn Mode", height=2, width=15, font=("Tahoma",12,"bold"), command=self.set_learn_mode)
        self.learn_mode['background'] = 'pink'
        self.learn_mode.pack_forget()

        self.test_label = Label(self.frame0, text="👽", font=("Arial",40))
        self.test_label['foreground'] = 'green'
        self.test_label['background'] = 'light grey'
        self.test_label.pack_forget()

        self.frame0['background'] = 'light grey'
        self.frame0.pack()

        self.root.mainloop()

    #Starts the program
    def start(self):
        self.filename = askopenfilename()
        if(self.filename == ""):
            self.filename = "./profiles/default.txt"
        print(self.filename)
        self.read_profile_file()
        
        self.root.geometry("800x425")
        self.label.pack_forget()
        self.title_label.pack_forget()
        self.btn.pack_forget()
        self.create_profile_btn.pack_forget()

        self.main_menu.add_command(label="Select Deck", command=self.select_deck)
        self.main_menu.add_command(label="Import Deck", command=self.import_deck)
        self.main_menu.add_command(label="Create New Deck", command=self.create_new_deck)
        self.profile_name_label.pack()
        self.current_deck_label.pack()
        self.card_label.pack() 
        self.next_btn.pack(side=LEFT)
        self.random_btn.pack(side=LEFT)
        self.space_mode.pack(side=RIGHT)
        self.learn_mode.pack(side=RIGHT)
        self.test_label.pack()

    def read_profile_file(self):
        #Read profile information
        file = open(self.filename)
        lines = file.readlines()
        self.cards = []
        for line in lines:
            self.profile_attributes.append(line)
        #Set profile attributes
        self.profile_name = self.profile_attributes[0]
        self.profile_name_label['text'] = self.profile_name

    #TODO Opens dialog window to create a profile, will write profile information to file
    def create_profile(self):
        pass

    #TODO Opens the spaced repetition mode
    #can't enter if no deck
    def set_space_mode(self):
        pass

    #TODO Opens the learn mode - essentially quizlet's Learn mode, but for SpaceCards
    #You won't be able to enter if your deck has less than 4 cards
    def set_learn_mode(self):
        pass

    #Returns to default mode
    def set_default_mode(self):
        pass

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

    #Opens the deck creating feature
    #Creates a new toplevel window, with options to create a new deck
        # Creating a deck:
        # User will fill in entry for deck name, this will be the deck's filename
        # User then will enter front and back of the cards in the deck,
        # selecting 'save card' to put it in the deck.
        # After the user has put all the cards they want in the deck,
        # the user can hit 'create deck' and the deck will now be
        # available to study
    def create_new_deck(self):
        win = Toplevel()
        win.geometry("500x300")
        win.resizable(False, False)
        win.title("Deck Creator")
        win.iconbitmap("./assets/icon.ico")

        new_cards = []

        header_label = Label(win, text="Deck Creator", font=("Tahoma",16,"bold"))
        header_label.pack()
        deck_name_label = Label(win, text="Enter Deck Name: ")
        deck_name_label.pack()
        deck_name_entry = Entry(win, width=40)
        deck_name_entry.pack()

        front_of_card_label = Label(win, text="Front: ")
        front_of_card_label.pack()
        front_of_card_entry = Entry(win, width=40)
        front_of_card_entry.pack()
        back_of_card_label = Label(win, text="Back: ")
        back_of_card_label.pack()
        back_of_card_entry = Entry(win, width=40)
        back_of_card_entry.pack()

        def save_card():
            new_cards.append(Card(front_of_card_entry.get(), back_of_card_entry.get()))
            front_of_card_entry.delete(0, 'end')
            back_of_card_entry.delete(0, 'end')
            print("New Cards: ")
            for card in new_cards:
                print("CARD: " + card.front + ", " + card.back)

        save_card_button = Button(win, text="Save Card", command=save_card)
        save_card_button.pack()

        def write_deck_information():
            file = open("./sample-decks/" + deck_name_entry.get() + ".txt", "w")
            for card in new_cards:
                if card == new_cards[-1]:
                    file.write(card.front + ",," + card.back)
                else:
                    file.write(card.front + ",," + card.back + "\n")

        create_deck_button = Button(win, text="Create Deck",command=combine_funcs(write_deck_information, win.destroy))
        create_deck_button.pack()

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
        if(self.cards == []):
            print("You must open a deck with cards!")
            self.current_deck_label['text'] = "You must open a deck with cards!"
        else:
            if(self.current_card_index == len(self.cards)-1):
                self.current_card_index = 0
                self.current_card = self.cards[self.current_card_index]
                self.card_label["text"] = self.current_card.front
                self.current_card_string = self.current_card.front
                self.spacing()
            else:
                #print("DEBUG: current card index: " + str(self.current_card_index) + "\nlen(self.cards)-1: " + str(len(self.cards) -1))
                self.current_card_index = self.current_card_index + 1
                self.current_card = self.cards[self.current_card_index]
                self.card_label["text"] = self.current_card.front
                self.current_card_string = self.current_card.front
                self.spacing()

    #Selects the next "random" card in the deck, updates the GUI
    def random_card(self):
        if(self.cards == []):
            print("You must open a deck with cards!")
            self.current_deck_label['text'] = "You must open a deck with cards!"
        else:
            if((self.current_card_index != 0) and (self.remaining_cards == len(self.cards) - 1)):
                # Not previously clicked random card, resets to random cards
                self.current_card = self.cards[0]
                self.current_card_index = 0
                self.card_label["text"] = self.current_card.front
                self.current_card_string = self.current_card.front
                self.spacing()
            elif(len(self.seen_cards) == len(self.cards)):
                # Seen all cards with random
                self.current_card = self.cards[0]
                self.current_card_index = 0
                self.remaining_cards = len(self.cards) - 1
                self.seen_cards = [0]
                self.card_label["text"] = self.current_card.front
                self.current_card_string = self.current_card.front
                self.spacing()
            else:
                # Pick a random card that hasn't been seen
                self.random_index = random.randint(0, len(self.cards)-1)
                while(self.random_index in self.seen_cards):
                    self.random_index = random.randint(0, len(self.cards)-1)
                self.seen_cards.append(self.random_index)
                self.remaining_cards = self.remaining_cards - 1
                self.current_card_index = self.random_index
                self.current_card = self.cards[self.random_index]
                self.card_label["text"] = self.current_card.front
                self.current_card_string = self.current_card.front
                self.spacing()
                #self.print_random_debug()

    def print_random_debug(self):
        print("DEBUG\n=========\n")
        print("SEEN CARDS: ")
        for card in self.seen_cards:
            if card == self.seen_cards[-1]:
                print(str(card))
            else:
                print(str(card) + ", ", end='')
        print("\nREMAINING CARDS: " + str(self.remaining_cards))
        print("\nCURRENT CARD INDEX: " + str(self.current_card_index))
        print("\nRANDOM INDEX: " + str(self.random_index))

    #Changes the Deck
    def change_deck(self):
        #Get deck selection from option page
        print("Deck choice: " + self.deck_choice)
        
        #Set the cards
        opened_deck = open("./sample-decks/" + self.deck_choice, "r")
        self.current_deck_label["text"] = "Current Deck: " + self.deck_choice[:-4]
        lines = opened_deck.readlines()
        if(lines == []):
            print("You must open a deck with cards!")
            self.current_deck_label['text'] = "You must open a deck with cards!"
        else:
            lines = [line.rstrip() for line in lines]
            self.cards = []
            for line in lines:
                x = line.split(",,")
                self.cards.append(Card(x[0],x[1]))

            #Init Deck
            self.current_card = self.cards[0]
            self.current_card_index = 0
            self.current_card_string = self.current_card.front
            self.card_label["text"] = self.current_card.front

            self.deck_size = len(self.cards)
            self.remaining_cards = len(self.cards) - 1
            self.seen_cards = [0]
            self.spacing()

    #Ensures that card spacing fits the label
    def spacing(self):
        if(len(self.card_label["text"]) > 85):
            #Split the label to fit the screen
            #print("Resizing text")
            line = self.card_label["text"]
            self.card_label["text"] = ""
            n = 85
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