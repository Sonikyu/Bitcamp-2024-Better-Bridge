import pygame
import Render
class Card:
    #Cards have a rank, suit, and id
    #id is used for comparing
    #Cards also have x and y coordinates for drawing, and and image
    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.id = suit.value * 13 + rank.value - 2
        self.owner = None
        self.x = 0
        self.y = Render.HAND_Y
        self.image = pygame.image.load(Render.get_png_from_card(self)).convert()
        self.rect = self.image.get_rect()
        self.gravity = 0
        self.ground_position = Render.SCREEN_HEIGHT - Render.CARD_HEIGHT//2
        self.roof_position = Render.SCREEN_HEIGHT - Render.CARD_HEIGHT
        self.canBeDragged = False

    #Checks if the other card is bigger than or less than the current card
    def __lt__ (self, otherCard):
        return self.id - otherCard.id
    
    def setOwner(self, owner):
        self.owner = owner

    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"

    def player_hover(self):
        isColliding = self.rect.collidepoint(pygame.mouse.get_pos())
        if isColliding:
            self.gravity -= 5
            # self.canSlideDown = False
        else:
            #self.gravity += 2
            # self.canSlideDown = True
        # if self.canSlideDown == True:
            self.gravity += 5

    def gravity_update(self):
        self.player_hover()
        self.rect.move_ip(0,self.gravity)
        if self.rect.y > self.ground_position:
            self.rect.y = self.ground_position
            self.gravity = 0
            # self.canSlideUp = True
            # self.canSlideDown = False
        if self.rect.y < self.roof_position:
             self.rect.y = self.roof_position
             self.gravity = 0
            #  self.canSlideUp = False
            #  self.canSlideDown = True
    def update_drag_state(self, state: bool):
        self.canBeDragged = state
    
    # def drag_card(self, event):
    #     if (event.type == pygame.MOUSEBUTTONDOWN and self.canBeDragged):

            