
class Card:
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.id = suit.value * 13 + rank.value - 2

    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def toString(self):
        return self.rank + " of " + self.suit
