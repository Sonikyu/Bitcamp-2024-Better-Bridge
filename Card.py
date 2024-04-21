import pygame
import Render
class Card:
    #Cards have a rank, suit, and id
    #id is used for comparing
    #Cards also have x and y coordinates for drawing, and and image
    def __init__ (self, rank, suit, owner):
        self.rank = rank
        self.suit = suit
        self.id = suit.value * 13 + rank.value - 2
        self.owner = None
        self.x = 0
        self.y = Render.HAND_Y
        self.image = pygame.image.load(Render.get_png_from_card(self))

    #Checks if the other card is bigger than or less than the current card
    def __lt__ (self, otherCard):
        return self.id - otherCard.id
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def getOwner(self):
        return self.owner
    
    def setOwner(self, owner):
        self.owner = owner

    def __str__(self):
        return self.rank .name+  self.suit.name
    
