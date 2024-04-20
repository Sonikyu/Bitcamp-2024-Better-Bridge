from Deck import Deck
from Player import Player
from BetSuit import BetSuit
import copy

class Board():
    #Globals
    #ArrayList of previous rounds {(),()}
    #Team Score
    #Bet of the Game
    #Actions should be defined by 

    def __init__(self):
        self.trumpSuit = None
        self.gamesToWin = 7#Make this always NS

        self.bettingOrder = []
        self.getState = 'BETTING' #This is either 'betting' or 'playing'

        self.teamOneScore = 0
        self.teamTwoScore = 0

        self.prioPlayer = None
        self.currentTrick = [None, None, None, None]
        self.pastTricks = []
        self.currentTrickSuit = None
        self.currentPrio = None
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()
        deck = Deck()
        for i in range(13):
            card = deck.draw()
            card.setOwner(self.player1)
            self.player1.addCard(card)
            card = deck.draw()
            card.setOwner(self.player2)
            self.player2.addCard(card)
            card = deck.draw()
            card.setOwner(self.player3)
            self.player3.addCard(card)
            card = deck.draw()
            card.setOwner(self.player4)
            self.player4.addCard(card)
    
    # def checkBetting(self):
    #     if self.bettingOrder.len < 4: 
    #         return False
    

    # def startBetting(self):
    #     while 



    #This method clears the old trick and adds it to pastTricks
    def startTrick(self):
        if self.currentTrick.len() != 0:
            self.pastTricks.append(self.currentTrick)
        self.currentTrick = []

    #Meant to be called in driver/main like board.addToTrick(board.player.playCard())
    #Errors if the currentTrick.len() is 4 or more
    #Sets currentTrickSuit to the first card in the CurrentTrickSuit
    def addToTrick(self, card):
        self.currentTrick.append(card)
        counter = 0
        
        for i in self.currentTrickSuit:
            if i != None:
                counter += 1
                index = i
        if counter == 1:
             self.currentTrickSuit = self.currentTrick[index]

    #Game over function prints winner 
    def gameOver(self, winner):
        print("Team " + winner + " wins!")

    #Looks at the cards in the trick and see who wins! Then sets prioPlayer to the owner of that card
    #Also updates the score
    #Calls isGameOver() if win
    def evaluateTrick(self):
        if self.currentPrio != BetSuit.LOW:
            highestTrump = -1
            winningTrump = None
            highestCurrent = -1
            winningCurrent = None
            prioPlayer = None
            for i in self.currentTrick:
                if self.currentTrick[i].suit == self.currentPrio:
                    if self.currentTrick[i].rank.value > highestTrump:
                        highestTrump = self.currentTrick[i].rank.value
                        winningTrump = self.currentTrick[i]
                elif self.currentTrick[i].suit == self.currentTrickSuit:
                    if self.currentTrick[i].rank.value > highestCurrent:
                        highestCurrent = self.currentTrick[i].rank.value
                        winningCurrent = self.currentTrick[i]
            if winningTrump == None | self.currentPrio == BetSuit.HIGH:
                prioPlayer = winningCurrent.owner
            else:
                prioPlayer = winningTrump.owner
        else:
            lowestCurrent = 15
            winningCurrent = None
            for i in self.currentTrick:
                if self.currentTrick[i].suit == self.currentTrickSuit:
                    if self.currentTrick[i].rank.value < lowestCurrent:
                        lowestCurrent = self.currentTrick[i].rank.value
                        winningCurrent = self.currentTrick[i]
            prioPlayer = winningCurrent.owner      


        if (prioPlayer.id == 0 | prioPlayer.id == 2):
            self.teamOneScore += 1
            if (self.teamOneScore >= self.gamesToWin):
                self.gameOver(1)
        elif (prioPlayer.id == 1 | prioPlayer.id == 3):
            self.teamTwoScore += 1
            if (self.teamTwoScore >= self.gamesToWin):
                self.gameOver(2)

