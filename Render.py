import os
import pygame
import math
import time
from BetSuit import BetSuit
from Suit import Suit
from BetButton import BetButton
from Board import Board

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
dark_green = (27, 45, 46)
tan = (210, 180, 140)
dark_red = (156, 33, 61)
light_red = (200, 33, 61)

def draw_menu_screen():
    pygame.init()
    pygame.display.set_caption("Bridge Game Main Menu")
    run = True
    while run:
        screen.fill(green)
        font = pygame.font.Font('freesansbold.ttf', 100)
        draw_centered_Text('Better Bridge Game!', font, white, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        border = submit_rect        
        #Text
        font = pygame.font.Font('freesansbold.ttf', 80)
        #draw_menu_button("MULTIPLAYER", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        multi_button = MenuButton("MULTIPLAYER", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//3), True)
        #draw_menu_button("SINGLE PLAYER", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        single_button = MenuButton("SINGLE PLAYER", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), True)
        #draw_menu_button("SETTINGS", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//6))
        setting_button = MenuButton("SETTINGS", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//6), True)
        #draw_menu_button("QUIT", font, white, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//3))
        quit_button = MenuButton("QUIT", font, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + SCREEN_HEIGHT//3), True)
        mouse_Pos = pygame.mouse.get_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if multi_button.check_click():
                pass
            if single_button.check_click():
                board = Board()
                board.getState = "BETTING"
                board.startBetting()
                board.startPlayerGame()
            if setting_button.check_click():
                pass
            if quit_button.check_click():
                run = False
            pygame.display.flip()
    pygame.display.quit()
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
        pygame.display.set_caption("Bridge Game [Playing...]")
        draw_scores(screen, board.teamOneScore, board.teamTwoScore, board.gamesToWin)
    draw_your_turn(board.yourTurn)
    #Draw betting UI, if applicable
    if board.getState == "BETTING":
        pygame.display.set_caption("Bridge Game [Betting...]")
        draw_bets(screen, board)
    if(board.getState == "GAME_OVER"):
        pygame.display.set_caption("Bridge Game [LeaderBoard]")
        draw_game_over_screen(board)
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
        

def draw_scores(screen, score_1, score_2, team_1_to_win):
    if team_1_to_win == 13:
        team_2_to_win = 1
    elif team_1_to_win == 0:
        team_1_to_win = 1
        team_2_to_win = 13
    else:
        team_2_to_win = 13 - team_1_to_win + 1
    #Background
    bgnd = pygame.Rect(220, 0, 210, 120)
    border_r = pygame.Rect(430, 0, 10, 130)
    border_b = pygame.Rect(220, 120, 210, 10)
    border_m = pygame.Rect(320, 0, 10, 130)
    pygame.draw.rect(screen, gray, bgnd)
    pygame.draw.rect(screen, black, border_r)
    pygame.draw.rect(screen, black, border_b, 5)
    pygame.draw.rect(screen, black, border_m, 5)
    #Text
    font = pygame.font.Font('freesansbold.ttf', 40)
    draw_centered_Text(str(score_1) + " / " + str(team_1_to_win) , font, black, (272, 60)) #Text1
    draw_centered_Text(str(score_2) + " / " + str(team_2_to_win), font, black, (378, 60)) #Text2

def draw_game_over_screen(board):
   screen.fill(tan)
   font = pygame.font.SysFont('georgia', 100)
   draw_centered_Text("Game Over", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//14))
   font = pygame.font.SysFont('georgia', 70)
   draw_centered_Text("Team " + str(board.winningTeam) + " Wins!", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//5))
   font = pygame.font.SysFont('georgia', 60)
   draw_centered_Text("LeaderBoard:", font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3))
   font = pygame.font.SysFont('georgia', 50)
   leaderboard = sorted(board.players,key=lambda x: x.wins, reverse=True)
   space:int = 80
   num = 1
   for player in leaderboard:
       draw_centered_Text(str(num) + ". " + str(player) + ", SCORE: " + str(player.wins), font, white, (SCREEN_WIDTH/2, SCREEN_HEIGHT//3 + space))
       pygame.display.update()
       space += 50
       num += 1
       time.sleep(1)
   running = True
   while running:
       try_again_button = MenuButton("TRY AGAIN", font, (SCREEN_WIDTH-160, SCREEN_HEIGHT-170), True)
       menu_button = MenuButton("MENU", font, (SCREEN_WIDTH-160, SCREEN_HEIGHT-80), True)
       pygame.display.update()
       for event in pygame.event.get():
        if try_again_button.check_click(): #Work on later
            pass
        if menu_button.check_click():
            running = False
        if event == pygame.QUIT:
            running = False

def draw_your_turn(isYourTurn: bool):
    font = pygame.font.SysFont('georgia', 40)
    if isYourTurn:
         draw_centered_Text("Your Turn!", font, white, (SCREEN_WIDTH-115, 30))
    else:
         draw_centered_Text("Waiting...", font, white, (SCREEN_WIDTH-115, 30))

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
'''
def draw_menu_button(text: str, font, text_col: tuple, center: tuple):
    (width, height) = font.size(text)
    inner_button = pygame.Rect(0,0, width + 20, height + 20)
    shade_button = pygame.Rect(0, 0, width + 10, height + 10)
    outline = pygame.Rect(0,0, width + 22, height + 22)
    inner_button.center = center
    outline.center = center
    shade_button.center = center
    #shading background
    backgrnd_shade = pygame.Rect(0, 0, width + 22, height + 22)
    (x,y) = center
    backgrnd_shade.center = (x+5, y+ 5)
    pygame.draw.rect(screen, dark_green, backgrnd_shade, 0, 15, 15, 15, 15, 15)
    pygame.draw.rect(screen, dark_red, inner_button, 0, 15, 15, 15, 15, 15)
    pygame.draw.rect(screen, light_red, shade_button, 0, 15, 15, 15, 15, 15)
    pygame.draw.rect(screen, black, outline, 2, 15, 15, 15, 15, 15)
    draw_centered_Text(text, font, text_col, center)
'''
class MenuButton:
    def __init__(self, text: str, font, center: tuple, enabled: bool) -> None:
        self.text = text
        self.font = font
        self.center = center
        self.enabled = enabled
        self.rect = self.draw(False)
    def draw(self, clicked: bool):
        (width, height) = self.font.size(self.text)
        self.inner_button = pygame.Rect(0,0, width + 20, height + 20)
        self.shade_button = pygame.Rect(0, 0, width + 10, height + 10)
        self.outline = pygame.Rect(0,0, width + 22, height + 22)
        self.inner_button.center = self.center
        self.outline.center = self.center
        (self.xpos, self.ypos) = self.outline.topleft
        self.shade_button.center = self.center
        #shading background
        backgrnd_shade = pygame.Rect(0, 0, width + 22, height + 22)
        (x,y) = self.center
        backgrnd_shade.center = (x+5, y+ 5)
        pygame.draw.rect(screen, dark_green, backgrnd_shade, 0, 15, 15, 15, 15, 15)
        pygame.draw.rect(screen, dark_red, self.inner_button, 0, 15, 15, 15, 15, 15)
        if not clicked:
            pygame.draw.rect(screen, light_red, self.shade_button, 0, 15, 15, 15, 15, 15)
        pygame.draw.rect(screen, black, self.outline, 2, 15, 15, 15, 15, 15)
        draw_centered_Text(self.text, self.font, white, self.center)
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos
        left_click = pygame.mouse.get_pressed()[0]
        buttonrect = self.outline
        if left_click and buttonrect.collidepoint(mouse_pos()[0], mouse_pos()[1]) and self.enabled:
            self.draw(True)
            return True
        else:
            self.draw(False)
            return False
        