import os
import pygame
import math
from BetSuit import BetSuit
from Suit import Suit
from BetButton import BetButton

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750
CARD_WIDTH = 100
CARD_HEIGHT = 145
HAND_Y = SCREEN_HEIGHT - (CARD_HEIGHT + 20)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

size_bet_rects = []
suit_bet_rects = []
pass_rect = pygame.Rect(820, 315, 100, 100)
submit_rect = pygame.Rect(730, 405, 190, 75)

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
    
    if(board.game_state == "GAME_OVER"):
        draw_game_over_screen()

    if board.getState == "PLAYING":
        draw_scores(screen, board.teamOneScore, board.teamTwoScore)
    #Draw betting UI, if applicable
    if board.getState == "BETTING":
        draw_bets(screen, board)
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

def get_glyph_from_suit(suit):
    glyph_name = suit.name.lower() + "_glyph.png"
    glyph_path = os.path.join("Cards", glyph_name)
    img = pygame.image.load(glyph_path)
    return img

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
    img = get_glyph_from_suit(suit)
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

def draw_game_over_screen():
   screen.fill((210, 180, 140))
   font = pygame.font.SysFont('georgia', 40)
   title = font.render('Game Over', True, (255, 255, 255))
   screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
   pygame.display.update()
def draw_bets(screen, board):
    global size_bet_rects
    global suit_bet_rects
    size_bet_rects = []
    suit_bet_rects = []
    #Calculate how many numbers are valid
    bet_id = board.currentBetID
    lowest_bet_size = math.floor(math.fabs(bet_id) / 6) + 7
    #Draw size boxes
    for i in range(lowest_bet_size, 14):
        rect = draw_size_bet_box(screen, i, 280 + 90*(i - lowest_bet_size), 225)
        size_bet_rects.append(rect)
    #Draw suit boxes
    for betsuit in BetSuit:
        rect = draw_suit_bet_box(screen, betsuit, 280 + 90*(betsuit.value), 315)
        suit_bet_rects.append(rect)
    #Draw pass button
    border = pass_rect
    bgnd = pygame.Rect(830, 325, 80, 80)
    pygame.draw.rect(screen, (0,0,0), border)
    pygame.draw.rect(screen, (179,202,141), bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("PASS", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (870,365)
    screen.blit(text, text_rect)
    #Draw submit button
    border = submit_rect
    bgnd = pygame.Rect(740, 415, 170, 55)
    pygame.draw.rect(screen, (0,0,0), border)
    pygame.draw.rect(screen, (156, 33, 61), bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render("SUBMIT", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (825,442.5)
    screen.blit(text, text_rect)

def draw_size_bet_box(screen, size, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, (0,0,0), border)
    pygame.draw.rect(screen, (170, 170, 170), bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render(str(size), True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (x+50,y+50)
    screen.blit(text, text_rect)
    return BetButton(border, size, None)

def draw_suit_bet_box(screen, betsuit, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, (0,0,0), border)
    pygame.draw.rect(screen, (170, 170, 170), bgnd)
    #Contents
    font = pygame.font.Font('freesansbold.ttf', 30)
    if betsuit.value == 0:
        text = font.render("LOW", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x+50,y+50)
        screen.blit(text, text_rect)
    elif betsuit.value == 5:
        text = font.render("HIGH", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x+50,y+50)
        screen.blit(text, text_rect)
    else:
        img = get_glyph_from_suit(Suit(betsuit.value))
        img_rect = img.get_rect()
        img_rect.center = (x+50, y+50)
        screen.blit(img, img_rect)
    return BetButton(border, None, betsuit)
