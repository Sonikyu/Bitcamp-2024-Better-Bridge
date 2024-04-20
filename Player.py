from Deck import Deck
from Board import Board
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
        #Checks if Player is first (i.e. the first card is None)
        isPlayerFirst = Board.currentPrio == None
        #Checks if Player choose the right suit and the Prio isn't None
        playerChoosesRightSuit = Board.currentPrio != None and Board.currentPrio == card.suit
        #Checks if player has hand
        playerHasPrio = False
        for i in self.hand:
            if self.hand[i].suit == Board.currentPrio:
                playerHasPrio = True
        needsChecking = True
        while needsChecking:
            if isPlayerFirst or playerChoosesRightSuit or not playerHasPrio :
                try:
                    self.hand.remove(card)
                    self.update_card_positions()
                    needsChecking = False
                except ValueError:
                    print("illegal move bro")
            else:
                print("Input Different Value")
    
    
    def update_card_positions(self):
        loc_offset = 0
        for card in self.hand:
            card.x = ((Render.SCREEN_WIDTH - ((len(self.hand) + 1) * (Render.CARD_WIDTH * 2 / 3))) / 2) + loc_offset*Render.CARD_WIDTH * 2/3
            loc_offset += 1


    