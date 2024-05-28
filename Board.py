from Deck import Deck
from Player import Player
from BetSuit import BetSuit
from os import path
import copy
import pygame
import Render
import time

class Board():
    #Globals
    #ArrayList of previous rounds {(),()}
    #Team Score
    #Bet of the Game
    #Actions should be defined by 

    def __init__(self) -> None:
        #self.getState = "BETTING" #This is either 'betting' or 'playing'
        self.getState = "MENU"
        self.gameMode: str = None

    def check_profile_name(self) -> str:
        profile_name_file = 'profile_name.txt'
        name = ''
        try:
            with open(profile_name_file) as file:
                name = file.read()
        except FileNotFoundError:
            with open(profile_name_file, 'w') as file:
                name = Render.draw_get_name()
                file.write(name)
        self.name = name



    
    def set_up_players(self) -> None:
        #ADD MULTIPLAYER LATER
        if self.gameMode == "SINGLE":
            self.player1 = Player(0, self.name)
            self.player2 = Player(1, "BOT")
            self.player3 = Player(2, "TEAM BOT")
            self.player4 = Player(3, "BOT")
        self.players = [self.player1, self.player2, self.player3, self.player4]
        self.getState = "BETTING"

    def cards_to_players(self) -> None:
        deck = Deck()
        for i in range(13):
            for player in self.players:
                card = deck.draw()
                card.setOwner(player)
                player.addCard(card)
    def reset_values(self) -> None:
        self.trumpSuit = None #Includes HIGH and LOW
        self.gamesToWin = 7 #Make this always NS

        self.bettingOrder = []
        self.currentBetID = -1 
        self.teamOneScore = 0
        self.teamTwoScore = 0
        self.winningTeam = 0

        self.yourTurn = False

        self.activePlayer = 0
        self.prioPlayer = None
        self.currentTrick = [None, None, None, None]
        self.pastTricks = []
        self.evalTrumpSuit = []
        self.evalCurSuit = []
        self.currentTrickSuit = None
        self.set_up_players()
        print("SET UP PLAYERS CALLED")
        self.cards_to_players()
        print("CARDS TO PLAYERS CALLED")

    def checkBetting(self) -> bool:
        if len(self.bettingOrder) < 4: 
            return False
        #ID for pass is 42
        elif self.bettingOrder[0].getID() == 42 and self.bettingOrder[1].getID() == 42 and self.bettingOrder[2].getID() == 42 and self.bettingOrder[3].getID() != 42:
            return True
        return False
    
    def addBet(self, bet) -> bool:
        if bet.getID() > self.currentBetID:
            self.bettingOrder.insert(0, bet)
            if(bet.getID() != 42):
                self.currentBetID = bet.getID()
            self.inc_player()
            return True
        print("Illegal Bet")
        return False

    def startBetting(self):
        print("START BETTING CALLED")
        self.player1.sortHand()
        self.player1.update_card_positions()
        while self.checkBetting() == False:
            for player in self.players:
                self.addBet(player.chooseBet(self))
                if self.checkBetting() == True: # == True is unnecessary
                    index = (player.id + 1) % 4
                    self.prioPlayer = self.players[index]
                    self.trumpSuit = self.bettingOrder[3].suit
                    if (player.id+1) % 2 == 0:
                        self.gamesToWin = self.bettingOrder[3].level
                    elif (player.id+1) % 2 == 1:
                        self.gamesToWin = 14-self.bettingOrder[3].level
                    break
        counter = 0
        self.bettingOrder.reverse()
        lastBet = None
        for bet in self.bettingOrder:
            print(counter % 4, bet)
            counter += 1
            if (bet.getID() != 42):
                lastBet = bet
        print("done betting, final bet:", lastBet)
        self.getState = "PLAYING"

    """""
    def startGame(self):
        print("Started Game")
        for i in range(13):
            self.startTrick()
            for j in range(4):
                index = (j + self.prioPlayer.id) % 4
                tempCard = self.players[index].chooseCard(self)
                print("Card", index, tempCard)
                self.players[index].playCard(tempCard, self)
                self.addToTrick(tempCard, self.players[index])
            self.evaluateTrick()
            #print("prio:", self.prioPlayer.id)

        self.getState = "GAME_OVER"
        print("Ended Game")
    """""
    def startPlayerGame(self):
        self.player1.sortHand()
        self.player1.update_card_positions()
        print("Started Player Game")
        for i in range(13):
            self.startTrick()
            for j in range(4):
                index = (j + self.prioPlayer.id) % 4
                tempCard = None
                if index != 0:
                    tempCard = self.players[index].chooseCard(self)
                else:
                    tempCard = Render.player_choosing_cards(self)

                self.players[index].playCard(tempCard, self)
                self.addToTrick(tempCard, self.players[index]) 
                Render.draw_gameplay(self)
                if j != 3:
                    Render.card_sound.play()
                    time.sleep(1)
            self.evaluateTrick(index)

        self.getState = "GAME_OVER"

        
        Render.draw_game_over_screen(self)
        print("Ended player Game")

    #This method clears the old trick and adds it to pastTricks
    def startTrick(self):
        
        #save old trick
        if len(self.currentTrick) != 0:
            self.pastTricks.append(self.currentTrick)
        # reset variables for new trick
        self.currentTrick = [None, None, None, None]
        self.evalTrumpSuit = []
        self.evalCurSuit = []
        self.currentTrickSuit = None

    #Meant to be called in driver/main like board.addToTrick(board.player.playCard())
    #Errors if the currentTrick.len() is 4 or more
    #Sets currentTrickSuit to the first card in the CurrentTrickSuit
    def addToTrick(self, card, player):
        #set current trick suit if card is the first played
        if (self.currentTrickSuit == None):
            self.currentTrickSuit = card.suit

        self.currentTrick[player.id] = card

        #add cards to corresponding lists for evaluating winner 
        if (card.suit.name == self.trumpSuit.name):
            self.evalTrumpSuit.append(card)
            print("TRUMP SUIT PLAYED", card)
        if (card.suit == self.currentTrickSuit):
            self.evalCurSuit.append(card)

    #Game over function prints winner 
    def gameOver(self, winner) -> None:
        self.gameWon = True
        print("Team", winner, "wins!")

    #Looks at the cards in the trick and see who wins! Then sets prioPlayer to the owner of that card
    #Also updates the score
    def evaluateTrick(self, index):
        winner = None
        if self.trumpSuit != BetSuit.LOW:
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
        self.prioPlayer.inc_wins()
        
        if self.prioPlayer == self.players[index]:
            sound = Render.vine_boom
        else:
            sound = Render.card_sound
        sound.play()
        time.sleep(1)
        if (self.prioPlayer.id == 0 or self.prioPlayer.id == 2):
            self.teamOneScore += 1
            if (self.teamOneScore >= self.gamesToWin):
                self.gameOver(1)
                self.winningTeam = 1
        elif (self.prioPlayer.id == 1 or self.prioPlayer.id == 3):
            self.teamTwoScore += 1
            if (self.teamTwoScore >= 14-self.gamesToWin):
                self.gameOver(2)
                self.winningTeam = 2
        print("Player", self.prioPlayer.id, "wins the trick")
        print("1:", self.teamOneScore, " 2:", self.teamTwoScore, "\n")
        
    def inc_player(self):
        self.activePlayer += 1
        if self.activePlayer > 3:
            self.activePlayer = 0
