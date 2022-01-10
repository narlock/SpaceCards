import os
from card import Card
from tkinter import *
from PIL import Image, ImageTk

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


    def test(self):
        self.text_label["text"] = "This\nIs a test"

    def __init__(self):
        
        #Create Window
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("SpaceCards - indev 0.1")
        self.root.resizable(False, False)

        self.cards = []

        #Image row
        frame0 = Frame(self.root)
        logo = PhotoImage(file="./assets/logo.png")
        self.label = Label(frame0, image=logo)
        self.label.pack()
        self.title_label = Label(frame0, text="By: Anthony Narlock", font="Tahoma").pack()
        frame0.pack()

        frame_line1 = Frame(self.root)
        line = Label(frame_line1, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n").pack()
        frame_line1.pack()

        #Instruction row
        frame1 = Frame(self.root)
        self.instructions = Label(frame1, text="Select a deck to study",font="Tahoma").pack()
        self.decks = os.listdir('./sample-decks')
        self.variable = StringVar(self.root)
        self.variable.set(self.decks[0])
        self.deck_menu = OptionMenu(frame1, self.variable, *self.decks)
        self.deck_menu.pack()
        self.change_deck_btn = Button(frame1, text="Change Deck", command=self.change_deck)
        self.change_deck_btn.pack()
        frame1.pack()

        #Get Cards
        self.deck_choice = self.variable.get()

        frame_line2 = Frame(self.root)
        line = Label(frame_line2, text="\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n").pack()
        frame_line2.pack()

        #Flip Card
        frame2 = Frame(self.root)
        self.deck_name_label = Label(frame2, text="Current Deck: ", font="Tahoma")
        self.deck_name_label.pack()
        self.text_label = Label(frame2, text="Front", font=("Tahoma",12,'bold'))
        self.text_label.pack()
        self.btn = Button(frame2, text="Flip",command=self.flip)
        self.btn.pack()
        self.next_btn = Button(frame2, text="Next Card", command=self.next)
        self.next_btn.pack()
        #self.test_btn = Button(frame2, text="Test", command=self.spacing)
        #self.test_btn.pack()
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