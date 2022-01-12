# SpaceCards - main.py
# Author: Anthony Narlock

import os
from card import Card

def main():
    #Prints welcome message
    print("SpaceCards indev 0.1\nBy: Anthony Narlock\n==============")

    #Scans decks folder for all decks
    decks = os.listdir('./sample-decks') #Gets Decks from deck folder
    print(decks)

    #Inputs user to ask which deck they wish to study
    deck_choice = int(input("Select Deck you wish to study by typing index: "))
    opened_deck = open("./sample-decks/" + decks[deck_choice], "r")
    name_of_deck = os.path.basename(opened_deck.name)

    print("==============")
    print("You opened " + name_of_deck)

    #Each line in the deck separated
    lines = opened_deck.readlines()
    lines = [line.rstrip() for line in lines]

    cards = []

    for line in lines:
        x = line.split(",")
        cards.append(Card(x[0],x[1]))

    card_quiz(cards)

def card_quiz(cards):
    #User will be quizzed on each card in the deck

    for card in cards:
        print(card.front)
        input("Press enter to show back of card")
        print(card.back)
        if(card == cards[-1]):
            print("Deck completed")
            complete(cards)
        else:
            input("Press enter to continue to next card")

def complete(cards):
    choice = input("Would you like to study this deck again? Enter y/n : ")
    if choice == "y":
        card_quiz(cards)
    else:
        choice = input("Study a different deck? Enter y/n : ")
        if choice == "y":
            main()
        else:
            print("Thanks for using SpaceCards")


if __name__ == '__main__':
    main()