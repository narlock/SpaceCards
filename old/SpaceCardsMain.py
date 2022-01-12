import os
from card import Card
from Scraper import Scraper
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
#from django.core.validators import URLValidator
#from django.core.exceptions import ValidationError

class SpaceCards():

    def print_cards(self):
        for card in self.cards:
            print(card.front + " " + card.back + "\n")
        self.cards[self.current_card_index].toString()

    def change_deck(self):
        self.deck_choice = self.variable.get()
        self.make_cards()
        self.current_card = self.cards[0]
        self.current_card_index = 0
        self.init_deck()
        self.spacing()

    def make_cards(self):
        opened_deck = open("./sample-decks/" + self.deck_choice, "r")
        self.deck_name_label["text"] = "Current Deck: " + self.deck_choice
        lines = opened_deck.readlines()
        lines = [line.rstrip() for line in lines]
        self.cards = []
        for line in lines:
            x = line.split(",")
            self.cards.append(Card(x[0],x[1]))

    def init_deck(self):
        self.text_label["text"] = self.current_card.front
        self.spacing()

    def flip(self):
        if(self.text_label["text"] == self.current_card.back):
            self.text_label["text"] = self.current_card.front
            self.spacing()
        else:
            self.text_label["text"] = self.current_card.back
            self.spacing()

    def next(self):
        if(self.current_card_index == len(self.cards)-1):
            self.current_card_index = 0
            self.current_card = self.cards[self.current_card_index]
            self.current_card.toString()
            self.text_label["text"] = self.current_card.front
            self.spacing()
        else:
            print("current card index: " + str(self.current_card_index) + "\nlen(self.cards)-1: " + str(len(self.cards) -1))
            self.current_card_index = self.current_card_index + 1
            self.current_card = self.cards[self.current_card_index]
            #self.current_card.toString()
            self.text_label["text"] = self.current_card.front
            self.spacing()

    def spacing(self):
        if(len(self.text_label["text"]) > 80):
            #Split the label to fit the screen
            print("Resizing text")
            line = self.text_label["text"]
            self.text_label["text"] = ""
            n = 80
            lines = [line[i:i+n] for i in range(0, len(line), n)]
            for line in lines:
                self.text_label["text"] += line + "\n"

    def import_deck_from_quizlet(self):
        #TODO check if url is valid
        valid = True
        if(valid and len(self.import_deck_name.get()) != 0):
            scraper = Scraper([])
            scraper.ql_to_cards(self.import_entry.get())
            scraper.write_cards_to_file(self.import_deck_name.get())
            print("Import Successful")
            #TODO
            #newGUI = SpaceCards()
            #self.root.destroy()
        else:
            print("Import unsuccessful")

    def refresh_deck_list(self):
        self.decks = os.listdir('./sample-decks')
        self.variable = StringVar(self.root)
        self.variable.set(self.decks[0])
        self.deck_menu = OptionMenu(self.frame1, self.variable, *self.decks)

    def test(self):
        self.text_label["text"] = "This\nIs a test"

    def __init__(self):
        
        #Create Window
        #self.root = Tk()
        self.root = Toplevel()
        self.root.geometry("800x650")
        self.root.title("SpaceCards - indev 0.1")
        #self.root.resizable(False, False)
        self.root['background'] = 'light grey'

        self.cards = []

        #Image row
        frame0 = Frame(self.root)
        logo = PhotoImage(file="./assets/logo.png")
        self.label = Label(frame0, image=logo)
        self.label['background'] = 'light grey'
        self.label.pack()
        self.title_label = Label(frame0, text="By: Anthony Narlock", font=("Tahoma",12,'bold'))
        self.title_label['background'] = 'light grey'
        self.title_label['foreground'] = 'black'
        self.title_label.pack()
        frame0['background'] = 'light grey'
        frame0.pack()

        frame_line1 = Frame(self.root)
        line = Label(frame_line1, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        line['background'] = 'light grey'
        line.pack()
        frame_line1.pack()

        #Instruction row
        self.frame1 = Frame(self.root)
        self.instructions = Label(self.frame1, text="Select a deck to study",font="Tahoma")
        self.instructions['background'] = 'light grey'
        self.instructions['foreground'] = 'black'
        self.instructions.pack()
        self.decks = os.listdir('./sample-decks')
        self.variable = StringVar(self.root)
        self.variable.set(self.decks[0])
        self.deck_menu = OptionMenu(self.frame1, self.variable, *self.decks)
        self.deck_menu['background'] = 'light blue'
        self.deck_menu.pack()
        self.change_deck_btn = Button(self.frame1, text="Change Deck", command=self.change_deck)
        self.change_deck_btn['background'] = 'light blue'
        self.change_deck_btn.pack()
        self.import_quizlet_deck_btn = Button(self.frame1, text="Import Deck", command=self.import_deck_from_quizlet)
        self.import_quizlet_deck_btn['background'] = 'light blue'
        self.import_quizlet_deck_btn.pack()
        self.import_entry = Entry(self.frame1, text="paste link here", width=40)
        self.import_entry.pack()
        self.import_deck_name = Entry(self.frame1, text="enter deck name", width=40)
        self.import_deck_name.pack()
        self.frame1['background'] = 'light grey'
        self.frame1.pack()

        #Get Cards
        self.deck_choice = self.variable.get()

        frame_line2 = Frame(self.root)
        line = Label(frame_line2, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        line['background'] = 'light grey'
        line.pack()
        frame_line2.pack()

        #Flip Card
        frame2 = Frame(self.root)
        self.deck_name_label = Label(frame2, text="Current Deck: ", font="Tahoma")
        self.deck_name_label['background'] = 'light grey'
        self.deck_name_label['foreground'] = 'red'
        self.deck_name_label.pack()
        self.text_label = Label(frame2, text="Front", height=2, width=70, padx=20, pady=20, borderwidth=2, relief="solid", font=("Tahoma",12,'bold'))
        self.text_label.pack()
        self.btn = Button(frame2, text="Flip", height=1, width=10, command=self.flip)
        self.btn['background'] = 'light blue'
        self.btn.pack()
        self.next_btn = Button(frame2, text="Next Card", height=1, width=10, command=self.next)
        self.next_btn['background'] = 'light blue'
        self.next_btn.pack()
        #self.test_btn = Button(frame2, text="Test", command=self.spacing)
        #self.test_btn.pack()
        frame2['background'] = 'light grey'
        frame2.pack()

        self.make_cards()
        self.current_card = self.cards[0]
        self.current_card_index = 0
        self.init_deck()
        self.spacing()

        #self.print_cards()

        self.root.mainloop()


def main():
    my_gui = SpaceCards()

if __name__ == "__main__":
    main()