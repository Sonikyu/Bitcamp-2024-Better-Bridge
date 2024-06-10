import random
from Assets.Card_Related.Card import Card
from Rank import Rank
from Assets.Card_Related.Suit import Suit

class Deck:
    #Deck initializes list of cards and shuffles it
    def __init__ (self):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(rank, suit))
        self.shuffle()
    #Shuffles Deck
    def shuffle(self):
        random.shuffle(self.cards)
    #Removes and returns the first card out of the deck 
    def draw(self):
        card = self.cards.pop()
        return card
