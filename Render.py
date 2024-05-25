import os
import pygame
import math
import time
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

#Colors
black = (0,0,0)
white = (255,255,255)
gray = (170,170,170)
green = (27, 99, 46)
light_green = (179,202,141)
tan = (210, 180, 140)
dark_red = (156, 33, 61)

def draw_menu_screen():
    pygame.display.set_caption("Bridge Game Main Menu")
    font = pygame.font.Font('freesansbold.ttf', 100)
    run = True
    while run:
        screen.fill(green)
        draw_centered_Text('Better Bridge Game!', font, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        mouse_Pos = pygame.mouse.get_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pygame.display.update()
    pygame.quit()

def draw(board):
    #Draw the background
    screen.fill(green)
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
    
    if board.getState == "PLAYING":
        draw_scores(screen, board.teamOneScore, board.teamTwoScore)
    draw_your_turn(board.yourTurn)
    #Draw betting UI, if applicable
    if board.getState == "BETTING":
        draw_bets(screen, board)
    if(board.getState == "GAME_OVER"):
        draw_game_over_screen(board.winningTeam)
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
    pygame.draw.rect(screen, gray, bgnd)
    pygame.draw.rect(screen, black, border_r)
    pygame.draw.rect(screen, black, border_b)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 20)
    draw_centered_Text("Trump: " + suit.name, font, black, (105, 30))
    #Glyph
    if (suit != BetSuit.LOW and suit != BetSuit.HIGH):
        img = get_glyph_from_suit(suit)
        draw_centered_Element(img, (105, 80))
        

def draw_scores(screen, score_1, score_2):
    #Background
    bgnd = pygame.Rect(220, 0, 210, 120)
    border_r = pygame.Rect(430, 0, 10, 130)
    border_b = pygame.Rect(220, 120, 210, 10)
    border_m = pygame.Rect(320, 0, 10, 130)
    pygame.draw.rect(screen, gray, bgnd)
    pygame.draw.rect(screen, black, border_r)
    pygame.draw.rect(screen, black, border_b)
    pygame.draw.rect(screen, black, border_m)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 40)
    draw_centered_Text(str(score_1), font, black, (272, 60)) #Text1
    draw_centered_Text(str(score_2), font, black, (378, 60)) #Text2

def draw_game_over_screen(winningTeam):
   screen.fill(tan)
   font = pygame.font.SysFont('georgia', 40)
   draw_centered_Text("Game Over", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
   draw_centered_Text("Team " + str(winningTeam) + " Wins!", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40))

   pygame.display.update()
   time.sleep(10)

def draw_your_turn(isYourTurn: bool):
    font = pygame.font.SysFont('georgia', 40)
    if isYourTurn:
         draw_centered_Text("Your Turn!", font, white, (SCREEN_WIDTH-115, 30))
    else:
         draw_centered_Text("Waiting!", font, white, (SCREEN_WIDTH-115, 30))

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
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, light_green, bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    draw_centered_Text("PASS", font, black, (870,365))
    #Draw submit button
    border = submit_rect
    bgnd = pygame.Rect(740, 415, 170, 55)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, dark_red, bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 30)
    draw_centered_Text("SUBMIT", font, black, (825,442.5))

def draw_size_bet_box(screen, size, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, gray, bgnd)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 40)
    draw_centered_Text(str(size), font, black, (x+50,y+50))
    return BetButton(border, size, None)

def draw_suit_bet_box(screen, betsuit, x, y):
    #Background
    border = pygame.Rect(x, y, 100, 100)
    bgnd = pygame.Rect(x + 10, y + 10, 80, 80)
    pygame.draw.rect(screen, black, border)
    pygame.draw.rect(screen, gray, bgnd)
    #Contents
    font = pygame.font.Font('freesansbold.ttf', 30)
    if betsuit.value == 0:
        draw_centered_Text("LOW", font, black, (x+50,y+50))
    elif betsuit.value == 5:
        draw_centered_Text("HIGH", font, black,(x+50,y+50))
    else:
        img = get_glyph_from_suit(Suit(betsuit.value))
        draw_centered_Element(img, (x+50, y+50))
    return BetButton(border, None, betsuit)
#Helper Functions
def draw_centered_Text(text: str, font, text_col: tuple, center: tuple):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect()
    img_rect.center = center
    screen.blit(img, img_rect)
def draw_centered_Element(img, center: tuple):
    img_rect = img.get_rect()
    img_rect.center = center
    screen.blit(img, img_rect)