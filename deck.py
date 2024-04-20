import random
import Card
import Rank
import Suit
import numpy as np
class Deck:
    def __init__ (self):
        self.cards = []
        for rank in Rank():
            for suit in Suit():
                self.cards.append(Card(rank, suit))
        
def shuffle(self):
    cards = np.array(self.cards)
    cards.shuffle(cards)

def draw(self):
    self.card = self.cards[0]
    self.cards.remove(0)
    return self.card

