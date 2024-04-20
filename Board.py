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
        self.trumpSuit = None #Includes HIGH and LOW
        self.gamesToWin = 7#Make this always NS

        self.bettingOrder = []
        self.currentBetID = -1 
        self.getState = "BETTING" #This is either 'betting' or 'playing'

        self.teamOneScore = 0
        self.teamTwoScore = 0

        self.currentTrick = [None, None, None, None]
        self.pastTricks = []
        self.currentTrickSuit = None
        self.currentPrio = None
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()
        self.players = [self.player1, self.player2, self.player3, self.player4]
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
    
    def checkBetting(self):
        if len(self.bettingOrder) < 4: 
            return False
        #ID for pass is 42
        elif self.bettingOrder[0].getID() == 42 and self.bettingOrder[1].getID() == 42 and self.bettingOrder[2].getID() == 42 and self.bettingOrder[3].getID() != 42:
            return True
        return False
    
    def addBet(self, bet):
        if bet.getID() > self.currentBetID:
            self.bettingOrder.insert(0, bet)
            if(bet.getID() != 42):
                self.currentBetID = bet.getID()
            return
        print("Illegal Bet")

    def startBetting(self):
        while self.checkBetting() == False:
            for player in self.players:
                self.addBet(player.chooseBet(self))
                if self.checkBetting() == True:
                    self.currentPrio = player
                    self.trumpSuit = self.bettingOrder[3].suit
                    self.getState = "PLAYING"
                    break
        for bet in self.bettingOrder:
            print(bet)
        print("done betting")
        



    

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
            if self.currentTrick[i] != None:
                counter += 1
                index = i
        if counter == 1:
             self.currentTrickSuit = self.currentTrick[index]

    #Looks at the cards in the trick and see who wins! Then returns the prioPlayer
    def evaluateTrick(self):
        if self.currentPrio != BetSuit.LOW:
            highestTrump = -1
            winningTrump = None
            highestCurrent = -1
            winningCurrent = None
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
                return winningCurrent.owner
            else:
                return winningTrump.owner
        else:
            lowestCurrent = 15
            winningCurrent = None
            for i in self.currentTrick:
                if self.currentTrick[i].suit == self.currentTrickSuit:
                    if self.currentTrick[i].rank.value < lowestCurrent:
                        lowestCurrent = self.currentTrick[i].rank.value
                        winningCurrent = self.currentTrick[i]
            return winningCurrent.owner        
