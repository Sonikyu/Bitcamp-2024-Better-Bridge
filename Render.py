import os
import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
CARD_WIDTH = 100
CARD_HEIGHT = 145
HAND_Y = SCREEN_HEIGHT - (CARD_HEIGHT + 20)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw(board):
    #Draw the background
    screen.fill((27, 99, 46))
    #Draw the player hand
    hand_offset = (SCREEN_WIDTH - ((len(board.player1.hand) + 1) * (CARD_WIDTH * 2 / 3))) / 2
    loc_offset = 0
    for card in board.player1.hand:       
        screen.blit(card.image, (hand_offset + loc_offset*CARD_WIDTH * 2/3, HAND_Y))
        loc_offset += 1
    #Draw the pile
    draw_pile(screen, board.currentTrick)
    #Draw the trump suit
    draw_trump(screen, board.trumpSuit)
    #Draw the score (rounds won)
    draw_scores(screen, board.teamOneScore, board.teamTwoScore)
    
    pygame.display.flip()

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

#Draws the pile in the center of the screen, pile MUST be length 4 with None for any position not yet filled
def draw_pile(screen, pile):
    #SOUTH
    if pile[0] != None:
        screen.blit(pile[0].image, (SCREEN_WIDTH / 2 - CARD_WIDTH / 2, SCREEN_HEIGHT /2))
    #WEST
    if pile[1] != None:
        screen.blit(pile[1].image, (SCREEN_WIDTH / 2 - CARD_WIDTH * 1.5, SCREEN_HEIGHT /2 - CARD_HEIGHT * .75))
    #NORTH
    if pile[2] != None:
        screen.blit(pile[2].image, (SCREEN_WIDTH / 2 - CARD_WIDTH / 2, SCREEN_HEIGHT /2 - CARD_HEIGHT * 1.5))
    #EAST
    if pile[3] != None:
        screen.blit(pile[3].image, (SCREEN_WIDTH / 2 + CARD_WIDTH * .5, SCREEN_HEIGHT /2 - CARD_HEIGHT * .75))

def draw_trump(screen, suit):
    if suit == None:
        return
    #Background
    bgnd = pygame.Rect(0, 0, 210, 120)
    border_r = pygame.Rect(210, 0, 10, 130)
    border_b = pygame.Rect(0, 120, 210, 10)
    pygame.draw.rect(screen, (170, 170, 170), bgnd)
    pygame.draw.rect(screen, (0, 0, 0), border_r)
    pygame.draw.rect(screen, (0, 0, 0), border_b)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 20)
    msg = "Trump: " + suit.name
    text = font.render(msg, True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (105, 30)
    screen.blit(text, textRect)
    #Glyph
    glyph_name = suit.name.lower() + "_glyph.png"
    glyph_path = os.path.join("Cards", glyph_name)
    img = pygame.image.load(glyph_path)
    img_rect = img.get_rect()
    img_rect.center = (105, 80)
    screen.blit(img, img_rect)

def draw_scores(screen, score_1, score_2):
    #Background
    bgnd = pygame.Rect(220, 0, 210, 120)
    border_r = pygame.Rect(430, 0, 10, 130)
    border_b = pygame.Rect(220, 120, 210, 10)
    border_m = pygame.Rect(320, 0, 10, 130)
    pygame.draw.rect(screen, (170, 170, 170), bgnd)
    pygame.draw.rect(screen, (0, 0, 0), border_r)
    pygame.draw.rect(screen, (0, 0, 0), border_b)
    pygame.draw.rect(screen, (0, 0, 0), border_m)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 40)
    text1 = font.render(str(score_1), True, (0,0,0))
    text2 = font.render(str(score_2), True, (0,0,0))
    text1_rect = text1.get_rect()
    text2_rect = text2.get_rect()
    text1_rect.center = (272, 60)
    text2_rect.center = (378, 60)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
