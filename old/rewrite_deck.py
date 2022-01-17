new_deck = []

deck = open("./sample-decks/software_dev_ch1.txt", "r")
lines = deck.readlines()
lines = [line.rstrip() for line in lines]
for line in lines:
    x = line.replace(",",",,")
    new_deck.append(x)

deck = open("./sample-decks/software_dev_ch1.txt", "w")
for card in new_deck:
    if card == new_deck[-1]:
        deck.write(card)
    else:
        deck.write(card + "\n")