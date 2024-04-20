from Card import Card
from Rank import Rank
from Suit import Suit
import os
import pygame
pygame.init()

SCREEN_WIDTH = 750

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_WIDTH])

def draw():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Draw the background
        screen.fill((27, 99, 46))
        #Draw the player hand
        #Draw the pile
        #Draw the trump suit/bet
        #Draw the score (rounds won)
        
        pygame.display.flip()
    pygame.quit()

#Returns the path to the image associated with card
def get_png_from_card(card):
    output = ""
    rank_val = card.rank.value
    if rank_val >= 11:
        output += card.rank.name.lower()
    else:
        output += str(rank_val)
    output += "_of_"
    output += card.suit.name.lower()
    output += ".png"
    return os.path.join("Cards", output)
