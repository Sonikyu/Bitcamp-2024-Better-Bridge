
class Card:
    #Cards have a rank, suit, and id
    #id is used for comparing
    def __init__ (self, rank, suit, owner):
        self.rank = rank
        self.suit = suit
        self.id = suit.value * 13 + rank.value - 2
        self.owner = None

    #Checks if the other card is bigger than or less than the current card
    def __lt__ (self, otherCard):
        return self.id - otherCard.id
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def getOwner(self):
        return self.owner
    
    def setOwner(self, owner):
        self.owner = owner

    def __str__(self):
        return self.rank.name +  self.suit.name
    
