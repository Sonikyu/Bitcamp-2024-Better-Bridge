import random
import Card
import Rank
import Suit
import numpy as np # type: ignore
class Deck:
    #Deck initializes list of cards and shuffles it
    def __init__ (self):
        self.cards = []
        for rank in Rank():
            for suit in Suit():
                self.cards.append(Card(rank, suit))
        self.shuffle(self)
    #Shuffles Deck
    def shuffle(self):
        cards = np.array(self.cards)
        cards.shuffle(cards)
    #Removes and returns the first card out of the deck 
    def draw(self):
        self.card = self.cards[0]
        self.cards.remove(0)
        return self.card

