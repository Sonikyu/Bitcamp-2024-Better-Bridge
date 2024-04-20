from Deck import Deck
from Player import Player

class Board():
    #Globals
    #ArrayList of previous rounds {(),()}
    #Team Score
    #Bet of the Game
    #Actions should be defined by 

    def __init__(self):
        self.trumpSuit
        self.gamesToWin #Make this always NS

        self.currentTrick = []
        self.pastTricks = []
        self.currentTrickSuit
        self.currentPrio

        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()
        deck = Deck()
        for i in range(13):
            self.player1.addCard(deck.draw())
            self.player2.addCard(deck.draw())
            self.player3.addCard(deck.draw())
            self.player4.addCard(deck.draw())

    #This method clears the old trick and adds it to pastTricks
    def startTrick(self):
        if self.currentTrick.len() != 0:
            self.pastTricks.append(self.currentTrick)
        self.currentTrick = []

    #Meant to be called in driver/main like board.addToTrick(board.player.playCard())
    #Errors if the currentTrick.len() is 4 or more
    
    def addToTrick(self, card):
        self.currentTrick.append(card)

    #Looks at the cards in the trick and see who wins! Then sets prioPlayer to the owner of that card
    #Also updates the score
    #Calls gameOver() if win
    def evaluateTrick(self):

    

    

    

        
    