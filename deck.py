import random
from Card import Card
from Rank import Rank
from Suit import Suit
import numpy as np
class Deck:
    #Deck initializes list of cards and shuffles it
    def __init__ (self):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                #Ensures that the suit created doesn't involve the High or Low values that will be used for betting
                if suit != Suit.LOW | suit != Suit.HIGH:
                    self.cards.append(Card(rank, suit))
        self.shuffle(self)
    #Shuffles Deck
    def shuffle(self):
        cards = np.array(self.cards)
        cards.shuffle(cards)
    #Removes and returns the first card out of the deck 
    def draw(self):
        card = self.cards.pop()
        return card
