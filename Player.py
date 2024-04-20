import 

class Player:
    def __init__(self, type: 'human'):
        self.hand = []
    
    def addCard(self, card):
        self.hand.append.card

    def sortHand(self):
        self.hand.sort
    def playCard(self, card):
        try:
            self.hand.reverse(card);
        except ValueError:
            print("illegal move bro")


    