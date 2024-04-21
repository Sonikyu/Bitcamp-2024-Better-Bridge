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
        self.gamesToWin = 7 #Make this always NS

        self.bettingOrder = []
        self.currentBetID = -1 
        self.getState = "BETTING" #This is either 'betting' or 'playing'

        self.teamOneScore = 0
        self.teamTwoScore = 0

        self.activePlayer = 0
        self.prioPlayer = None
        self.currentTrick = [None, None, None, None]
        self.pastTricks = []
        self.evalTrumpSuit = []
        self.evalCurSuit = []
        self.currentTrickSuit = None
        self.currentPrioSuit = None
        self.player1 = Player(0)
        self.player2 = Player(1)
        self.player3 = Player(2)
        self.player4 = Player(3)
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
            self.inc_player()
            return True
        print("Illegal Bet")
        return False

    def startBetting(self):
        while self.checkBetting() == False:
            for player in self.players:
                self.addBet(player.chooseBet(self))
                if self.checkBetting() == True:
                    self.prioPlayer = player
                    self.trumpSuit = self.bettingOrder[3].suit
                    self.getState = "PLAYING"
                    if player.id == 0 or player.id == 2:
                        self.gamesToWin = self.bettingOrder[3].level
                    elif player.id == 1 or player.id == 3:
                        self.gamesToWin = 14-self.bettingOrder[3].level
                    break
        for bet in self.bettingOrder:
            print(bet)
        print("done betting")


    def startGame(self):
        print("Started Game")
        for i in range(13):
            self.startTrick()
            for j in range(4):
                index = (j + self.prioPlayer.id) % 4
                tempCard = self.players[index].chooseCard(self)
                print("Card", index, tempCard)
                self.players[index].playCard(tempCard, self)
                self.addToTrick(tempCard)
            self.evaluateTrick()
            #print("prio:", self.prioPlayer.id)

        self.getState = "GAME_OVER"
        print("Ended Game")


    #This method clears the old trick and adds it to pastTricks
    def startTrick(self):
        
        #save old trick
        if len(self.currentTrick) != 0:
            self.pastTricks.append(self.currentTrick)
        # reset variables for new trick
        self.currentTrick = []
        self.evalTrumpSuit = []
        self.evalCurSuit = []
        self.currentTrickSuit = None

    #Meant to be called in driver/main like board.addToTrick(board.player.playCard())
    #Errors if the currentTrick.len() is 4 or more
    #Sets currentTrickSuit to the first card in the CurrentTrickSuit
    def addToTrick(self, card):
        #set current trick suit if card is the first played
        if (self.currentTrickSuit == None):
            self.currentTrickSuit = card.suit

        self.currentTrick.append(card)

        #add cards to corresponding lists for evaluating winner 
        if (card.suit == self.currentPrioSuit):
            self.evalTrumpSuit.append(card)
        if (card.suit == self.currentTrickSuit):
            self.evalCurSuit.append(card)

    #Game over function prints winner 
    def gameOver(self, winner):
        self.gameWon = True
        print("Team", winner, "wins!")

    #Looks at the cards in the trick and see who wins! Then sets prioPlayer to the owner of that card
    #Also updates the score
    #Calls isGameOver() if win
    def evaluateTrick(self):
        winner = None
        if self.currentPrioSuit != BetSuit.LOW:
            if (len(self.evalTrumpSuit) != 0):
                self.evalTrumpSuit.sort(reverse=True, key= lambda x: x.rank.value)
                winner = self.evalTrumpSuit[0]
                
            else:
                self.evalCurSuit.sort(reverse=True, key= lambda x: x.rank.value)
                winner = self.evalCurSuit[0]
        else:
            self.evalCurSuit.sort(key= lambda x: x.rank.value)
            winner = self.evalCurSuit[0]

        self.prioPlayer = winner.owner

        if (self.prioPlayer.id == 0 or self.prioPlayer.id == 2):
            self.teamOneScore += 1
            if (self.teamOneScore >= self.gamesToWin):
                self.gameOver(1)
        elif (self.prioPlayer.id == 1 or self.prioPlayer.id == 3):
            self.teamTwoScore += 1
            if (self.teamTwoScore >= 14-self.gamesToWin):
                self.gameOver(2)

        print("1:", self.teamOneScore, " 2:", self.teamTwoScore, "\n")
        
    def inc_player(self):
        self.activePlayer += 1
        if self.activePlayer > 3:
            self.activePlayer = 0
