from Deck import Deck
import Render
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
            self.update_card_positions()
        except ValueError:
            print("illegal move bro")
    
    
    def update_card_positions(self):
        loc_offset = 0
        for card in self.hand:
            card.x = ((Render.SCREEN_WIDTH - ((len(self.hand) + 1) * (Render.CARD_WIDTH * 2 / 3))) / 2) + loc_offset*Render.CARD_WIDTH * 2/3
            loc_offset += 1


    