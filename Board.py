from Deck import Deck
from Player import Player

class Board():
    #Globals
    #ArrayList of previous rounds {(),()}
    #Team Score
    #Bet of the Game
    #Actions should be defined by 

    def __init__(self):
        currentTrick = []
        pastTricks = []

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

        
    