
class Card:
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def toString(self):
        return self.rank + " of " + self.suit
    