from Deck import Deck
from Bet import BetFactory
import random
import Render
class Player:
    def __init__(self, id: int):
        self.hand = []
        self.id = id
        self.wins = 0
    #Will replace for user or abstract method
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
    
    #Chooses the best move out of the legal moves available
    def chooseCard(self, board):
        legalCards = []
        for i in self.hand:
            if self.isValidCardMove(i, board) == True:
                legalCards.append(i)
      
        chosenCard = random.choice(legalCards)
        
        return chosenCard

    #Checks if the players card is legal for the current trick suit
    def isValidCardMove(self, card, Board):
        isPlayerFirst = Board.currentTrickSuit == None
        #Checks if Player choose the right suit and the Current Trick Suit isn't None
        playerChoseRightSuit = Board.currentTrickSuit != None and Board.currentTrickSuit == card.suit
        #Checks if player has Current Trick Suit
        playerHasSuit = False
        for i in self.hand:
            if i.suit == Board.currentTrickSuit:
                playerHasSuit = True
        if isPlayerFirst or playerChoseRightSuit or not playerHasSuit :
            return True
        else:
            return False

    
    def addCard(self, card):
        self.hand.append(card)

    def printHand(self):
        result = ""
        for card in self.hand:
            result += card.__str__() + " | "
        print(f"[{result}]")

    #Sorts hand based on id (suit * 13 + suit )
    def sortHand(self):
        self.hand.sort(key = lambda x: x.id)
        
    #If the player chose the right suit or doesn't have the right suit, the function returns True
    #Otherwise, the function returns False;
    def playCard(self, card, Board):
        check = self.isValidCardMove(card, Board)
        if check:
            try:
                self.hand.remove(card)
                self.update_card_positions()
                return True
            except ValueError:
                print("illegal move bro")
        else:
            print("Input Different Value")
            return False
    def inc_wins(self):
        self.wins += 1
    def update_card_positions(self):
        loc_offset = 0
        for card in self.hand:
            card.x = ((Render.SCREEN_WIDTH - ((len(self.hand) + 1) * (Render.CARD_WIDTH * 2 / 3))) / 2) + loc_offset*Render.CARD_WIDTH * 2/3
            loc_offset += 1

    def __str__(self) -> str:
        return f"PLAYER {str(1+self.id)}"
    def __lt__ (self, otherPlayer):
        return self.wins - otherPlayer.wins
    