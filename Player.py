from Deck import Deck

class Player:
    def __init__(self, id):
        self.hand = []
        self.id = id

    def __init__(self):
        self.hand = []
        self.id = 0
    
    def addCard(self, card):
        self.hand.append(card)

    def printHand(self):
        result = ""
        for card in self.hand:
            result += card.__str__() + " | "
        print("[" + result + "]")

    def sortHand(self):
        self.hand.sort
    def playCard(self, card):
        try:
            self.hand.remove(card)
        except ValueError:
            print("illegal move bro")


    