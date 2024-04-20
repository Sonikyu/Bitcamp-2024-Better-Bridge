from Deck import Deck
from Player import Player
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

        self.getState = 'BETTING' #This is either 'betting' or 'playing'

        self.currentTrick = []
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

    #Looks at the cards in the trick and see who wins! Then sets prioPlayer to the owner of that card
    #Also updates the score
    #Calls gameOver() if win
    def evaluateTrick(self):
        copyTrick = copy.deepCopy(self.currentTrick)
        if self.currentPrio == HIGH:
           copyTrick.sort
           #Continue Coding
        elif self.currentPrio == LOW:
            copyTrick.sort(True)
            #Continue Coding
        else:
            #I'm not sure if this works
            prioCount = copyTrick.count(self.currentPrio)
            if prioCount > 0:
                #Find Values with Prio and puts it into a list. Then list is sorted
                prioIndexList = []
                for i in copyTrick:
                    if i.suit == self.currentPrio:
                        prioIndexList.append
                
            else:
                 #Find Values with currentSuit and puts it into a list. Then list is sorted




