from Deck import Deck
from Bet import BetFactory
import random
import Render
class Player:
    def __init__(self, id):
        self.hand = []
        self.id = id

    def __init__(self):
        self.hand = []
        self.id = 0

    def chooseBet(self, Board):
        currentBetID = Board.currentBetID
        legalMoves = []
        betFactory = BetFactory()
        for bet in betFactory.Bets:
            if bet.getID() > currentBetID:
                legalMoves.append(bet)
        if len(legalMoves) == 0:
            return betFactory.getBet(42)
        if currentBetID == -1:
            return random.choice(legalMoves)
        elif random.randint(0,100) < 70:
            return betFactory.getBet(42)
        else:
            return random.choice(legalMoves)



    
    def addCard(self, card):
        self.hand.append(card)

    def printHand(self):
        result = ""
        for card in self.hand:
            result += card.__str__() + " | "
        print("[" + result + "]")

    def sortHand(self):
        self.hand.sort
        
    #If the player chose the right suit or doesn't have the right suit, the function returns True
    #Otherwise, the function returns False;
    def playCard(self, card, Board):
        #Checks if Player is first (i.e. the first card is None)
        isPlayerFirst = Board.currentTrickSuit == None
        #Checks if Player choose the right suit and the Current Trick Suit isn't None
        playerChoseRightSuit = Board.currentTrickSuit != None and Board.currentTrickSuit == card.suit
        #Checks if player has Current Trick Suit
        playerHasSuit = False
        for i in self.hand:
            if self.hand[i].suit == Board.currentTrickSuit:
                playerHasSuit = True
        
        if isPlayerFirst or playerChoseRightSuit or not playerHasSuit :
            try:
                self.hand.remove(card)
                self.update_card_positions()
                needsChecking = False
                return True
            except ValueError:
                print("illegal move bro")
        else:
            print("Input Different Value")
            return False
    
    
    def update_card_positions(self):
        loc_offset = 0
        for card in self.hand:
            card.x = ((Render.SCREEN_WIDTH - ((len(self.hand) + 1) * (Render.CARD_WIDTH * 2 / 3))) / 2) + loc_offset*Render.CARD_WIDTH * 2/3
            loc_offset += 1


    