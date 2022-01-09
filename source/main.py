# SpaceCards - main.py
# Author: Anthony Narlock

import os

def main():
    print("SpaceCards indev 0.1\nBy: Anthony Narlock\n====")

    decks = os.listdir('./sample-decks') #Gets Decks from deck folder
    print(decks)

    deck_choice = int(input("Select Deck you wish to study by typing index: "))
    opened_deck = open("./sample-decks/" + decks[deck_choice], "r")

    print("====")
    print(opened_deck.read())

if __name__ == '__main__':
    main()