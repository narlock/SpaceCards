import requests
from bs4 import BeautifulSoup
from card import Card

url = 'https://quizlet.com/657778880/fruit-or-vegetable-flash-cards/?new'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

cards = []

for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
    cards.append(Card(question.get_text(),answer.get_text()))

for card in cards:
    card.toString()

#TODO
#Now that I have a list of cards, let's begin next time by converting it to a text file