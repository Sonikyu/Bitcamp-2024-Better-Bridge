from Card import Card
from Rank import Rank
from Suit import Suit
import os
import pygame
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
CARD_WIDTH = 100
CARD_HEIGHT = 145
HAND_Y = SCREEN_HEIGHT - (CARD_HEIGHT + 20)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw(hand, pile):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Draw the background
        screen.fill((27, 99, 46))
        #Draw the player hand
        hand_offset = (SCREEN_WIDTH - ((len(hand) + 1) * (CARD_WIDTH * 2 / 3))) / 2
        loc_offset = 0
        for card in hand:
            draw_card(screen, card, hand_offset + loc_offset*CARD_WIDTH * 2/3, HAND_Y)
            loc_offset += 1
        #Draw the pile
        draw_pile(screen, pile)
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

#Draws an individual card at x,y
def draw_card(screen, card, x, y):
    img_path = get_png_from_card(card)
    img = pygame.image.load(img_path)
    screen.blit(img, (x,y))

def draw_pile(screen, pile):
    #SOUTH
    if pile[0] != None:
        draw_card(screen, pile[0], SCREEN_WIDTH / 2 - CARD_WIDTH / 2, SCREEN_HEIGHT /2)
    #WEST
    if pile[1] != None:
        draw_card(screen, pile[1], SCREEN_WIDTH / 2 - CARD_WIDTH * 1.5, SCREEN_HEIGHT /2 - CARD_HEIGHT * .75)
    #NORTH
    if pile[2] != None:
        draw_card(screen, pile[2], SCREEN_WIDTH / 2 - CARD_WIDTH / 2, SCREEN_HEIGHT /2 - CARD_HEIGHT * 1.5) 
    #EAST
    if pile[3] != None:
        draw_card(screen, pile[3], SCREEN_WIDTH / 2 + CARD_WIDTH * .5, SCREEN_HEIGHT /2 - CARD_HEIGHT * .75)