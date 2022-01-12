import requests
from bs4 import BeautifulSoup
from card import Card

class Scraper:
    def __init__(self, cards):
        self.cards = []

    def ql_to_cards(self, url):
        #url = 'https://quizlet.com/657778880/fruit-or-vegetable-flash-cards/?new'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

        for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
            self.cards.append(Card(question.get_text(),answer.get_text()))

        #Printing the cards to console
        for card in self.cards:
            card.toString()

    def write_cards_to_file(self, file_name):
        #Takes list of Card and puts it into a text file (under file name)
        #front,back\nfront,back etc...
        file = open("./sample-decks/" + file_name + ".txt","w")
        for card in self.cards:
            if card == self.cards[-1]:
                file.write(card.front + "," + card.back)
            else:
                file.write(card.front + "," + card.back + "\n")

#Example of using Scraper to get card from website
#ob = Scraper([])
#ob.ql_to_cards('https://quizlet.com/657778880/fruit-or-vegetable-flash-cards/?new')
#ob.write_cards_to_file("quizlet")