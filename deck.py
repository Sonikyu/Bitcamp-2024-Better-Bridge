import random
<<<<<<< Updated upstream
import Card
import Rank
import Suit
import numpy as np # type: ignore
=======
from Card import Card
from Rank import Rank
from Suit import Suit
import numpy as np
>>>>>>> Stashed changes
class Deck:
    #Deck initializes list of cards and shuffles it
    def __init__ (self):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(rank, suit))
<<<<<<< Updated upstream
        self.shuffle(self)
    #Shuffles Deck
    def shuffle(self):
        cards = np.array(self.cards)
        cards.shuffle(cards)
    #Removes and returns the first card out of the deck 
=======
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)

>>>>>>> Stashed changes
    def draw(self):
        card = self.cards.pop()
        return card
